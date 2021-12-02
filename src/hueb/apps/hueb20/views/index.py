from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.utils.translation import gettext as _


class IndexView(LoginView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overlayOpen"] = False
        return context
