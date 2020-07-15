# Create your models here.


import hueb.apps.hueb_legacy_latein.models as Legacy
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.template.defaultfilters import escape


class YearRange(models.Model):
    id = models.BigAutoField(primary_key=True)
    timerange = IntegerRangeField(null=True, blank=True)
    start_uncertainty = models.IntegerField(null=True, blank=True)
    end_uncertainty = models.IntegerField(null=True, blank=True)
    parsed_string = models.TextField(blank=True, null=True)
    app = models.CharField(max_length=255)
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


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    lifetime = models.OneToOneField(
        YearRange, on_delete=models.CASCADE, null=True, blank=True
    )
    alias = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    is_alias = models.BooleanField(null=True, blank=True)
    app = models.CharField(max_length=255)
    author_ref = models.OneToOneField(
        Legacy.AuthorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translator_ref = models.OneToOneField(
        Legacy.TranslatorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    publisher_ref = models.OneToOneField(
        Legacy.OriginalNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        if self.name is None:
            return " "
        return escape(self.name)


@receiver(post_delete, sender=Person)
def post_delete_lifetime(sender, instance, *args, **kwargs):
    if instance.lifetime:  # just in case user is not specified
        instance.lifetime.delete()


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255)
    app = models.CharField(max_length=255)
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
    app = models.CharField(max_length=255)
    ddc_ref = models.OneToOneField(
        Legacy.DdcGerman, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.ddc_number + " " + self.ddc_name


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=255)
    app = models.CharField(max_length=255)
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
    app = models.CharField(max_length=255)
    location_ref = models.OneToOneField(
        Legacy.LocationNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        if self.name is None:
            return " "
        return self.name


class Archive(models.Model):
    id = models.BigAutoField(primary_key=True)
    signatur = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    app = models.CharField(max_length=255)
    locAssign_ref = models.OneToOneField(
        Legacy.LocAssign, on_delete=models.DO_NOTHING, null=True, blank=True
    )


class Document(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    subtitle = models.TextField(blank=True, null=True)
    published = models.OneToOneField(YearRange, null=False, on_delete=models.CASCADE)
    publisher = models.ManyToManyField(Person, related_name="DocumentPublisher")
    author = models.ManyToManyField(Person, related_name="DocumentAuthor")
    translated_from = models.ManyToManyField("self")
    translated_to = models.ManyToManyField("self")

    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey("Language", on_delete=models.DO_NOTHING)
    year_published = models.DateTimeField(blank=True, null=True)
    country = models.ManyToManyField(Country)

    ddc = models.ForeignKey("DdcGerman", on_delete=models.DO_NOTHING)
    archive = models.ManyToManyField(Archive)

    app = models.CharField(max_length=255)
    origAssign_ref = models.OneToOneField(
        Legacy.OrigAssign, on_delete=models.DO_NOTHING, null=True, blank=True
    )
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
