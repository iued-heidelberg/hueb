import hueb.apps.hueb_legacy_latein.models as Legacy
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from hueb.apps.hueb20.models import HUEB20, HUEB_APPLICATIONS
from simple_history.models import HistoricalRecords

from .archive import Archive
from .culturalCircle import CulturalCircle
from .ddc import DdcGerman
from .language import Language
from .person import Person


class Document(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    written_in = IntegerRangeField(null=True, blank=True)
    publishers = models.ManyToManyField(Person, related_name="DocumentPublishers")
    written_by = models.ManyToManyField(Person, related_name="DocumentAuthor")
    translations = models.ManyToManyField(
        "self",
        symmetrical=False,
        through="DocumentRelationship",
        through_fields=("document_from", "document_to"),
        related_name="originals",
    )

    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(
        Language, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    cultural_circle = models.ForeignKey(
        CulturalCircle, blank=True, null=True, on_delete=models.DO_NOTHING
    )

    ddc = models.ForeignKey(
        DdcGerman, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    located_in = models.ManyToManyField(
        Archive, through="Filing", through_fields=("document", "archive"),
    )
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    original_ref = models.OneToOneField(
        Legacy.OriginalNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translation_ref = models.OneToOneField(
        Legacy.TranslationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    originalAuthor_ref = models.OneToOneField(
        Legacy.OriginalNewAuthorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translationTranslator_ref = models.OneToOneField(
        Legacy.TranslationNewTranslatorNew,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    history = HistoricalRecords()

    def __str__(self):
        if self.title is None:
            return " "
        return (self.title[:75] + "[...]") if len(self.title) > 75 else self.title

    # def translations(self):
    #    self.document_relationships.filter()

    #    return None


class DocumentRelationship(models.Model):
    id = models.BigAutoField(primary_key=True)

    document_from = models.ForeignKey(
        "Document", on_delete=models.DO_NOTHING, related_name="to_original"
    )
    document_to = models.ForeignKey(
        "Document", on_delete=models.DO_NOTHING, related_name="to_translation"
    )

    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
