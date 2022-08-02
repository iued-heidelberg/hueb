import logging
import beeline
from django import forms
from django.db.models import Q
from django.forms.formsets import BaseFormSet, formset_factory
from django.views.generic import ListView
from hueb.apps.hueb20.models.document import Document, DocumentRelationship
from hueb.apps.hueb20.models.language import Language
from hueb.apps.hueb20.models import DdcGerman
from django.db.models import F
from django.utils.translation import get_language_info
from django.utils.translation import gettext_lazy as _
import textwrap


# Get an instance of a logger
logger = logging.getLogger(__name__)


class TypeCheckboxWidget(forms.widgets.CheckboxSelectMultiple):
    template_name = "hueb20/search/widgets/checkbox.html"


class SearchSelectWidget(forms.widgets.Select):
    template_name = "hueb20/search/widgets/select.html"


class SearchChoiceWidget(forms.widgets.Select):
    template_name = "hueb20/search/widgets/choice_option.html"
    # option_template_name = 'hueb20/search/widgets/choice_option.html'


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
    search_ddc_new = forms.ChoiceField(

        choices=tuple(
            (ddc, textwrap.fill(ddc.ddc_number, width=10, initial_indent='', subsequent_indent='',
                                expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False,
                                break_long_words=True, drop_whitespace=True, break_on_hyphens=True,
                                tabsize=4, placeholder=' [...]'))
            for ddc in DdcGerman.objects.filter()
            .all()
            .order_by("ddc_number")
        ),
        widget=SearchChoiceWidget,
    )
    """
    search_ddc_new = forms.ChoiceField(
        choices=tuple(
            (
                DdcGerman.objects.get(ddc_number=str(i).zfill(3)).ddc_name,
                tuple(
                    (
                        DdcGerman.objects.get(ddc_number=str(number).zfill(3)),
                        str(number).zfill(3),
                    )
                    for number in range(i, i + 10)
                ),
            )
            for i in range(0, len(DdcGerman.objects.all()), 10)
        ),
        widget=SearchSelectWidget,
    )

    search_language = forms.ChoiceField(
        choices=tuple(
            (language, language)
            for language in Language.objects.filter()
            .exclude(language_de="")  # manual coding, but couldn't find another way
            .exclude(language_en="")
            .all()
            .order_by("language_de")
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
        .select_related("document_to__ddc")
        .select_related("document_to__language")
        .prefetch_related("document_from__written_by")
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
            if data["attribute"] == "title":
                if data["operator"] == "and" or data["operator"] == "or":
                    search_texts.append(data["search_text"])
        return search_texts


class SortForm(forms.Form):
    sort_attribute = forms.ChoiceField(
        choices=Document.sortable_attributes, widget=SearchSelectWidget
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
        # sortform = self.sort_form(data=self.request.GET)
        sortform = SortForm(data=self.request.GET)
        # typeform = self.type_form(data=self.request.GET)
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
            context["title_queries"] = ""

        return context
