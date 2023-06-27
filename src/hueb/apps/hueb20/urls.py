from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog
from hueb import settings
from hueb.apps.hueb20.views.authentication import Login, Logout
from hueb.apps.hueb20.views.documentDetailView import DocumentDetailView
from hueb.apps.hueb20.views.help_guide import HelpGuide
from hueb.apps.hueb20.views.index import IndexView
from hueb.apps.hueb20.views.personDetailView import PersonDetailView
from hueb.apps.hueb20.views.publications import Publications
from hueb.apps.hueb20.views.search import Search
from hueb.apps.tenants.admin_site import admin_site

admin_site._registry.update(admin.site._registry)

urlpatterns = [
    # ex: /polls/
    path("admin/", admin_site.urls),
    # path("padmin/", include("publication.urls")),#conflict change the path
    path("", IndexView.as_view(), name="Index"),
    path("search", Search.as_view(), name="search"),
    path("publications", Publications.as_view(), name="publications"),
    path("help_guide", HelpGuide.as_view(), name="help_guide"),
    path("publications<sub>", Publications.as_view(), name="publicationsSub"),
    path("accounts/login", Login.as_view(), name="login"),
    path("accounts/logout", Logout.as_view(), name="logout"),
    path("document/<int:pk>/", DocumentDetailView.as_view(), name="documentDetailView"),
    path("person/<int:pk>/", PersonDetailView.as_view(), name="personDetailView"),
    # path("subscribe", Publications.set_subscription, name="sub"),
    path(
        "document/<int:pk>/export_csv", DocumentDetailView.download_csv, name="docCsv"
    ),
    path(
        "document/<int:pk>/export_bib", DocumentDetailView.download_bib, name="docBib"
    ),
    path("publications/<int:pk>/", Publications.download_pdf, name="pubPdf"),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    url(r"^i18n/", include("django.conf.urls.i18n")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [re_path(r"^rosetta/", include("rosetta.urls"))]
