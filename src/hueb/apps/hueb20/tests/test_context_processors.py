from django.contrib.auth.models import AnonymousUser
from hueb.apps.hueb20.context_processors import menu


def test_unauthenticated_user(rf):
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

    assert context["menu"][2]["name"] == "Katalog"
    assert context["menu"][2]["link"] == "#"
    assert context["menu"][2]["disabled"] == True


def test_authenticated_user(rf, django_user_model):
    username = "Test"
    password = "Test"
    user = django_user_model.objects.create_user(username=username, password=password)

    request = rf.get("/")
    request.user = user
    context = menu(request)
    assert "menu" in context

    assert context["menu"][0]["name"] == "Projekt"
    assert context["menu"][0]["link"] == "/"
    assert context["menu"][0]["disabled"] == False

    assert context["menu"][1]["name"] == "Suche"
    assert context["menu"][1]["link"] == "/search"
    assert context["menu"][1]["disabled"] == False

    assert context["menu"][2]["name"] == "Katalog"
    assert context["menu"][2]["link"] == "#"
    assert context["menu"][2]["disabled"] == True
