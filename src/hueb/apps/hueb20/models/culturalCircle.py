from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.urls import reverse
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS


class CulturalCircle(Reviewable):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Name of the cultural circle")
    start = IntegerRangeField(null=True, blank=True)
    end = IntegerRangeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)

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
