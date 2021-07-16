# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    loginname = models.CharField(max_length=255)
    passwort = models.CharField(max_length=12)
    anmerkungen = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sueb_latein_user"
        verbose_name_plural = "Latein User"


class Translator(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    class Meta:
        db_table = "sueb_latein_translator"
        verbose_name_plural = "OLD Translator"


class TranslatorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    class Meta:
        db_table = "sueb_latein_translator_new"
        verbose_name_plural = "Latein Translator"


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    class Meta:
        db_table = "sueb_latein_author"
        verbose_name_plural = "OLD Author"


class AuthorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    class Meta:
        db_table = "sueb_latein_author_new"
        verbose_name_plural = "Latein Author"


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.country is None:
            return " "
        return self.country

    class Meta:
        db_table = "sueb_latein_country"
        verbose_name_plural = "Latein Country"


class DdcGerman(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc_number = models.CharField(max_length=3)
    ddc_name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        return self.ddc_number + " " + self.ddc_name

    class Meta:
        db_table = "sueb_latein_ddc_german"
        verbose_name_plural = "Latein DDC"


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.language is None:
            return " "
        return self.language

    class Meta:
        db_table = "sueb_latein_language"
        verbose_name_plural = "Latein Language"


class LocAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    loc = models.ForeignKey("Location", models.DO_NOTHING, blank=True, null=True)
    orig = models.ForeignKey("Original", models.DO_NOTHING, blank=True, null=True)
    trans = models.ForeignKey("Translation", models.DO_NOTHING, blank=True, null=True)
    signatur = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)
    loc_new = models.ForeignKey("LocationNew", models.DO_NOTHING, blank=True, null=True)
    orig_new = models.ForeignKey(
        "OriginalNew", models.DO_NOTHING, blank=True, null=True
    )
    trans_new = models.ForeignKey(
        "TranslationNew", models.DO_NOTHING, blank=True, null=True
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "sueb_latein_loc_assign"
        verbose_name_plural = "Latein LocAssign"


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    class Meta:
        db_table = "sueb_latein_location"
        verbose_name_plural = "OLD Location"


class LocationNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    class Meta:
        db_table = "sueb_latein_location_new"
        verbose_name_plural = "Latein Location"


class OrigAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    orig = models.ForeignKey("Original", models.DO_NOTHING, blank=True, null=True)
    trans = models.ForeignKey("Translation", models.DO_NOTHING, blank=True, null=True)
    orig_diff = models.ForeignKey(
        "Original", models.DO_NOTHING, blank=True, null=True, related_name="orig_diff"
    )
    trans_diff = models.ForeignKey(
        "Translation",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="trans_diff",
    )
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)
    orig_new = models.ForeignKey(
        "OriginalNew", models.DO_NOTHING, blank=True, null=True
    )
    trans_new = models.ForeignKey(
        "TranslationNew", models.DO_NOTHING, blank=True, null=True
    )
    orig_diff_new = models.ForeignKey(
        "OriginalNew",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="orig_diff_new",
    )
    trans_diff_new = models.ForeignKey(
        "TranslationNew",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="trans_diff_new",
    )

    def __str__(self):
        if self.id is None:
            return " "
        return str(self.id)

    class Meta:
        db_table = "sueb_latein_orig_assign"
        verbose_name_plural = "Latein OrigAssign"


class Original(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)
    author = models.ManyToManyField(Author, through="OriginalAuthor")
    author_new = models.ManyToManyField(AuthorNew, through="OriginalAuthorNew")

    def __str__(self):
        if self.title is None:
            return " "
        return (self.title[:75] + "[...]") if len(self.title) > 75 else self.title

    class Meta:
        db_table = "sueb_latein_original"
        verbose_name_plural = "OLD Original"


class OriginalNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)
    author = models.ManyToManyField(Author, through="OriginalNewAuthor")
    author_new = models.ManyToManyField(AuthorNew, through="OriginalNewAuthorNew")

    def __str__(self):
        if self.title is None:
            return " "
        return (self.title[:75] + "[...]") if len(self.title) > 75 else self.title

    class Meta:
        db_table = "sueb_latein_original_new"
        verbose_name_plural = "Latein Original"


class Translation(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    via_language = models.ForeignKey(
        Language, models.DO_NOTHING, blank=True, null=True, related_name="via_language"
    )
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)
    author_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True)
    translator = models.ManyToManyField(Translator, through="TranslationTranslator")
    translator_new = models.ManyToManyField(
        TranslatorNew, through="TranslationTranslatorNew"
    )

    def __str__(self):
        if self.title is None:
            return " "
        return (self.title[:75] + "[...]") if len(self.title) > 75 else self.title

    class Meta:
        db_table = "sueb_latein_translation"
        verbose_name_plural = "OLD Translation"


class TranslationNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    via_language = models.ForeignKey(
        Language,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="new_via_language",
    )
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(default=False)
    author_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True)
    translator = models.ManyToManyField(Translator, through="TranslationNewTranslator")
    translator_new = models.ManyToManyField(
        TranslatorNew, through="TranslationNewTranslatorNew"
    )

    def __str__(self):
        if self.title is None:
            return " "
        return (self.title[:75] + "[...]") if len(self.title) > 75 else self.title

    class Meta:
        db_table = "sueb_latein_translation_new"
        verbose_name_plural = "Latein Translation"


class OriginalAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey(Original, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "sueb_latein_original_author"


class OriginalAuthorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey(Original, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "sueb_latein_original_author_new"


class OriginalNewAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey(OriginalNew, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "sueb_latein_original_new_author"


class OriginalNewAuthorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey(OriginalNew, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "sueb_latein_original_new_author_new"


class TranslationNewTranslator(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation = models.ForeignKey(
        TranslationNew, models.DO_NOTHING, blank=True, null=True
    )
    translator = models.ForeignKey(
        "Translator", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        db_table = "sueb_latein_translation_new_translator"


class TranslationNewTranslatorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation = models.ForeignKey(
        TranslationNew, models.DO_NOTHING, blank=True, null=True
    )
    translator = models.ForeignKey(
        "TranslatorNew", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        db_table = "sueb_latein_translation_new_translator_new"


class TranslationTranslator(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation = models.ForeignKey(
        Translation, models.DO_NOTHING, blank=True, null=True
    )
    translator = models.ForeignKey(
        "Translator", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        db_table = "sueb_latein_translation_translator"


class TranslationTranslatorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation = models.ForeignKey(
        Translation, models.DO_NOTHING, blank=True, null=True
    )
    translator = models.ForeignKey(
        "TranslatorNew", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        db_table = "sueb_latein_translation_translator_new"
