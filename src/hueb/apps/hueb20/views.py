from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


def index(request):

    menu = []
    menu.append({"name": "Projekt", "link": "#", "disabled": False})
    menu.append({"name": "Katalog", "link": "#", "disabled": True})
    menu.append({"name": "Suche", "link": "#", "disabled": True})

    context = {
        "menu": menu,
        "form": AuthenticationForm(initial={"username": "", "password": ""}),
        "overlayOpen": True,
    }

    return render(request, "hueb20/index.html", context)
