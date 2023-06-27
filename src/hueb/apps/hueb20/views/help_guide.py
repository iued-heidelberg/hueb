# flake8: noqa
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _
from hueb.apps.tenants.utils import tenantname_from_request


class HelpGuide(LoginView):
    template_name = "hueb20/help_guide/help_guide.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overlayOpen"] = False

        context["tenant"] = tenantname_from_request(self.request)
        return context
