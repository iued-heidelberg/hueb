from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language


def menu(request):
    menu = []

    menu.append({"name": _("Projekt"), "link": "/", "disabled": False})

    if request.user.is_authenticated:
        menu.append(
            {
                "name": _("Suche"),
                "link": "/" + get_language() + "/search",
                "disabled": False,
            }
        )
    else:
        menu.append({"name": _("Suche"), "link": "#", "disabled": True})

    menu.append({"name": _("Katalog"), "link": "#", "disabled": True})

    context = {}
    context["menu"] = menu

    return context


def overlay(request, context={}):
    context = {}
    context["overlayOpen"] = False

    return context
