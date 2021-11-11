from django.views.generic.detail import DetailView
from django import forms
from hueb.apps.hueb20.models import Person
from hueb.apps.hueb20.models import Document
from django.http import HttpResponse
import csv


class PersonDetailView(DetailView):
    # specify the model to use
    model = Person
    template_name = "hueb20/person_details/person_detail_view.html"
