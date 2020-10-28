from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    template_name = "hueb20/index.html"
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overlayOpen"] = True
        return context


class Logout(LogoutView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
