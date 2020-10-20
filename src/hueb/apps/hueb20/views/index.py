from django.views.generic import TemplateView
from hueb.apps.hueb20.views.authentication import CustomAuthForm


class IndexView(TemplateView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CustomAuthForm(initial={"username": "", "password": ""})
        return context
