from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language


def menu(request):
    menu = []

    menu.append({"name": _("Projekt"), "link": "/", "disabled": False})

    menu.append(
        {
            "name": _("Suche"),
            "link": "/" + get_language() + "/search",
            "disabled": False,
        }
    )

    menu.append(
        {
            "name": _("Publikationen"),
            "link": "/" + get_language() + "/publications",
            "disabled": False,
        }
    )

    context = {}
    context["menu"] = menu

    return context


def overlay(request, context={}):
    context = {}
    context["overlayOpen"] = False

    return context
