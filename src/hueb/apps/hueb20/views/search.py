import logging

import beeline
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms.formsets import BaseFormSet, formset_factory
from django.views.generic import ListView
from hueb.apps.hueb20.models.document import Document

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
        Document.objects.prefetch_related("translations__written_by")
        .prefetch_related("translations__ddc")
        .prefetch_related("translations__language")
        .prefetch_related("originals__written_by")
        .prefetch_related("originals__ddc")
        .prefetch_related("originals__language")
        .prefetch_related("written_by")
        .select_related("language")
        .select_related("ddc")
    )

    def get_query_object(self):
        with beeline.tracer(name="building_search_query"):

            include_q_objects = Q()
            exclude_q_objects = Q()

            logger.debug(self.cleaned_data)
            logger.debug(self.cleaned_data)
            beeline.add_context_field("form_data", self.cleaned_data)

            for form in self:

                q = Document.get_q_object(form.cleaned_data)
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


class FormsetSearch(ListView):
    template_name = "hueb20/search/search_complex.html"
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
        try:
            formset.is_valid()
            queryset = formset.get_query_object()

            return queryset.all().order_by("id")
        except ValidationError:
            results = BaseSearchFormSet.base_queryset.all().order_by("id")
            return results

    def get_context_data(self, **kwargs):
        context = super(FormsetSearch, self).get_context_data(**kwargs)

        try:
            formset = self.SearchFormset(data=self.request.GET)
            formset.is_valid()
        except ValidationError:
            formset = self.SearchFormset()

        context["formset"] = formset

        return context


class Search(ListView):
    model = Document
    template_name = "hueb20/search/search.html"
    paginate_by = 20

    def get_queryset(self):
        filter_val = self.request.GET.get("filter")
        if filter_val is not None:
            results = (
                Document.objects.prefetch_related("translations__written_by")
                .prefetch_related("translations__ddc")
                .prefetch_related("translations__language")
                .prefetch_related("originals__written_by")
                .prefetch_related("originals__ddc")
                .prefetch_related("originals__language")
                .prefetch_related("written_by")
                .select_related("language")
                .select_related("ddc")
                .filter(
                    Q(title__icontains=filter_val)
                    | Q(written_by__name__icontains=filter_val)
                    | Q(language__language__icontains=filter_val)
                )
                .order_by("id")
            )
            return results
        else:
            result = (
                Document.objects.prefetch_related("translations__written_by")
                .prefetch_related("translations__ddc")
                .prefetch_related("translations__language")
                .prefetch_related("originals__written_by")
                .prefetch_related("originals__ddc")
                .prefetch_related("originals__language")
                .prefetch_related("written_by")
                .select_related("language")
                .select_related("ddc")
                .all()
                .order_by("id")
            )
        return result

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "")
        return context
