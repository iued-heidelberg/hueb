from django.contrib.auth.models import AnonymousUser
from hueb.apps.hueb20.context_processors import menu, overlay
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language


def test_menu_unauthenticated_user(rf):
    request = rf.get("/")
    request.user = AnonymousUser()

    context = menu(request)

    assert "menu" in context

    assert context["menu"][0]["name"] == "Projekt"
    assert context["menu"][0]["link"] == "/"
    assert context["menu"][0]["disabled"] == False

    assert context["menu"][1]["name"] == "Suche"
    assert context["menu"][1]["link"] == "#"
    assert context["menu"][1]["disabled"] == True

    assert context["menu"][2]["name"] == "Publikationen"
    assert context["menu"][2]["link"] == "#"
    assert context["menu"][2]["disabled"] == True


def test_menu_authenticated_user(rf, django_user_model):
    username = "Test"
    password = "Test"
    user = django_user_model.objects.create_user(username=username, password=password)

    request = rf.get("/")
    request.user = user
    context = menu(request)
    assert "menu" in context

    assert context["menu"][0]["name"] == _("Projekt")
    assert context["menu"][0]["link"] == "/"
    assert context["menu"][0]["disabled"] == False

    assert context["menu"][1]["name"] == _("Suche")
    assert context["menu"][1]["link"] == "/" + get_language() + "/search"
    assert context["menu"][1]["disabled"] == False

    assert context["menu"][2]["name"] == _("Publikationen")
    assert context["menu"][2]["link"] == "/" + get_language() + "/publications"
    assert context["menu"][2]["disabled"] == False


def test_overlay(rf):
    request = rf.get("/")
    request.user = AnonymousUser()

    context = overlay(request)

    assert "overlayOpen" in context

    assert context["overlayOpen"] == False
