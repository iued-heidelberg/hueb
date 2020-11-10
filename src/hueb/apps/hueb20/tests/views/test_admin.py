import pytest
from django.urls import reverse
from hueb.apps.hueb20.models.archive import Archive
from hueb.apps.hueb20.models.comment import Comment
from hueb.apps.hueb20.models.country import Country
from hueb.apps.hueb20.models.culturalCircle import CulturalCircle
from hueb.apps.hueb20.models.ddc import DdcGerman
from hueb.apps.hueb20.models.document import Document
from hueb.apps.hueb20.models.filing import Filing
from hueb.apps.hueb20.models.language import Language
from hueb.apps.hueb20.models.person import Person

admin_sites = [
    Filing,
    Country,
    DdcGerman,
    Document,
    Language,
    Archive,
    Person,
    Comment,
    CulturalCircle,
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
