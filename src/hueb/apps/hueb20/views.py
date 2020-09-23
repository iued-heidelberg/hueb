from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
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


class Login(LoginView):
    template_name = "hueb20/index.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_common_context(context)
        context["overlayOpen"] = True
        return context


class Logout(LogoutView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_common_context(context)
        return context
