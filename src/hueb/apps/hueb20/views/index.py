from django.contrib.auth.views import LoginView


class IndexView(LoginView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overlayOpen"] = False
        return context
