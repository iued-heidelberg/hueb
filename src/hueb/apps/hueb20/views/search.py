from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms.formsets import BaseFormSet, formset_factory
from django.views.generic import ListView
from hueb.apps.hueb20.models.document import Document


class SearchSelectWidget(forms.widgets.Select):
    template_name = "hueb20/search/widgets/select.html"


class SearchForm(forms.Form):
    operator_choices = (("and", "And"), ("or", "Or"), ("not", "Not"))
    attribute_choices = (
        ("title", "Title"),
        ("author", "Author"),
        ("ddc", "DDC"),
        ("year", "Year"),
    )

    operator = forms.ChoiceField(choices=operator_choices, widget=SearchSelectWidget)
    attribute = forms.ChoiceField(choices=attribute_choices, widget=SearchSelectWidget)
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
                "placeholder": "Suchbegriff",
            }
        ),
    )
    search_year = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "flex p-2 mx-2 my-2 font-medium placeholder-black placeholder-opacity-25 bg-transparent border-b-4 border-black rounded-none appearance-none lg:placeholder-opacity-25 lg:border-sand-bg lg:placeholder-sand-bg",
            }
        ),
    )

    def get_q_object(self):
        search_text = self.cleaned_data["search_text"]
        if self.cleaned_data["attribute"] == "title":
            return Document.q_object_by_title(search_text)


class BaseSearchFormSet(BaseFormSet):
    def get_query_object(self):
        include_q_objects = Q()
        exclude_q_objects = Q()

        for form in self:

            q = form.get_q_object()
            operator = form.cleaned_data["operator"]

            if operator == "and":
                include_q_objects &= q
            elif operator == "or":
                include_q_objects |= q
            elif operator == "not":
                exclude_q_objects |= q

        print(include_q_objects)
        print(exclude_q_objects)

        print(
            Document.objects.filter(include_q_objects)
            .exclude(exclude_q_objects)
            .count()
        )

        return Document.objects.filter(include_q_objects).exclude(exclude_q_objects)


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
            return formset.get_query_object().all().order_by("id")
        except ValidationError:
            results = Document.objects.all().order_by("id")
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
