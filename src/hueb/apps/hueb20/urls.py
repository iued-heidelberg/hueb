from django.urls import path
from hueb.apps.hueb20.views.authentication import Login, Logout
from hueb.apps.hueb20.views.index import index, search

urlpatterns = [
    # ex: /polls/
    path("", index, name="Index"),
    path("search", search, name="Search"),
    path("accounts/login", Login.as_view(), name="login"),
    path("accounts/logout", Logout.as_view(), name="logout"),
]
