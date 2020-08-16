from django.test import TestCase
from hueb.apps.hueb20.models import Person


class IsAliasTestCase(TestCase):
    def setUp(self):
        self.person_1 = Person()
        self.person_1.save()
        self.person_2 = Person()
        self.person_2.save()

    def test_no_alias(self):
        self.assertFalse(self.person_1.is_alias)
        self.assertFalse(self.person_2.is_alias)

    def test_alias(self):
        self.person_1.alias = self.person_2
        self.person_1.save()
        self.assertTrue(self.person_1.is_alias)
        self.assertFalse(self.person_2.is_alias)
