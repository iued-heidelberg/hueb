from django.shortcuts import render
from hueb.apps.hueb20.views.authentication import CustomAuthForm


def index(request):
    context = {}
    context["form"] = CustomAuthForm(initial={"username": "", "password": ""})

    return render(request, "hueb20/index.html", context)
