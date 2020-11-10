import pytest
from django.urls import reverse

from hueb.apps.hueb_legacy_latein.models import (  # OriginalAuthorNew,; OriginalNewAuthor,; TranslationNewTranslator,; TranslationTranslatorNew,
    AuthorNew,
    Country,
    DdcGerman,
    Language,
    LocAssign,
    LocationNew,
    OrigAssign,
    OriginalNew,
    TranslationNew,
    TranslatorNew,
    User,
)


admin_sites = [
    AuthorNew,
    Country,
    DdcGerman,
    Language,
    LocAssign,
    LocationNew,
    OrigAssign,
    OriginalNew,
    TranslationNew,
    TranslatorNew,
    User,
]


@pytest.mark.slow
@pytest.mark.django_db
@pytest.mark.parametrize("site", admin_sites)
def test_smoke_admin(admin_client, site):
    instance = site()
    instance.save()
    info = (site._meta.app_label, site._meta.model_name)
    admin_url = reverse("admin:%s_%s_change" % info, args=(instance.pk,))

    response = admin_client.get(admin_url)
    assert response.status_code == 200


@pytest.mark.slow
@pytest.mark.django_db
@pytest.mark.parametrize("site", admin_sites)
def test_smoke_admin_search(admin_client, site):
    info = (site._meta.app_label, site._meta.model_name)
    admin_url = reverse("admin:%s_%s_changelist" % info)
    print(admin_url)
    search_url = admin_url + "?q=test"
    response = admin_client.get(search_url)
    assert response.status_code == 200
