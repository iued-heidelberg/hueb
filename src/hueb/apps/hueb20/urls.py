from django.urls import path

from . import views
from .views import Login, Logout

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="Index"),
    path("search", views.search, name="Search"),
    path("accounts/login", Login.as_view(), name="login"),
    path("accounts/logout", Logout.as_view(), name="logout"),
]
