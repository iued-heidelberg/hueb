# Create your models here.
from django.db import models


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = "sueb_author"

    def __str__(self) -> str:
        return str(self.name)


class Collection(models.Model):
    id = models.BigAutoField(primary_key=True)
    editor = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = "sueb_collection"

    def __str__(self) -> str:
        return str(self.title)


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.country)

    class Meta:
        db_table = "sueb_country"
        verbose_name_plural = "Countries"


class DdcGerman(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc_number = models.CharField(max_length=3, blank=True, null=True)
    ddc_name = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.ddc_number}: {self.ddc_name}"

    class Meta:
        db_table = "sueb_ddc_german"
        verbose_name_plural = "DDC German"


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.language)

    class Meta:
        db_table = "sueb_language"


class LocAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.ForeignKey("Location", models.DO_NOTHING, blank=True, null=True)
    original = models.ForeignKey("Original", models.DO_NOTHING, blank=True, null=True)
    translation = models.ForeignKey(
        "Translation", models.DO_NOTHING, blank=True, null=True
    )
    signatur = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.signatur)

    class Meta:
        db_table = "sueb_loc_assign"
        verbose_name_plural = "Loc Assign"


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "sueb_location"


class ManualKeys(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey("Original", models.DO_NOTHING, blank=True, null=True)
    translation = models.ForeignKey(
        "Translation", models.DO_NOTHING, blank=True, null=True
    )
    term = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.term)

    class Meta:
        verbose_name_plural = "ManualKeys"
        db_table = "sueb_manual_keys"


class OrigAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey("Original", models.DO_NOTHING, blank=True, null=True)
    translation = models.ForeignKey(
        "Translation", models.DO_NOTHING, blank=True, null=True
    )
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{getattr(self.original, 'title', ' ')} --> {getattr(self.translation, 'title', ' ')}"

    class Meta:
        verbose_name_plural = "OrigAssign"
        db_table = "sueb_orig_assign"


class Original(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "sueb_original"


class PndAlias(models.Model):
    id = models.BigAutoField(primary_key=True)
    pnd = models.ForeignKey("PndMain", models.DO_NOTHING, blank=True, null=True)
    pnd_alias = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.pnd_alias)

    class Meta:
        verbose_name_plural = "PndAlias"
        db_table = "sueb_pnd_alias"


class PndMain(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.person)

    class Meta:
        verbose_name_plural = "PndMain"
        db_table = "sueb_pnd_main"


class PndTitle(models.Model):
    id = models.BigAutoField(primary_key=True)
    pnd = models.ForeignKey(PndMain, models.DO_NOTHING, blank=True, null=True)
    pnd_title = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.pnd_title)

    class Meta:
        verbose_name_plural = "PndTitle"
        db_table = "sueb_pnd_title"


class SwdMain(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_800_hauptschlagwort = models.CharField(
        db_column="800_hauptschlagwort", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_801_unterschlagwort1 = models.CharField(
        db_column="801_unterschlagwort1", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_802_unterschlagwort2 = models.CharField(
        db_column="802_unterschlagwort2", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.number_800_hauptschlagwort} --> {self.number_801_unterschlagwort1} --> {self.number_802_unterschlagwort2}"

    class Meta:
        verbose_name_plural = "SwdMain"
        db_table = "sueb_swd_main"


class SwdTerm(models.Model):
    id = models.BigAutoField(primary_key=True)
    swd = models.ForeignKey(SwdMain, models.DO_NOTHING, blank=True, null=True)
    number_820_alternativform = models.CharField(
        db_column="820_alternativform", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_830_aequivalentebezeichnung = models.CharField(
        db_column="830_aequivalentebezeichnung", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_845_oberbegriff = models.CharField(
        db_column="845_oberbegriff", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_850_uebergeordnetesschlagwort = models.CharField(
        db_column="850_uebergeordnetesschlagwort", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_860_verwandtesschlagwort = models.CharField(
        db_column="860_verwandtesschlagwort", max_length=255, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.number_845_oberbegriff)

    class Meta:
        verbose_name_plural = "SwdTerm"
        db_table = "sueb_swd_term"


class Translation(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    translator = models.ForeignKey(
        "Translator", models.DO_NOTHING, blank=True, null=True
    )
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
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
        related_name="BridgeLanguage",
    )
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "sueb_translation"


class Translator(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "sueb_translator"
