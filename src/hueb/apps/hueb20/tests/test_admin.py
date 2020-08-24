from django.contrib.auth.models import User as DjangoUser
from django.test import Client, TestCase
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


class AdminSmokeTestCase(TestCase):
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

    def setUp(self):
        self.client = Client()
        user = DjangoUser.objects.create_superuser(username="test", password="test",)
        self.client.force_login(user)

    def test_smoke_admin(self):
        for obj in self.admin_sites:
            instance = obj()
            instance.save()

            info = (instance._meta.app_label, instance._meta.model_name)
            admin_url = reverse("admin:%s_%s_change" % info, args=(instance.pk,))

            response = self.client.get(admin_url)
            self.assertEqual(response.status_code, 200)
