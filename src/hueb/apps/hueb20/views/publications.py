from django.views.generic import ListView
from hueb.apps.publications.models import Publication


class Publications(ListView):

    # specify the model to use
    template_name = "hueb20/publications/publications.html"
    model = Publication
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent"] = (
            Publication.objects.all().order_by("-publication_date").first()
        )
        return context

    def get_queryset(self):
        return Publication.objects.all().order_by("-publication_date").all()
