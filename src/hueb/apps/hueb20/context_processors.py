from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from hueb.apps.tenants.models import Tenant, TENANT_APPS_TO_PREFIX


def menu(request):
    menu = []

    host = request.get_host()

    has_subdomain = host.split(".")[0] in TENANT_APPS_TO_PREFIX.keys()
    if not has_subdomain:
        default_host = host
    else:
        default_host = host.split(".", 1)[1]

    absolute_uri = request.build_absolute_uri()
    name_and_link = [
        {
            "name": tenant,
            "link": absolute_uri.replace(host, prefix + "." + default_host),
        }
        for tenant, prefix in TENANT_APPS_TO_PREFIX.items()
    ] + [{"name": "HÜB", "link": absolute_uri.replace(host, default_host)}]
    menu.append(
        {"name": _("Projekt"), "link": "/", "disabled": False, "sub": name_and_link}
    )

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
