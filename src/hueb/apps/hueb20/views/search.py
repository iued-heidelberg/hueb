from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from hueb.apps.hueb20.models.document import Document


@login_required
def search(request):
    return render(request, "hueb20/search/search.html")


class Search(ListView):
    model = Document
    template_name = "hueb20/search/search.html"
    paginate_by = 10

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
            )
        return result

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "")
        return context
