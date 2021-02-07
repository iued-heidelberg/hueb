from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from simple_history.models import HistoricalRecords


class CulturalCircle(Reviewable):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Name of the cultural circle")
    start = IntegerRangeField(null=True, blank=True)
    end = IntegerRangeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    history = HistoricalRecords()

    def __str__(self):
        if self.name is None:
            return " "
        return self.name
