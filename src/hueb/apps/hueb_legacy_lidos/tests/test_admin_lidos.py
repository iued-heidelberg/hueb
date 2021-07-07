import pytest
from django.urls import reverse
from hueb.apps.hueb_legacy_lidos.models import (
    Author,
    DdcGerman,
    Filter,
    Language,
    LidosEx,
    ManualKeys,
    OrigAssign,
    Original,
    Translation,
    Translator,
)

admin_sites = [
    Author,
    DdcGerman,
    Filter,
    Language,
    LidosEx,
    ManualKeys,
    OrigAssign,
    Original,
    Translation,
    Translator,
]


@pytest.mark.slow
@pytest.mark.django_db
@pytest.mark.parametrize("site", admin_sites)
def test_smoke_admin_search(admin_client, site):
    info = (site._meta.app_label, site._meta.model_name)
    admin_url = reverse("admin:%s_%s_changelist" % info)
    response = admin_client.get(admin_url)
    assert response.status_code == 200

    search_url = admin_url + "?q=test"
    response = admin_client.get(search_url)
    assert response.status_code == 200

    instance = site()
    instance.save()
    instance_url = reverse("admin:%s_%s_change" % info, args=(instance.pk,))
    response = admin_client.get(instance_url)
    assert response.status_code == 200
