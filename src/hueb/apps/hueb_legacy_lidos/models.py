from django.db import models


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sueb_lidos_author"


class DdcGerman(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc_number = models.CharField(max_length=3)
    ddc_name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return f"{self.ddc_number}: {self.ddc_name}"

    class Meta:
        verbose_name_plural = "DDC German"
        db_table = "sueb_lidos_ddc_german"


class Filter(models.Model):
    id = models.BigAutoField(primary_key=True)
    a = models.CharField(max_length=255, blank=True, null=True)
    b = models.CharField(max_length=255, blank=True, null=True)
    c = models.CharField(max_length=255, blank=True, null=True)
    d = models.TextField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return f"{self.a} {self.b} {self.c} {self.d}"

    class Meta:
        db_table = "sueb_lidos_filter"


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        return str(self.language)

    class Meta:
        db_table = "sueb_lidos_language"


class LidosEx(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_01 = models.CharField(
        db_column="01", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_03 = models.CharField(
        db_column="03", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_04 = models.CharField(
        db_column="04", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_05 = models.CharField(
        db_column="05", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_06 = models.CharField(
        db_column="06", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_11 = models.CharField(
        db_column="11", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1a = models.CharField(
        db_column="1a", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_12 = models.CharField(
        db_column="12", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_13 = models.CharField(
        db_column="13", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_15 = models.CharField(
        db_column="15", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_20 = models.CharField(
        db_column="20", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_21 = models.CharField(
        db_column="21", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2a = models.CharField(
        db_column="2a", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_22 = models.CharField(
        db_column="22", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_23 = models.CharField(
        db_column="23", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_51 = models.CharField(
        db_column="51", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_52 = models.CharField(
        db_column="52", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_60 = models.CharField(
        db_column="60", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_61 = models.CharField(
        db_column="61", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_62 = models.CharField(
        db_column="62", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_63 = models.CharField(
        db_column="63", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    deskriptoren = models.CharField(max_length=255, blank=True, null=True)
    number_25 = models.CharField(
        db_column="25", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        return str(self.number_01)

    class Meta:
        verbose_name_plural = "Lidos Ex"
        db_table = "sueb_lidos_lidos_ex"


class ManualKeys(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey("Original", models.DO_NOTHING, blank=True, null=True)
    translation = models.ForeignKey(
        "Translation", models.DO_NOTHING, blank=True, null=True
    )
    term = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        return str(self.term)

    class Meta:
        verbose_name_plural = "Manual keys"
        db_table = "sueb_lidos_manual_keys"


class OrigAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey("Original", models.DO_NOTHING, blank=True, null=True)
    translation = models.ForeignKey(
        "Translation", models.DO_NOTHING, blank=True, null=True
    )
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        return f"{getattr(self.original, 'title', ' ')} --> {getattr(self.translation, 'title', ' ')}"

    class Meta:
        db_table = "sueb_lidos_orig_assign"


class Original(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manual_keys = models.ForeignKey(
        ManualKeys,
        models.DO_NOTHING,
        related_name="OriginalManualKeys",
        blank=True,
        null=True,
    )
    real_year = models.IntegerField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "sueb_lidos_original"


class Translation(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    translator = models.ForeignKey(
        "Translator", models.DO_NOTHING, blank=True, null=True
    )
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
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
        related_name="bridgeTranslation",
    )
    comment = models.TextField(blank=True, null=True)
    manual_keys = models.CharField(max_length=255, blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    invisible = models.IntegerField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "sueb_lidos_translation"


class Translator(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "sueb_lidos_translator"
