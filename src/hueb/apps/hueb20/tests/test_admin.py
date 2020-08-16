from django.contrib.auth.models import User as DjangoUser
from django.test import Client, TestCase
from django.urls import reverse

from hueb.apps.hueb20.models import (  # OriginalAuthorNew,; OriginalNewAuthor,; TranslationNewTranslator,; TranslationTranslatorNew,
    Archive,
    Country,
    DdcGerman,
    Document,
    Language,
    Location,
    Person,
)


class AdminSmokeTestCase(TestCase):
    admin_sites = [
        Archive,
        Country,
        DdcGerman,
        Document,
        Language,
        Location,
        Person,
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
