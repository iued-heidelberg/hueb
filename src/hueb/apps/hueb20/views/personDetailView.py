from django.views.generic.detail import DetailView
from hueb.apps.hueb20.models import Person


class PersonDetailView(DetailView):
    # specify the model to use
    model = Person
    template_name = "hueb20/person_details/person_detail_view.html"
