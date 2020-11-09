import hueb.apps.hueb_legacy_latein.models as Legacy
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.template.defaultfilters import escape
from hueb.apps.hueb20.models import HUEB20, HUEB_APPLICATIONS
from hueb.apps.hueb20.models.utils import timerange_serialization
from simple_history.models import HistoricalRecords


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    alias = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    lifetime_start = IntegerRangeField(null=True, blank=True)
    lifetime_end = IntegerRangeField(null=True, blank=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    author_ref = models.OneToOneField(
        Legacy.AuthorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translator_ref = models.OneToOneField(
        Legacy.TranslatorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherOriginal_ref = models.OneToOneField(
        Legacy.OriginalNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherTranslation_ref = models.OneToOneField(
        Legacy.TranslationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        if self.name is None:
            return " "
        return escape(self.name)

    @property
    def is_alias(self):
        if self.alias is not None:
            return True
        else:
            return False

    def adapt_person_lifetime_start_list_view(self):
        return timerange_serialization(self.lifetime_start)

    def adapt_person_lifetime_end_list_view(self):
        return timerange_serialization(self.lifetime_end)

    adapt_person_lifetime_end_list_view.short_description = "Lifetime End"
    adapt_person_lifetime_start_list_view.short_description = "Lifetime Start"
