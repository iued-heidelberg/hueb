import hueb.apps.hueb_legacy.models as LegacyLegacy
import hueb.apps.hueb_legacy_latein.models as Legacy
import hueb.apps.hueb_legacy_lidos.models as Lidos
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.template.defaultfilters import escape
from django.urls import reverse
from hueb.apps.hueb20.models.culturalCircle import CulturalCircle
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import (
    HUEB20,
    HUEB_APPLICATIONS,
    timerange_serialization,
)


class Person(Reviewable):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    cultural_circle = models.ForeignKey(
        CulturalCircle, blank=True, null=True, on_delete=models.DO_NOTHING
    )
    alias = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    organisation = models.BooleanField(default=False, null=False, blank=None)
    lifetime_start = IntegerRangeField(null=True, blank=True)
    lifetime_end = IntegerRangeField(null=True, blank=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    # references to LATEIN
    author_ref = models.OneToOneField(
        Legacy.AuthorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translator_ref = models.OneToOneField(
        Legacy.TranslatorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherOriginal_ref = models.ForeignKey(
        Legacy.OriginalNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherTranslation_ref = models.ForeignKey(
        Legacy.TranslationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    # references to LIDOS
    author_ref_lidos = models.ForeignKey(
        Lidos.Author, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translator_ref_lidos = models.ForeignKey(
        Lidos.Translator, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherOriginal_ref_lidos = models.ForeignKey(
        Lidos.Original, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherTranslation_ref_lidos = models.ForeignKey(
        Lidos.Translation, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    # references to LEGACY
    author_ref_legacy = models.ForeignKey(
        LegacyLegacy.Author, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translator_ref_legacy = models.ForeignKey(
        LegacyLegacy.Translator, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherOriginal_ref_legacy = models.ForeignKey(
        LegacyLegacy.Original, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisherTranslation_ref_legacy = models.ForeignKey(
        LegacyLegacy.Translation, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        if self.name is None:
            return " "
        return escape(self.name)

    def linked_name(self):
        url = reverse(
            "admin:hueb20_person_change",
            args=[self.id],
        )
        link = '<a href="%s">Person: %s</a>' % (url, str(self))
        return link

    def get_translations(self):
        return self.documents.filter(translations__isnull=True).all()

    def get_originals(self):
        return self.documents.filter(originals__isnull=True).all()

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
