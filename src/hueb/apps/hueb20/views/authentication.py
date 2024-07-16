from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import resolve_url
from django.conf import settings


class Login(LoginView):
    template_name = "hueb20/index.html"
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overlayOpen"] = True
        return context

    def get_success_url(self):
        # check if user has staff status
        if self.request.user.is_staff:
            return super().get_success_url()
        else:
            # redirect to index page
            return resolve_url("Index")


class Logout(LogoutView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
