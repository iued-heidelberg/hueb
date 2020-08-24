import hueb.apps.hueb_legacy_latein.models as Legacy
from django.contrib.postgres.fields import IntegerRangeField
from django.core import validators
from django.db import models
from hueb.apps.hueb20.models import HUEB20, HUEB_APPLICATIONS

from .culturalCircle import CulturalCircle
from .person import Person


class YearRange(models.Model):
    id = models.BigAutoField(primary_key=True)
    timerange = IntegerRangeField(null=True, blank=True)
    start = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator(
                r"^[0-9]*$", "Only 0-9 are allowed.", "Invalid Number"
            ),
        ],
    )
    end = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator(
                r"^[0-9]*$", "Only 0-9 are allowed.", "Invalid Number"
            ),
        ],
    )
    parsed_string = models.TextField(blank=True, null=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    lifetime = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="lifetime",
    )
    culturalCircleTimeRange = models.ForeignKey(
        CulturalCircle,
        on_delete=models.CASCADE,
        related_name="culturalCircleTimeRange",
        blank=True,
        null=True,
    )
    author_ref = models.OneToOneField(
        Legacy.AuthorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translator_ref = models.OneToOneField(
        Legacy.TranslatorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        try:
            return str(self.timerange.lower) + " - " + str(self.timerange.upper)
        except Exception:

            return "none"
