from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.urls import include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from hueb import settings
from hueb.apps.hueb20.views.authentication import Login, Logout
from hueb.apps.hueb20.views.index import IndexView
from hueb.apps.hueb20.views.search import Search
from hueb.apps.hueb20.views.publications import Publications
from hueb.apps.hueb20.views.documentDetailView import DocumentDetailView
from hueb.apps.hueb20.views.personDetailView import PersonDetailView
from django.views.i18n import JavaScriptCatalog
from django.utils import translation

urlpatterns = [
    # ex: /polls/
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="Index"),
    path("search", Search.as_view(), name="search"),
    path("publications", Publications.as_view(), name="publications"),
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
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    url(r"^i18n/", include("django.conf.urls.i18n")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += i18n_patterns(
#'',
# (_(r'^dual-lang/'), include('duallang.urls')),
# (r'^', include('home.urls')),
# )

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [re_path(r"^rosetta/", include("rosetta.urls"))]
