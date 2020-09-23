from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="Index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login", auth_views.LoginView.as_view(template_name="hueb20/index.html")),
]
