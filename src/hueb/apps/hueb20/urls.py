from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from hueb import settings
from hueb.apps.hueb20.views.authentication import Login, Logout
from hueb.apps.hueb20.views.index import IndexView
from hueb.apps.hueb20.views.search import Search
from hueb.apps.hueb20.views.documentDetailView import DocumentDetailView

urlpatterns = [
    # ex: /polls/
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="Index"),
    path("search", Search.as_view(), name="search"),
    path("accounts/login", Login.as_view(), name="login"),
    path("accounts/logout", Logout.as_view(), name="logout"),
    path("document/<int:pk>/", DocumentDetailView.as_view(), name="documentDetailView"),
    path(
        "document/<int:pk>/export_csv", DocumentDetailView.download_csv, name="docCsv"
    ),
    path(
        "document/<int:pk>/export_bib", DocumentDetailView.download_bib, name="docBib"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
