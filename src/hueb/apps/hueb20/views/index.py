from django.contrib.auth.views import LoginView
from hueb.apps.tenants.utils import tenantname_from_request


class IndexView(LoginView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overlayOpen"] = False

        context["tenant"] = tenantname_from_request(self.request)
        return context
