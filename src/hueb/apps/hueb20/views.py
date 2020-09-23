from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


def get_common_context(context={}):
    menu = []
    menu.append({"name": "Projekt", "link": "#", "disabled": False})
    menu.append({"name": "Katalog", "link": "#", "disabled": True})
    menu.append({"name": "Suche", "link": "#", "disabled": True})
    context["menu"] = menu

    context["overlayOpen"] = False

    return context


def index(request):

    context = get_common_context()
    context["form"] = AuthenticationForm(initial={"username": "", "password": ""})

    return render(request, "hueb20/index.html", context)
