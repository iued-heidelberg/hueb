"""hueb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


import debug_toolbar
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url, include

urlpatterns = [
    # path("", include("hueb.apps.hueb20.urls")),
    url(r"^i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include("hueb.apps.hueb20.urls")),  # , name="Index"),
)
