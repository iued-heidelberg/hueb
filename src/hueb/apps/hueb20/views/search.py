import csv
import logging

import beeline
from django import forms
from django.contrib.auth.models import User
from django.db.models import F, Q, BooleanField
from django.forms.formsets import BaseFormSet, formset_factory
from django.http import StreamingHttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from hueb.apps.hueb20.models import DdcGerman
from hueb.apps.hueb20.models.document import Document, DocumentRelationship
from hueb.apps.hueb20.models.language import Language
from hueb.apps.hueb20.models.comment import Comment
from hueb.apps.hueb20.models.utils import HUEB_APPLICATIONS, timerange_serialization
from hueb.apps.tenants.models import (
    TENANT_APPS,
    TENANT_PREFIX_TO_COLOR,
    TENANT_PREFIX_TO_TITLE,
)
from hueb.apps.tenants.utils import tenant_from_request
from django.contrib.postgres.search import (
    TrigramBase,
    TrigramSimilarity,
    TrigramDistance,
)


# Get an instance of a logger
logger = logging.getLogger(__name__)


class TrigramWordSimilarity(TrigramBase):
    output_field = BooleanField()
    function = ""
    arg_joiner = " %%> "


class TypeCheckboxWidget(forms.widgets.CheckboxSelectMultiple):
    template_name = "hueb20/search/widgets/checkbox.html"
    option_template_name = "hueb20/search/widgets/checkbox_centered_option.html"


class SearchSelectWidget(forms.widgets.Select):
    template_name = "hueb20/search/widgets/select.html"


class TruncatingSearchSelectWidget(forms.widgets.Select):
    template_name = "hueb20/search/widgets/truncatingSelect.html"


class SearchForm(forms.Form):
    operator_choices = (("and", _("Und")), ("or", _("Oder")), ("not", _("Nicht")))

    operator = forms.ChoiceField(choices=operator_choices, widget=SearchSelectWidget)
    attribute = forms.ChoiceField(
        choices=Document.searchable_attributes, widget=SearchSelectWidget
    )

    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": _("Suchbegriff"),
            }
        ),
    )

    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": _("Suchbegriff"),
            }
        ),
    )

    search_comment = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": _("Suchbegriff"),
            }
        ),
    )

    search_year_mode = forms.ChoiceField(
        choices=(("range", _("Range")), ("approx", _("± 10 years"))),
        widget=SearchSelectWidget,
    )

    search_year_from = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "min": 0,
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": _("von"),
            }
        ),
    )
    search_year_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "min": 0,
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": _("bis"),
            }
        ),
    )
    """
    search_ddc = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "min": 00,
                "step": 10,
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": _("DDC Nummer"),
            }
        ),
    )
    """

    def get_search_ddc_choices():
        ddcs = DdcGerman.objects.all().order_by("ddc_number")
        choices = []
        for i in range(0, len(ddcs), 100):
            category = []
            for num in range(i, i + 100, 10):
                category.append((ddcs[num].ddc_number, ddcs[num]))
            category = tuple(category)
            cat_name = ddcs[i]
            choices.append((cat_name, category))
        return tuple(choices)

    search_ddc = forms.ChoiceField(
        choices=get_search_ddc_choices(),
        widget=TruncatingSearchSelectWidget,
    )

    search_language = forms.ChoiceField(
        choices=tuple(
            (language, language)
            for language in Language.objects.filter()
            .exclude(language_de="")  # bad manual coding, but couldn't find another way
            .exclude(language_en="")
            .all()
            .order_by(
                "language_de"
            )  # could not find a language dynamic way (check again!)
        ),
        widget=SearchSelectWidget,
    )

    search_database = forms.ChoiceField(
        choices=HUEB_APPLICATIONS + TENANT_APPS,
        widget=SearchSelectWidget,
    )


class BaseSearchFormSet(BaseFormSet):
    base_queryset = (
        DocumentRelationship.objects.prefetch_related("document_to__written_by")
        .prefetch_related("document_to__contribution_set__person")
        .select_related("document_to__ddc")
        .select_related("document_to__language")
        .prefetch_related("document_to__document_comment")
        .prefetch_related("document_from__written_by")
        .prefetch_related("document_from__contribution_set__person")
        .select_related("document_from__ddc")
        .select_related("document_from__language")
        .prefetch_related("document_from__document_comment")
    )

    def create_fuzzy_annotations(self, queryset):
        for form in self:
            if form.cleaned_data["attribute"] == "title":
                queryset = queryset.annotate(
                    document_from_title_similarity=TrigramWordSimilarity(
                        "document_from__title", form.cleaned_data["search_text"]
                    ),
                    document_to_title_similarity=TrigramWordSimilarity(
                        "document_to__title", form.cleaned_data["search_text"]
                    ),
                    document_from_subtitle_similarity=TrigramWordSimilarity(
                        "document_from__subtitle", form.cleaned_data["search_text"]
                    ),
                    document_to_subtitle_similarity=TrigramWordSimilarity(
                        "document_to__subtitle", form.cleaned_data["search_text"]
                    ),
                )

        return queryset

    def get_query_object(
        self,
        types=[Document.ORIGINAL, Document.TRANSLATION, Document.BRIDGE],
        online_only=False,
        fuzzy=False,
    ):
        base_queryset = self.base_queryset

        with beeline.tracer(name="building_search_query"):
            include_q_objects = Q()
            exclude_q_objects = Q()

            beeline.add_context_field("form_data", self.cleaned_data)

            if fuzzy:
                base_queryset = self.create_fuzzy_annotations(base_queryset)

            for form in self:
                if form.cleaned_data["search_year_mode"] == "approx":
                    form.cleaned_data["search_year_to"] = (
                        form.cleaned_data["search_year_from"] + 10
                    )
                    form.cleaned_data["search_year_from"] = (
                        form.cleaned_data["search_year_from"] - 10
                    )

                form.cleaned_data["fuzzy"] = fuzzy
                q = DocumentRelationship.get_q_object(form.cleaned_data, types)
                operator = form.cleaned_data["operator"]

                if operator == "and":
                    include_q_objects &= q
                elif operator == "or":
                    include_q_objects |= q
                elif operator == "not":
                    exclude_q_objects |= q

            # This is necessary or the query breaks if only not operators are used. It's a bit of a hack, but it works.
            include_q_objects &= DocumentRelationship.get_q_object(
                {"attribute": "title", "search_text": "", "fuzzy": False}, types
            )

            beeline.add_context_field("include_q_objects", include_q_objects)
            beeline.add_context_field("exclude_q_objects", exclude_q_objects)

            queryset = base_queryset
            if include_q_objects != Q():
                queryset = queryset.filter(include_q_objects)
            if exclude_q_objects != Q():
                queryset = queryset.exclude(exclude_q_objects)

            if online_only:
                queryset = queryset.filter(
                    document_to__filing__archive__name="Online-Version"
                )

            doc_froms = queryset.values_list("document_from", flat=True)
            if queryset.filter(document_to__in=doc_froms).exists():
                queryset = queryset.exclude(
                    id__in=queryset.filter(document_to__in=doc_froms).all()
                )

            queryset = queryset.exclude(document_to__hidden=True)
            queryset = queryset.exclude(document_from__hidden=True)

            return queryset.distinct()

    def get_title_queries(self):
        search_texts = []
        for form in self:
            data = form.cleaned_data
            if data["attribute"] == "title" and data["search_text"]:
                if data["operator"] == "and" or data["operator"] == "or":
                    search_texts.append(data["search_text"])
        return search_texts

    def get_comment_queries(self):
        search_texts = []
        for form in self:
            data = form.cleaned_data
            if data["attribute"] == "comment" and data["search_text"]:
                if data["operator"] == "and" or data["operator"] == "or":
                    search_texts.append(data["search_text"])
        return search_texts


class SortForm(forms.Form):
    sort_attribute = forms.ChoiceField(
        choices=Document.sortable_attributes,
        widget=SearchSelectWidget,
    )
    sort_type = forms.ChoiceField(
        choices=(("document_from", _("Original")), ("document_to", _("Übersetzung"))),
        widget=SearchSelectWidget,
    )
    sort_direction = forms.ChoiceField(
        choices=(("asc", _("Aufsteigend")), ("desc", _("Absteigend"))),
        widget=SearchSelectWidget,
    )

    def get_order_by(self):
        return (
            self.cleaned_data["sort_direction"],
            self.cleaned_data["sort_type"],
            self.cleaned_data["sort_attribute"],
        )


class TypeForm(forms.Form):
    type = forms.MultipleChoiceField(
        widget=TypeCheckboxWidget(
            attrs={
                "style": "width:20px; height:20px;",
            }
        ),
        choices=(
            (Document.ORIGINAL, _("Originale")),
            (Document.TRANSLATION, _("Übersetzungen")),
            (Document.BRIDGE, _("Brückenübersetzungen")),
        ),
    )

    online_only = forms.MultipleChoiceField(  # Easier than making boolean field and adding custom widget for label
        required=False,
        widget=TypeCheckboxWidget(
            attrs={
                "style": "width:20px; height:20px;",
            }
        ),
        choices=((True, _("Online accessible documents only")),),
    )

    fuzzy = forms.BooleanField(
        required=False,
        label=_("Fuzzy search"),
    )


class Search(ListView):
    template_name = "hueb20/search/search.html"
    model = Document
    paginate_by = 20

    SearchFormset = formset_factory(
        SearchForm,
        formset=BaseSearchFormSet,
        extra=0,
        min_num=1,
        max_num=6,
        validate_max=True,
        validate_min=True,
    )

    def get_queryset(self):
        formset = self.SearchFormset(data=self.request.GET)
        sortform = SortForm(data=self.request.GET)
        typeform = TypeForm(data=self.request.GET)

        if formset.is_valid() and typeform.is_valid():
            types = typeform.cleaned_data["type"]
            online_only = typeform.cleaned_data["online_only"]
            fuzzy = typeform.cleaned_data["fuzzy"]
            queryset = formset.get_query_object(types, online_only, fuzzy)
            if sortform.is_valid():
                orderDir, documentType, orderBy = sortform.get_order_by()
                if orderDir == "asc":
                    return (
                        queryset.all()
                        .order_by(F(documentType + "__" + orderBy).asc(nulls_last=True))
                        .distinct()
                    )
                else:
                    return (
                        queryset.all()
                        .order_by(
                            F(documentType + "__" + orderBy).desc(nulls_last=True)
                        )
                        .distinct()
                    )
            else:
                return (
                    queryset.all()
                    .order_by(F("document_from__id").asc(nulls_last=True))
                    .distinct()
                )
        else:
            if sortform.is_valid():
                orderDir, documentType, orderBy = sortform.get_order_by()
                if orderDir == "asc":
                    return (
                        BaseSearchFormSet.base_queryset.all()
                        .order_by(F(documentType + "__" + orderBy).asc(nulls_last=True))
                        .distinct()
                    )
                else:
                    return (
                        BaseSearchFormSet.base_queryset.all()
                        .order_by(
                            F(documentType + "__" + orderBy).desc(nulls_last=True)
                        )
                        .distinct()
                    )
            else:
                # Filter by tenant app if no search is performed
                tenant = tenant_from_request(self.request)
                app = tenant.app if tenant else "HUEB20"
                q_object = Q(document_from__app=app) | Q(document_to__app=app)

                return (
                    BaseSearchFormSet.base_queryset.filter(q_object)
                    .order_by(F("document_from__id").asc(nulls_last=True))
                    .distinct()
                )

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        # check if self.request.GET is empty
        if not self.request.GET:
            tenant = tenant_from_request(self.request)
            app = tenant.app if tenant else "HUEB20"
            formset = self.SearchFormset(
                initial=[
                    {"search_text": "", "attribute": "title"},
                    {"search_database": app, "attribute": "app"},
                ]
            )

        else:
            formset = self.SearchFormset(data=self.request.GET)
            if not formset.is_valid():
                formset = self.SearchFormset()

        context["formset"] = formset

        sortform = SortForm(data=self.request.GET)
        if not sortform.is_valid():
            sortform = SortForm()
        context["sortform"] = sortform

        typeform = TypeForm(data=self.request.GET)
        if not typeform.is_valid():
            typeform = TypeForm(
                initial={
                    "type": [Document.ORIGINAL, Document.TRANSLATION, Document.BRIDGE]
                }
            )
            context["types"] = None
        else:
            context["types"] = typeform.cleaned_data["type"]
        context["typeform"] = typeform

        if formset.is_valid():
            context["title_queries"] = formset.get_title_queries()
        else:
            context["title_queries"] = []

        context["tenant_colors"] = TENANT_PREFIX_TO_COLOR
        context["tenant_titles"] = TENANT_PREFIX_TO_TITLE

        return context

    def get(self, request, *args, **kwargs):
        if "download" in request.GET:
            if not User.is_authenticated:
                return redirect(reverse("login"))
            queryset = self.get_queryset()
            return self.export_to_csv(queryset)
        else:
            return super().get(request, *args, **kwargs)

    def export_to_csv(self, queryset):
        # Optimize queryset prefetching to minimize redundant queries
        queryset = queryset.select_related(
            "document_from__cultural_circle",
            "document_to__cultural_circle",
            "document_to__language",
            "document_from__language",
        ).prefetch_related(
            "document_from__filing_set__archive",
            "document_to__filing_set__archive",
            "document_to__translations",
            "document_from__contribution_set__person__cultural_circle",
            "document_to__contribution_set__person__cultural_circle",
            "document_from__originals__language",
            "document_from__document_comment",
            "document_to__document_comment",
            "document_from__originals__document_comment",
        )

        def get_value(obj, attr, default="-"):
            if attr is None:
                return default
            return getattr(obj, attr, default) if obj else default

        def get_queryset_values(queryset, field, separator=", "):
            return (
                separator.join(
                    [
                        value if value else "-"
                        for value in queryset.values_list(field, flat=True)
                    ]
                )
                if queryset.exists()
                else "-"
            )

        def construct_row(docs):
            doc_from, doc_to = docs.document_from, docs.document_to
            orig_is_bridge = doc_from.originals.exists() if doc_from else False
            orig_lang = (
                get_value(doc_from.originals.first(), "language")
                if orig_is_bridge
                else get_value(doc_from, "language")
            )

            doc_to_data = [
                get_value(doc_to, "title"),
                get_value(doc_to, "subtitle"),
                str(bool(doc_to.translations.exists() if doc_to else False)),
                get_value(doc_from, "title" if orig_is_bridge else None),
                get_value(doc_to, "edition"),
                (
                    get_queryset_values(doc_to.get_authors(), "person__name")
                    if doc_to
                    else "-"
                ),
                doc_to.serialize_written_in() if doc_to else "-",
                (
                    get_queryset_values(doc_to.get_publishers(), "person__name")
                    if doc_to
                    else "-"
                ),
                get_value(doc_to, "published_location"),
                (
                    get_queryset_values(doc_to.filing_set, "archive__name")
                    if doc_to
                    else "-"
                ),
                (
                    get_value(
                        doc_to.filing_set.filter(
                            archive__name="Online-Version"
                        ).first(),
                        "link",
                    )
                    if doc_to
                    else "-"
                ),
                get_value(doc_to, "language"),
                orig_lang,
                get_value(doc_from, "language" if orig_is_bridge else None),
                get_value(doc_to, "ddc"),
                doc_to.get_cultural_circle() if doc_to else "-",
                list(doc_to.get_comments() if doc_to else []),
            ]

            doc_from_data = []
            if doc_from:
                if orig_is_bridge:
                    orig = doc_from.originals.first()
                    doc_from_data = [
                        get_queryset_values(doc_from.originals, "title"),
                        get_queryset_values(doc_from.originals, "subtitle"),
                        get_queryset_values(orig.get_authors(), "person__name"),
                        get_value(orig, "edition"),
                        get_value(orig, "written_in"),
                        get_queryset_values(orig.get_publishers(), "person__name"),
                        get_value(orig, "published_location"),
                        get_queryset_values(orig.get_filings(), "archive__name"),
                        get_value(
                            orig.filing_set.filter(
                                archive__name="Online-Version"
                            ).first(),
                            "link",
                        ),
                        list(orig.get_comments()),
                    ]
                else:
                    doc_from_data = [
                        get_value(doc_from, "title"),
                        get_value(doc_from, "subtitle"),
                        get_queryset_values(doc_from.get_authors(), "person__name"),
                        get_value(doc_from, "edition"),
                        doc_from.serialize_written_in(),
                        get_queryset_values(doc_from.get_publishers(), "person__name"),
                        get_value(doc_from, "published_location"),
                        get_queryset_values(doc_from.filing_set, "archive__name"),
                        get_value(
                            doc_from.filing_set.filter(
                                archive__name="Online-Version"
                            ).first(),
                            "link",
                        ),
                        list(doc_from.get_comments()),
                    ]
            else:
                doc_from_data = ["-" for _ in range(10)]

            return doc_to_data + doc_from_data + [get_value(doc_from or doc_to, "app")]

        def row_generator(queryset):
            yield [
                "Translation Title",
                "Subtitle",
                "Is Intermediary",
                "Intermediary",
                "Edition",
                "Translator",
                "Year",
                "Publisher",
                "Publication Place",
                "Locations",
                "Link",
                "Language",
                "Original Language",
                "Intermediary Language",
                "DDC",
                "Cultural Circle",
                "Comment",
                "Original Title",
                "Original Subtitle",
                "Author",
                "Original Edition",
                "Original Year",
                "Original Publisher",
                "Original Publication Place",
                "Original Locations",
                "Original Link",
                "App",
            ]

            for docs in queryset:
                yield construct_row(docs)
                if docs.document_from and docs.document_from.originals.exists():
                    for orig in docs.document_from.originals.all():
                        yield construct_row(
                            type(
                                "Dummy",
                                (),
                                {
                                    "document_from": orig,
                                    "document_to": docs.document_from,
                                },
                            )
                        )

        class Echo:
            def write(self, value):
                return value

        pseudo_buffer = Echo()
        writer = csv.writer(
            pseudo_buffer, delimiter=";", dialect="excel", quoting=csv.QUOTE_ALL
        )
        return StreamingHttpResponse(
            (writer.writerow(row) for row in row_generator(queryset)),
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="docExport.csv"'},
        )
