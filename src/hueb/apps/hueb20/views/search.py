import csv
import logging

import beeline
from django import forms
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.forms.formsets import BaseFormSet, formset_factory
from django.http import StreamingHttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from hueb.apps.hueb20.models import DdcGerman
from hueb.apps.hueb20.models.document import Document, DocumentRelationship
from hueb.apps.hueb20.models.language import Language
from hueb.apps.hueb20.models.utils import timerange_serialization

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TypeCheckboxWidget(forms.widgets.CheckboxSelectMultiple):
    template_name = "hueb20/search/widgets/checkbox.html"


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
        choices=(
            ("HUEB20", _("HUEB20")),
            ("LATEIN", _("HUEBLATEIN")),
            ("LEGACY", _("HUEBLEGACY")),
            ("LIDOS", _("HUEBLIDOS")),
        ),
        widget=SearchSelectWidget,
    )


class BaseSearchFormSet(BaseFormSet):
    base_queryset = (
        DocumentRelationship.objects.prefetch_related("document_to__written_by")
        .prefetch_related("document_to__contribution_set__person")
        .select_related("document_to__ddc")
        .select_related("document_to__language")
        .prefetch_related("document_from__written_by")
        .prefetch_related("document_from__contribution_set__person")
        .select_related("document_from__ddc")
        .select_related("document_from__language")
    )

    def get_query_object(
        self,
        types=[Document.ORIGINAL, Document.TRANSLATION, Document.BRIDGE],
        online_only=False,
    ):
        with beeline.tracer(name="building_search_query"):

            include_q_objects = Q()
            exclude_q_objects = Q()

            logger.debug(self.cleaned_data)
            logger.debug(self.cleaned_data)
            beeline.add_context_field("form_data", self.cleaned_data)

            for form in self:
                q = DocumentRelationship.get_q_object(form.cleaned_data, types)
                operator = form.cleaned_data["operator"]

                if operator == "and":
                    include_q_objects &= q
                elif operator == "or":
                    include_q_objects |= q
                elif operator == "not":
                    exclude_q_objects |= q

            logger.debug(include_q_objects)
            logger.debug(exclude_q_objects)
            beeline.add_context_field("include_q_objects", include_q_objects)
            beeline.add_context_field("exclude_q_objects", exclude_q_objects)
            # print("\nINCLUDE: ", include_q_objects)
            # print("\nEXCLUDE: ", exclude_q_objects)
            queryset = self.base_queryset.filter(include_q_objects).exclude(
                exclude_q_objects
            )

            if online_only:
                queryset = queryset.filter(
                    document_to__filing__archive__name="Online-Version"
                )
            logger.debug(queryset.query)
            return queryset

    def get_title_queries(self):
        search_texts = []
        for form in self:
            data = form.cleaned_data
            if data["attribute"] == "title" and data["search_text"]:
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

    online_only = forms.MultipleChoiceField(  # Easier than making booleanfield and adding custom widget for label
        required=False,
        widget=TypeCheckboxWidget(
            attrs={
                "style": "width:20px; height:20px;",
            }
        ),
        choices=((True, _("Online accessible documents only")),),
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
            queryset = formset.get_query_object(types, online_only)

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
                return (
                    BaseSearchFormSet.base_queryset.all()
                    .order_by(F("document_from__id").asc(nulls_last=True))
                    .distinct()
                )

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)

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
        queryset.select_related("document_from__cultural_circle").select_related(
            "document_to__cultural_circle"
        )
        queryset.prefetch_related(
            "document_from__filing_set__archive"
        ).prefetch_related("document_to__filing_set__archive")

        # Fetch original attributes in case of bridge
        queryset.prefetch_related(
            "document_from__document_from__contribution_set__person"
        )
        queryset.select_related("document_from__document_from__language")

        def row_generator(queryset):
            yield [
                "Title of the translation",
                "Subtitle",
                "Intermediary Translation",
                "Edition",
                "Translator",
                "Year",
                "Publisher",
                "Place of publication",
                "Locations",
                "Link",
                "Language",
                "Language of the original",
                "DDC",
                "Culture circle",
                "Title of the original",
                "Subtitle_org",
                "Author",
                "Edition",
                "Year",
                "Publisher",
                "Place of publication",
                "Locations",
                "Link",
            ]

            for i, docs in enumerate(queryset.all()):
                if not docs.document_from:
                    continue
                if not docs.document_to:
                    continue

                doc_to = [
                    # title
                    title if (title := docs.document_to.title) != "" else "-",  # title
                    # subtitle
                    subtitle
                    if (subtitle := docs.document_to.subtitle) != ""
                    else "-",  # subtitle
                    # Intermediary Translation
                    str(bool(docs.document_to.translations.exists())),
                    # Edition
                    edition
                    if (edition := docs.document_to.edition) != ""
                    else "-",  # edition
                    # translator
                    ", ".join(authors.values_list("person__name", flat=True))
                    if (authors := docs.document_to.get_authors()).exists()
                    else "-",
                    # year
                    year
                    if not (year := docs.document_to.serialize_written_in()) is None
                    else "-",
                    # publisher
                    ", ".join(pubs.values_list("person__name", flat=True))
                    if (pubs := docs.document_to.get_publishers()).exists()
                    else "-",
                    # place of publication
                    location
                    if (location := docs.document_to.published_location) != ""
                    else "-",
                    # Location (ARCHIVES)
                    ", ".join(
                        filings.filter(archive__name__isnull=False).values_list(
                            "archive__name", flat=True
                        )
                    )
                    if (filings := docs.document_to.get_filings()).exists()
                    else "-",
                    # Link
                    archives.first().link
                    if (
                        archives := docs.document_to.filing_set.filter(
                            archive__name="Online-Version"
                        )
                    ).exists()
                    else "-",
                    # language generally
                    language
                    if (language := docs.document_to.get_language()) != ""
                    else "-",
                    # language of original
                    lang
                    if (lang := docs.document_from.get_original_language()) != ""
                    else "-",  # ORIGINAL!
                    # ddc
                    ddc if (ddc := docs.document_to.ddc) != "" else "-",
                    # cultural circle
                    circle
                    if (circle := docs.document_to.cultural_circle) != ""
                    else "-",
                ]

                if not docs.document_from.originals.exists():
                    doc_from = [
                        title
                        if (title := docs.document_from.title) != ""
                        else "-",  # title
                        # Subtitle orig
                        subtitle
                        if (subtitle := docs.document_from.subtitle) != ""
                        else "-",  # subtitle
                        # authors
                        ", ".join(authors.values_list("person__name", flat=True))
                        if (authors := docs.document_from.get_authors()).exists()
                        else "-",
                        # edition
                        edition
                        if (edition := docs.document_from.edition) != ""
                        else "-",
                        # year
                        year
                        if not (year := docs.document_from.serialize_written_in())
                        is None
                        else "-",
                        # publisher
                        ", ".join(pubs.values_list("person__name", flat=True))
                        if (pubs := docs.document_from.get_publishers()).exists()
                        else "-",
                        # published location
                        location
                        if (location := docs.document_from.published_location) != ""
                        else "-",
                        # Location (ARCHIVES)
                        ", ".join(
                            filings.filter(archive__name__isnull=False).values_list(
                                "archive__name", flat=True
                            )
                        )
                        if (filings := docs.document_from.get_filings()).exists()
                        else "-",
                        # Link
                        archives.first().link
                        if (
                            archives := docs.document_from.filing_set.filter(
                                archive__name="Online-Version"
                            )
                        ).exists()
                        else "-",
                    ]

                else:

                    doc_from = [
                        # title orig
                        ", ".join(titles)
                        if (
                            titles := docs.document_from.originals.values_list(
                                "title", flat=True
                            )
                        )
                        else "-",
                        # Subtitle orig
                        ", ".join(subtitles)
                        if (
                            subtitles := docs.document_from.originals.values_list(
                                "subtitle", flat=True
                            )
                        )
                        != ""
                        else "-",
                        # authors
                        ", ".join(authors.values_list("person__name", flat=True))
                        if (
                            authors := docs.document_from.originals.first().get_authors()
                        ).exists()
                        else "-",
                        # edition
                        edition
                        if (edition := docs.document_from.originals.first().edition)
                        != ""
                        else "-",  # edition
                        # year
                        timerange_serialization(year)
                        if not (year := docs.document_from.originals.first().written_in)
                        is None
                        else "-",
                        # publisher
                        ", ".join(pubs.values_list("person__name", flat=True))
                        if (
                            pubs := docs.document_from.originals.first().get_publishers()
                        ).exists()
                        else "-",
                        # published location
                        location
                        if (
                            location := docs.document_from.originals.first().published_location
                        )
                        != ""
                        else "-",
                        # Location (ARCHIVES)
                        ", ".join(
                            filings.filter(archive__name__isnull=False).values_list(
                                "archive__name", flat=True
                            )
                        )
                        if (
                            filings := docs.document_from.originals.first().get_filings()
                        ).exists()
                        else "-",
                        # Link
                        archives.first().link
                        if (
                            archives := docs.document_from.originals.first().filing_set.filter(
                                archive__name="Online-Version"
                            )
                        ).exists()
                        else "-",
                    ]

                yield doc_to + doc_from

        class Echo:
            """An object that implements just the write method of the file-like
            interface.
            """

            def write(self, value):
                """Write the value by returning it, instead of storing in a buffer."""
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
