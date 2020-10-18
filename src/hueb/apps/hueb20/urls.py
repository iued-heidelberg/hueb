from django.urls import path
from hueb.apps.hueb20.views.authentication import Login, Logout
from hueb.apps.hueb20.views.index import IndexView
from hueb.apps.hueb20.views.search import search

urlpatterns = [
    # ex: /polls/
    path("", IndexView.as_view(), name="Index"),
    path("search", search, name="Search"),
    path("accounts/login", Login.as_view(), name="login"),
    path("accounts/logout", Logout.as_view(), name="logout"),
]
