import hueb.apps.hueb_legacy_latein.models as Legacy
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.urls import reverse
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from translated_fields import TranslatedField


class CulturalCircle(Reviewable):
    id = models.BigAutoField(primary_key=True)
    name = TranslatedField(
        models.CharField(
            max_length=255, help_text="Name of the cultural circle", null=True
        )
    )
    name_temp = models.CharField(
        max_length=255, help_text="Name of the cultural circle", null=True
    )
    start = IntegerRangeField(null=True, blank=True)
    end = IntegerRangeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    country_ref = models.OneToOneField(
        Legacy.Country,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="cultural_circle_ref",
    )

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    def linked_name(self):
        url = reverse(
            "admin:hueb20_culturalcircle_change",
            args=[self.id],
        )
        link = '<a href="%s">Cultural Circle: %s</a>' % (url, str(self))
        return link
