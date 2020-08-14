import inspect

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from hueb.apps.hueb20 import models


class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_superuser(username="test", password="test",)
        self.client.force_login(user)

    def test_smoke_admin(self):
        for name, obj in inspect.getmembers(models):
            if inspect.isclass(obj):
                if obj.__module__ == models.__name__:
                    instance = obj()
                    instance.save()
                    info = (instance._meta.app_label, instance._meta.model_name)
                    admin_url = reverse(
                        "admin:%s_%s_change" % info, args=(instance.pk,)
                    )

                    response = self.client.get(admin_url)
                    self.assertEqual(response.status_code, 200)
