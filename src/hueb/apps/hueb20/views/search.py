from django import forms
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, View
from hueb.apps.hueb20.models.document import Document


class SearchSelectWidget(forms.widgets.Select):
    template_name = "hueb20/search/widgets/select.html"


class SearchForm(forms.Form):
    logical_choices = (("and", "And"), ("or", "Or"), ("not", "Not"))
    attribute_choices = (
        ("title", "Title"),
        ("author", "Author"),
        ("ddc", "DDC"),
        ("year", "Year"),
    )

    logical = forms.ChoiceField(choices=logical_choices, widget=SearchSelectWidget)
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


class ComplexSearch(View):
    template_name = "hueb20/search/search_complex.html"
    form_class = SearchForm

    def get(self, request, *args, **kwargs):

        form = SearchForm(data=request.GET)
        if not form.is_valid():
            form = SearchForm()

        context = {"form": form}

        return render(request, "hueb20/search/search_complex.html", context)


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
