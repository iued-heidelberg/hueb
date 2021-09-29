import hueb.apps.hueb_legacy_latein.models as Legacy
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.db.models import Q
from django.urls import reverse
from hueb.apps.hueb20.models.archive import Archive
from hueb.apps.hueb20.models.culturalCircle import CulturalCircle
from hueb.apps.hueb20.models.ddc import DdcGerman
from hueb.apps.hueb20.models.language import Language
from hueb.apps.hueb20.models.person import Person
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import (
    HUEB20,
    HUEB_APPLICATIONS,
    timerange_serialization,
)
from psycopg2.extras import NumericRange


class Document(Reviewable):
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

    contributions = models.ManyToManyField(
        Person,
        through="Contribution",
    )

    located_in = models.ManyToManyField(
        Archive,
        through="Filing",
        through_fields=("document", "archive"),
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

    def get_author_contributions(self):
        return self.contribution_set.filter(contribution_type="WRITER")
        # Function is used to display authors only on single_result_document

    def mark_reviewed(self, updated=[]):
        if self not in updated:
            super().mark_reviewed(updated=updated)

            self.language.mark_reviewed(updated)
            self.cultural_circle.mark_reviewed(updated)
            self.ddc.mark_reviewed(updated)

            for contribution in self.contribution_set.all():
                contribution.mark_reviewed(updated)

            for filing in self.filing_set.all():
                filing.mark_reviewed(updated)

            # Marking related documents as reviewed will lead to an explosion of review updates. The effect of those will not be obvious to the user.
            # for relationship in self.to_original.all().union(self.to_translation.all()):
            #    relationship.mark_reviewed(updated)

    def __str__(self):
        if self.title is None:
            return " "
        return (self.title[:75] + "[...]") if len(self.title) > 75 else self.title

    def linked_name(self):
        url = reverse(
            "admin:hueb20_document_change",
            args=[self.id],
        )
        link = '<a href="%s">Document: %s</a>' % (url, str(self))
        return link

    searchable_attributes = (
        ("title", "Titel"),
        ("author", "Autor"),
        ("ddc", "DDC"),
        ("year", "Jahr"),
    )

    def adapt_document_written_in_list_view(self):
        return timerange_serialization(self.written_in)

    adapt_document_written_in_list_view.short_description = "Written in"

    @classmethod
    def get_q_object(cls, query):
        if query["attribute"] == "title":
            return Document.q_object_by_title(query["search_text"])
        elif query["attribute"] == "author":
            return Document.q_object_by_author(query["search_text"])
        elif query["attribute"] == "ddc":
            return Document.q_object_by_ddc(query["search_ddc"])
        elif query["attribute"] == "year":
            return Document.q_object_by_written_in(
                query["search_year_from"], query["search_year_to"]
            )
        else:
            return Q()

    @classmethod
    def q_object_by_title(cls, value):
        return Q(title__icontains=value)

    @classmethod
    def q_object_by_author(cls, value):
        return Q(contribution__person__name__icontains=value) & Q(
            contribution__contribution_type="WRITER"
        )

    @classmethod
    def q_object_by_ddc(cls, value):
        return Q(ddc__ddc_number__contains=value)

    @classmethod
    def q_object_by_written_in(cls, lower, upper):
        return Q(written_in__overlap=NumericRange(lower, upper))


class DocumentRelationship(Reviewable):
    id = models.BigAutoField(primary_key=True)

    document_from = models.ForeignKey(
        "Document", on_delete=models.DO_NOTHING, related_name="to_original"
    )
    document_to = models.ForeignKey(
        "Document", on_delete=models.DO_NOTHING, related_name="to_translation"
    )

    original_ref = models.OneToOneField(
        Legacy.OriginalNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translation_ref = models.OneToOneField(
        Legacy.TranslationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)

    def mark_reviewed(self, updated=[]):
        if self not in updated:
            super().mark_reviewed(updated=updated)
            self.document_from.mark_reviewed(updated)
            self.document_to.mark_reviewed(updated)
