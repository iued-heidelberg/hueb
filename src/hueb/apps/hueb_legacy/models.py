# Create your models here.
from django.db import models


class SuebAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_author"


class SuebCollection(models.Model):
    id = models.IntegerField(primary_key=True)
    editor = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_collection"


class SuebCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_country"


class SuebDdcGerman(models.Model):
    id = models.IntegerField(primary_key=True)
    ddc_number = models.CharField(max_length=3)
    ddc_name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_ddc_german"


class SuebLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_language"


class SuebLocAssign(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.ForeignKey(
        "SuebLocation", models.DO_NOTHING, blank=True, null=True
    )
    original = models.ForeignKey(
        "SuebOriginal", models.DO_NOTHING, blank=True, null=True
    )
    translation = models.ForeignKey(
        "SuebTranslation", models.DO_NOTHING, blank=True, null=True
    )
    signatur = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_loc_assign"


class SuebLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.ForeignKey(SuebCountry, models.DO_NOTHING, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_location"


class SuebManualKeys(models.Model):
    id = models.IntegerField(primary_key=True)
    original = models.ForeignKey(
        "SuebOriginal", models.DO_NOTHING, blank=True, null=True
    )
    translation = models.ForeignKey(
        "SuebTranslation", models.DO_NOTHING, blank=True, null=True
    )
    term = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = "sueb_manual_keys"


class SuebOrigAssign(models.Model):
    id = models.IntegerField(primary_key=True)
    original = models.ForeignKey(
        "SuebOriginal", models.DO_NOTHING, blank=True, null=True
    )
    translation = models.ForeignKey(
        "SuebTranslation", models.DO_NOTHING, blank=True, null=True
    )
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_orig_assign"


class SuebOriginal(models.Model):
    id = models.IntegerField(primary_key=True)
    ddc = models.ForeignKey(SuebDdcGerman, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(SuebAuthor, models.DO_NOTHING)
    title = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(
        SuebCollection, models.DO_NOTHING, blank=True, null=True
    )
    subtitle = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(SuebLanguage, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_original"


class SuebPndAlias(models.Model):
    id = models.IntegerField(primary_key=True)
    pnd = models.ForeignKey("SuebPndMain", models.DO_NOTHING)
    pnd_alias = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_pnd_alias"


class SuebPndMain(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_pnd_main"


class SuebPndTitle(models.Model):
    id = models.IntegerField(primary_key=True)
    pnd = models.ForeignKey(SuebPndMain, models.DO_NOTHING, blank=True, null=True)
    pnd_title = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_pnd_title"


class SuebSwdMain(models.Model):
    id = models.IntegerField(primary_key=True)
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
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_swd_main"


class SuebSwdTerm(models.Model):
    id = models.IntegerField(primary_key=True)
    swd = models.ForeignKey(SuebSwdMain, models.DO_NOTHING)
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
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_swd_term"


class SuebTranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    ddc = models.ForeignKey(SuebDdcGerman, models.DO_NOTHING, blank=True, null=True)
    translator = models.ForeignKey("SuebTranslator", models.DO_NOTHING)
    author = models.ForeignKey(SuebAuthor, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(
        SuebCollection, models.DO_NOTHING, blank=True, null=True
    )
    subtitle = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    via_language = models.ForeignKey(
        SuebLanguage, models.DO_NOTHING, blank=True, null=True
    )
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_translation"


class SuebTranslator(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = "sueb_translator"
