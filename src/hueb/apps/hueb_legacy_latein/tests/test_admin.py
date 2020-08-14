from django.contrib.auth.models import User as DjangoUser
from django.test import Client, TestCase
from django.urls import reverse

from hueb.apps.hueb_legacy_latein.models import (  # OriginalAuthorNew,; OriginalNewAuthor,; TranslationNewTranslator,; TranslationTranslatorNew,
    Author,
    AuthorNew,
    Country,
    DdcGerman,
    Language,
    LocAssign,
    Location,
    LocationNew,
    OrigAssign,
    Original,
    OriginalNew,
    Translation,
    TranslationNew,
    Translator,
    TranslatorNew,
    User,
)


class AdminSmokeTestCase(TestCase):
    admin_sites = [
        Author,
        AuthorNew,
        Country,
        DdcGerman,
        Language,
        LocAssign,
        Location,
        LocationNew,
        OrigAssign,
        Original,
        OriginalNew,
        Translation,
        TranslationNew,
        Translator,
        TranslatorNew,
        User,
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