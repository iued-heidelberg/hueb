from django.urls import path

from . import views
from .views import Login

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="Index"),
    path("accounts/login", Login.as_view(), name="login"),
]
