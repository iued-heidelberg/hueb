# Create your models here.


import hueb.apps.hueb_legacy_latein.models as Legacy
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.template.defaultfilters import escape

LATEIN = "LATEIN"
LIDOS = "LIDOS "
LEGACY = "LEGACY"
HUEB20 = "HUEB20"

HUEB_APPLICATIONS = [
    (LATEIN, "HÜB Latein Datensatz"),
    (LIDOS, "HÜB Lidos Datensatz"),
    (LEGACY, "HÜB Basis Datensatz"),
    (HUEB20, "HÜB 2020 Datensatz"),
]


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    person = models.ForeignKey(
        "Person", on_delete=models.CASCADE, null=True, blank=True
    )
    document = models.ForeignKey(
        "Document", on_delete=models.CASCADE, null=True, blank=True
    )
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)

    def __str__(self):
        if self.text is None:
            return " "
        return escape(self.text)


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    alias = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
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


class YearRange(models.Model):
    id = models.BigAutoField(primary_key=True)
    timerange = IntegerRangeField(null=True, blank=True)
    start_uncertainty = models.IntegerField(null=True, blank=True)
    end_uncertainty = models.IntegerField(null=True, blank=True)
    parsed_string = models.TextField(blank=True, null=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    lifetime = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="lifetime",
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


class DdcGerman(models.Model):

    id = models.BigAutoField(primary_key=True)
    ddc_number = models.CharField(max_length=3)
    ddc_name = models.CharField(max_length=255)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    ddc_ref = models.OneToOneField(
        Legacy.DdcGerman, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    class Meta:
        verbose_name = "DDC"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.ddc_number + " " + self.ddc_name


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=255)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    language_ref = models.OneToOneField(
        Legacy.Language,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="language_ref",
    )

    def __str__(self):
        if self.language is None:
            return " "
        return self.language


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.ForeignKey("Country", on_delete=models.DO_NOTHING, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    location_ref = models.OneToOneField(
        Legacy.LocationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        if self.name is None:
            return " "
        return self.name


class Document(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publishers = models.ManyToManyField(Person, related_name="DocumentPublishers")
    written_by = models.ManyToManyField(Person, related_name="DocumentAuthor")
    document_relationships = models.ManyToManyField(
        "self",
        through="DocumentRelationship",
        through_fields=("document_from", "document_to"),
    )

    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(
        "Language", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    real_year = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(
        "Country", blank=True, null=True, on_delete=models.DO_NOTHING
    )

    ddc = models.ForeignKey(
        "DdcGerman", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    located_in = models.ManyToManyField(
        Location, through="Archive", through_fields=("document", "location"),
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

    def __str__(self):
        if self.title is None:
            return " "
        return (self.title[:75] + "[...]") if len(self.title) > 75 else self.title


class DocumentRelationship(models.Model):
    id = models.BigAutoField(primary_key=True)

    document_from = models.ForeignKey(
        Document, on_delete=models.DO_NOTHING, related_name="source"
    )
    document_to = models.ForeignKey(
        Document, on_delete=models.DO_NOTHING, related_name="target"
    )

    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)


class Archive(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    document = models.ForeignKey(
        Document, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    signatur = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    locAssign_ref = models.ForeignKey(
        Legacy.LocAssign, on_delete=models.DO_NOTHING, null=True, blank=True
    )
