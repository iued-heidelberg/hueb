import logging

import beeline
from django import forms
from django.db.models import Q
from django.forms.formsets import BaseFormSet, formset_factory
from django.views.generic import ListView
from hueb.apps.hueb20.models.document import Document, DocumentRelationship
from django.db.models import F

# Get an instance of a logger
logger = logging.getLogger(__name__)


class SearchSelectWidget(forms.widgets.Select):
    template_name = "hueb20/search/widgets/select.html"


class SearchForm(forms.Form):
    operator_choices = (("and", "And"), ("or", "Or"), ("not", "Not"))

    operator = forms.ChoiceField(choices=operator_choices, widget=SearchSelectWidget)
    attribute = forms.ChoiceField(
        choices=Document.searchable_attributes, widget=SearchSelectWidget
    )
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": "Suchbegriff",
            }
        ),
    )
    search_year_from = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": "von",
            }
        ),
    )
    search_year_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": "bis",
            }
        ),
    )
    search_ddc = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": "DDC Nummer",
            }
        ),
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

    def get_query_object(self):
        with beeline.tracer(name="building_search_query"):

            include_q_objects = Q()
            exclude_q_objects = Q()

            logger.debug(self.cleaned_data)
            logger.debug(self.cleaned_data)
            beeline.add_context_field("form_data", self.cleaned_data)

            for form in self:

                q = DocumentRelationship.get_q_object(form.cleaned_data)
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

            queryset = self.base_queryset.filter(include_q_objects).exclude(
                exclude_q_objects
            )

            logger.debug(queryset.query)
            return queryset


class SortForm(forms.Form):
    sort_attribute = forms.ChoiceField(
        choices=Document.sortable_attributes, widget=SearchSelectWidget
    )
    sort_direction = forms.ChoiceField(
        choices=(("asc", "Aufsteigend"), ("desc", "Absteigend")),
        widget=SearchSelectWidget,
    )

    def get_order_by(self):
        return self.cleaned_data["sort_direction"], self.cleaned_data["sort_attribute"]


class Search(ListView):
    template_name = "hueb20/search/search.html"
    model = Document
    paginate_by = 20

    sort_form = SortForm

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
        sortform = self.sort_form(data=self.request.GET)

        if formset.is_valid():
            queryset = formset.get_query_object()
            if sortform.is_valid():
                orderBy = sortform.get_order_by()[1]
                orderDir = sortform.get_order_by()[0]
                if orderDir == "asc":
                    return queryset.all().order_by(
                        F("document_from__" + orderBy).asc(nulls_last=True)
                    )
                else:
                    return queryset.all().order_by(
                        F("document_from__" + orderBy).desc(nulls_last=True)
                    )
            else:
                return queryset.all().order_by(
                    F("document_from__id").asc(nulls_last=True)
                )
        else:
            if sortform.is_valid():
                orderBy = sortform.get_order_by()[1]
                orderDir = sortform.get_order_by()[0]
                if orderDir == "asc":
                    return queryset.all().order_by(
                        F("document_from__" + orderBy).asc(nulls_last=True)
                    )
                else:
                    return queryset.all().order_by(
                        F("document_from__" + orderBy).desc(nulls_last=True)
                    )
            else:
                return BaseSearchFormSet.base_queryset.all().order_by(
                    F("document_from__id").asc(nulls_last=True)
                )

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)

        formset = self.SearchFormset(data=self.request.GET)
        if not formset.is_valid():
            formset = self.SearchFormset()

        context["formset"] = formset

        sortform = self.sort_form(data=self.request.GET)
        if not sortform.is_valid():
            sortform = self.sort_form()
        context["sortform"] = sortform

        return context
