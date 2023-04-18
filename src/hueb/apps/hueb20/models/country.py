import hueb.apps.hueb_legacy_latein.models as Legacy
from django.db import models
from django.urls import reverse
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from hueb.apps.tenants.models import TENANT_APPS, TenantAwareModel


class Country(Reviewable, TenantAwareModel):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255, help_text="Name of the country")
    app = models.CharField(
        max_length=6, choices=HUEB_APPLICATIONS + TENANT_APPS, default=HUEB20
    )
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

    def linked_name(self):
        url = reverse(
            "admin:hueb20_country_change",
            args=[self.id],
        )
        link = '<a href="%s">Country: %s</a>' % (url, str(self))
        return link
