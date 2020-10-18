from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from hueb.apps.hueb20.views.authentication import CustomAuthForm


def index(request):
    context = {}
    context["form"] = CustomAuthForm(initial={"username": "", "password": ""})

    return render(request, "hueb20/index.html", context)


@login_required
def search(request):
    return render(request, "hueb20/search.html")
