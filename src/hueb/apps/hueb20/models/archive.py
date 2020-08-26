import hueb.apps.hueb_legacy_latein.models as Legacy
from django.db import models
from hueb.apps.hueb20.models import HUEB20, HUEB_APPLICATIONS
from simple_history.models import HistoricalRecords

from .country import Country


class Archive(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    location_ref = models.OneToOneField(
        Legacy.LocationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        if self.name is None:
            return " "
        return self.name
