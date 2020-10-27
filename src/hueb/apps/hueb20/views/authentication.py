from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "validate",
                "placeholder": "Benutzername",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        strip=False,
        widget=PasswordInput(
            attrs={"placeholder": "Passwort", "autocomplete": "current-password"}
        ),
    )


class Login(LoginView):
    template_name = "hueb20/index.html"
    redirect_authenticated_user = True
    authentication_form = CustomAuthForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overlayOpen"] = True
        return context


class Logout(LogoutView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
