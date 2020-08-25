import hueb.apps.hueb_legacy_latein.models as Legacy
from django.db import models
from hueb.apps.hueb20.models import HUEB20, HUEB_APPLICATIONS


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255, help_text="Name of the country")
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    country_ref = models.OneToOneField(
        Legacy.Country,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="country_ref",
    )

    def __str__(self):
        if self.country is None:
            return " "
        return self.country
