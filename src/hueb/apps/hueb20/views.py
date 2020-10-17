from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.widgets import PasswordInput, TextInput
from django.shortcuts import render


def get_common_context(request, context={}):

    context["overlayOpen"] = False

    return context


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        initial="",
        widget=TextInput(attrs={"class": "validate", "placeholder": "Benutzername"}),
    )
    password = forms.CharField(
        initial="", widget=PasswordInput(attrs={"placeholder": "Passwort"})
    )


def index(request):
    context = get_common_context(request)
    context["form"] = CustomAuthForm(initial={"username": "", "password": ""})

    return render(request, "hueb20/index.html", context)


@login_required
def search(request):
    context = get_common_context(request)

    return render(request, "hueb20/search.html", context)


class Login(LoginView):
    template_name = "hueb20/index.html"
    redirect_authenticated_user = True
    authentication_form = CustomAuthForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_common_context(self.request, context)
        context["overlayOpen"] = True
        return context


class Logout(LogoutView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_common_context(self.request, context)
        return context
