from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from hueb.apps.tenants.models import Tenant, TENANT_APPS


def menu(request):
    menu = []

    host = request.get_host()
    default_host = ("." + host).split(".")[-1]
    tenants = Tenant.objects.all()
    absolute_uri = request.build_absolute_uri()
    name_and_link = [
        {
            "name": tenant.get_verbose_name(),
            "link": absolute_uri.replace(
                host, tenant.subdomain_prefix + "." + default_host
            ),
        }
        for tenant in tenants
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
