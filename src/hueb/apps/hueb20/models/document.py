import hueb.apps.hueb_legacy.models as LegacyLegacy
import hueb.apps.hueb_legacy_latein.models as Legacy
import hueb.apps.hueb_legacy_lidos.models as Lidos
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.db.models import F, Q
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
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

    ORIGINAL = _("Original")
    TRANSLATION = _("Übersetzung")
    BRIDGE = _("Brückenübersetzung")

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
    # This field is only necessary to identify language of the original when the original itself is not in the database
    language_orig = models.ForeignKey(
        Language,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="temp_originals",
    )
    cultural_circle = models.ForeignKey(
        CulturalCircle, blank=True, null=True, on_delete=models.DO_NOTHING
    )

    ddc = models.ForeignKey(
        DdcGerman, on_delete=models.DO_NOTHING, blank=True, null=True
    )

    contributions = models.ManyToManyField(
        Person, through="Contribution", related_name="documents"
    )

    main_author = models.ForeignKey(
        Person, on_delete=models.DO_NOTHING, blank=True, null=True
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
    original_ref_lidos = models.OneToOneField(
        Lidos.Original, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translation_ref_lidos = models.OneToOneField(
        Lidos.Translation, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    original_ref_legacy = models.OneToOneField(
        LegacyLegacy.Original, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translation_ref_legacy = models.OneToOneField(
        LegacyLegacy.Translation, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if self.contribution_set.filter(contribution_type="WRITER").exists():
            main_author = (
                self.get_authors()
                .order_by(F("person__name").asc(nulls_last=True))
                .first()
                .person
            )
            if self.main_author != main_author:
                self.main_author = main_author
        super(Document, self).save(*args, **kwargs)

    def get_document_type(self):
        if self.translations.exists() and not self.originals.exists():
            return Document.ORIGINAL
        if self.originals.exists() and not self.translations.exists():
            return Document.TRANSLATION
        if self.originals.exists() and self.translations.exists():
            return Document.BRIDGE

        # In case of a translation without original or original without translation:
        if (
            DocumentRelationship.objects.filter(document_from=self)
            .filter(document_to__isnull=True)
            .exists()
        ):
            return Document.ORIGINAL
        if (
            DocumentRelationship.objects.filter(document_to=self)
            .filter(document_from__isnull=True)
            .exists()
        ):
            return Document.TRANSLATION

    def get_cultural_circle(self):
        main_author = self.get_authors().first()
        if main_author:
            circle = main_author.person.cultural_circle
            if circle:
                return circle
        else:
            return self.cultural_circle

    def get_authors(self):
        return self.contribution_set.filter(contribution_type="WRITER").filter(
            person__isnull=False
        )

    """
    def get_original_author(self):
        if self.get_document_type() == Document.ORIGINAL:
            return self.get_authors()
        else:
            if self.originals.exists():
                if self.originals.first().get_document_type() == Document.ORIGINAL:
                    if self.originals.first().get_authors().exists():
                        return self.originals.first().get_authors()
                else:
                    if self.originals.first().originals.first().get_authors().exists():
                        return self.originals.first().originals.first().get_authors()
    """

    def get_translation(self):
        return self.translations.all().order_by("title")

    def get_originals(self):
        return self.originals.all().order_by("title")

    def get_original_authors(self):
        return self.get_original_attr("get_authors")

    def get_original_language(self):
        return self.get_original_attr("language")[0]

    def get_original_attr(self, attr, *args):
        return self.get_rec_attr(attr, 0, *args)

    def get_bridge_attr(self, attr, *args):
        return self.get_rec_attr(attr, 1, *args)

    def get_rec_attr(self, attr, i, *args):
        docs = Document.get_originals_and_bridges(self)[i]
        if docs:
            if callable(getattr(docs[0], attr)):
                if isinstance(getattr(docs[0], attr)(*args), QuerySet):
                    values = set()
                    for doc in docs:
                        values.update([value for value in getattr(doc, attr)(*args)])
                    values = list(values)
                else:
                    values = list(set([getattr(doc, attr)(*args) for doc in docs]))
            else:
                if isinstance(getattr(docs[0], attr), QuerySet):
                    values = set()
                    for doc in docs:
                        values.update([value for value in getattr(doc, attr)])
                    values = list(values)
                else:
                    values = list(set([getattr(doc, attr) for doc in docs]))
            return values

    @classmethod
    def get_originals_and_bridges(cls, document):
        originals = set()
        bridges = set()
        if document.originals.exists():
            for original in document.originals.all():
                if original.originals.exists():
                    bridges.add(original)
                    rec_originals, rec_bridges = Document.get_originals_and_bridges(
                        original
                    )
                    originals.update(rec_originals)
                    bridges.update(rec_bridges)
                else:
                    originals.add(original)
        else:
            originals.add(document)
        return list(originals), list(bridges)

    def get_contributor_names(self, contribution_type):
        contributors = []
        for contribution in self.contribution_set.filter(
            contribution_type=contribution_type
        ):
            contributors.append(contribution.person.name)
        return contributors

    def get_publishers(self):
        return self.contribution_set.filter(contribution_type="PUBLISHER").filter(
            person__isnull=False
        )

    def get_language(self):
        return self.language

    # get language of the original if no original in database - necessary for LEGACY
    def get_language_orig(self):
        return self.language_orig

    def get_filings(self):
        return self.filing_set.all().order_by("archive__name")

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.__total__ = None

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
        ("title", _("Titel")),
        ("author", _("Person")),
        ("ddc", _("DDC")),
        ("year", _("Jahr")),
        ("language", _("Sprache")),
        ("app", _("Datenbank")),
    )

    sortable_attributes = (
        ("written_in", _("Sortiert nach Jahr")),
        ("title", _("Sortiert nach Titel")),
        ("main_author__name", _("Sortiert nach Autor")),
        ("ddc", _("Sortiert nach DDC")),
    )

    def serialize_written_in(self):
        return timerange_serialization(self.written_in)

    serialize_written_in.short_description = "Written in"

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
        elif query["attribute"] == "language":
            return Document.q_object_by_type(query["search_language"])
        elif query["attribute"] == "app":
            return Document.q_object_by_app(query["search_database"])
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

    @classmethod
    def q_object_by_app(cls, value):
        return Q(app__icontains=value)

    def get_docs_online_only(self, only_online: bool = True):
        if only_online:
            if self.filing_set.filter(archive="Online-Version").exists():
                return self


class DocumentRelationship(Reviewable):
    id = models.BigAutoField(primary_key=True)

    document_from = models.ForeignKey(
        "Document",
        on_delete=models.DO_NOTHING,
        related_name="to_original",
        null=True,
        blank=True,
    )
    document_to = models.ForeignKey(
        "Document",
        on_delete=models.DO_NOTHING,
        related_name="to_translation",
        null=True,
        blank=True,
    )

    original_ref = models.OneToOneField(
        Legacy.OriginalNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translation_ref = models.OneToOneField(
        Legacy.TranslationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)

    @classmethod
    def get_q_object(cls, query, types):
        if query["attribute"] == "title":
            return DocumentRelationship.q_object_by_title(query["search_text"], types)
        elif query["attribute"] == "author":
            return DocumentRelationship.q_object_by_author(query["search_text"], types)
        elif query["attribute"] == "ddc":
            return DocumentRelationship.q_object_by_ddc(query["search_ddc"], types)
        elif query["attribute"] == "year":
            return DocumentRelationship.q_object_by_written_in(
                query["search_year_from"], query["search_year_to"], types
            )
        elif query["attribute"] == "language":
            return DocumentRelationship.q_object_by_language(
                query["search_language"], types
            )
        elif query["attribute"] == "app":
            return DocumentRelationship.q_object_by_app(query["search_database"], types)
        else:
            return Q()

    @classmethod
    def get_type_q(cls, type, document_from):
        if document_from:
            if type == Document.ORIGINAL:
                return (
                    Q(document_from__originals__isnull=True)
                    & Q(document_from__translations__isnull=False)
                ) | Q(document_to__isnull=True)
            elif type == Document.TRANSLATION:
                return Q(document_from__originals__isnull=False) & Q(
                    document_from__translations__isnull=True
                )
            elif type == Document.BRIDGE:
                return Q(document_from__originals__isnull=False) & Q(
                    document_from__translations__isnull=False
                )
        else:
            if type == Document.ORIGINAL:
                return Q(document_to__originals__isnull=True) & Q(
                    document_to__translations__isnull=False
                )
            elif type == Document.TRANSLATION:
                return (
                    Q(document_to__originals__isnull=False)
                    & Q(document_to__translations__isnull=True)
                ) | Q(document_from__isnull=True)
            else:
                return Q(document_to__originals__isnull=False) & Q(
                    document_to__translations__isnull=False
                )

    @classmethod
    def get_types_q(cls, types, document_from):
        type_q = Q()
        for type in types:
            if document_from:
                type_q |= cls.get_type_q(type, True)
            else:
                type_q |= cls.get_type_q(type, False)
        return type_q

    @classmethod
    def get_online_q(cls):
        return Q(document_to__filing_set__archive="Online-Version")

    @classmethod
    def q_object_by_title(cls, value, types):
        return (
            Q(document_from__title__icontains=value)
            | Q(document_from__subtitle__icontains=value)
        ) & Q(document_from__title__icontains=value) & cls.get_types_q(types, True) | (
            Q(document_to__title__icontains=value)
            | Q(document_to__subtitle__icontains=value)
        ) & cls.get_types_q(
            types, False
        )

    @classmethod
    def q_object_by_author(cls, value, types):
        return Q(
            document_from__contribution__person__name__icontains=value
        ) & cls.get_types_q(types, True) & Q(
            document_from__contribution__contribution_type="WRITER"
        ) | Q(
            document_to__contribution__person__name__icontains=value
        ) & Q(
            document_to__contribution__contribution_type="WRITER"
        ) & cls.get_types_q(
            types, False
        )

    @classmethod
    def q_object_by_ddc(cls, value, types):
        value = value[:3]
        if value.endswith("00"):
            match_up_to = 1
        elif value.endswith("0"):
            match_up_to = 2
        else:
            match_up_to = 3
        return Q(
            document_from__ddc__ddc_number__iregex=rf"^{value[:match_up_to]}"
        ) & cls.get_types_q(types, True) | Q(
            document_to__ddc__ddc_number__iregex=rf"^{value[:match_up_to]}"
        ) & cls.get_types_q(
            types, False
        )

    @classmethod
    def q_object_by_written_in(cls, lower, upper, types):
        return Q(
            document_from__written_in__overlap=NumericRange(lower, upper)
        ) & cls.get_types_q(types, True) | Q(
            document_to__written_in__overlap=NumericRange(lower, upper)
        ) & cls.get_types_q(
            types, False
        )

    @classmethod
    def q_object_by_language(cls, value, types):
        return (
            Q(document_from__language__language_en__icontains=value)
            | Q(document_from__language__language_de__icontains=value)
        ) & cls.get_types_q(types, True) | (
            Q(document_to__language__language_en__icontains=value)
            | Q(document_to__language__language_de__icontains=value)
        ) & cls.get_types_q(
            types, False
        )

    @classmethod
    def q_object_by_app(cls, value, types):
        return Q(document_from__app__icontains=value) & cls.get_types_q(
            types, True
        ) | Q(document_to__app__icontains=value) & cls.get_types_q(types, False)

    def __init__(self, *args, **kwargs):
        super(DocumentRelationship, self).__init__(*args, **kwargs)
        self.__total__ = None

    def mark_reviewed(self, updated=[]):
        if self not in updated:
            super().mark_reviewed(updated=updated)
            self.document_from.mark_reviewed(updated)
            self.document_to.mark_reviewed(updated)
