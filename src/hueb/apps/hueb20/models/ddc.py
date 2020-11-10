import hueb.apps.hueb_legacy_latein.models as Legacy
from django.db import models
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from simple_history.models import HistoricalRecords


class DdcGerman(models.Model):

    id = models.BigAutoField(primary_key=True)
    ddc_number = models.CharField(max_length=3)
    ddc_name = models.CharField(max_length=255)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    ddc_ref = models.OneToOneField(
        Legacy.DdcGerman, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "DDC"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.ddc_number + " " + self.ddc_name
