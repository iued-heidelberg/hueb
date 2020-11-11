from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from hueb import settings
from hueb.apps.hueb20.views.authentication import Login, Logout
from hueb.apps.hueb20.views.index import IndexView
from hueb.apps.hueb20.views.search import Search

urlpatterns = [
    # ex: /polls/
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="Index"),
    path("search", Search.as_view(), name="search"),
    path("accounts/login", Login.as_view(), name="login"),
    path("accounts/logout", Logout.as_view(), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

try:
    if settings.DEBUG:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
except AttributeError:
    pass
