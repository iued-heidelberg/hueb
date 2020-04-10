# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    author_id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'author'


class AuthorNew(models.Model):
    author_id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'author_new'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'country'


class DdcGerman(models.Model):
    ddc_id = models.BigIntegerField(primary_key=True)
    ddc_number = models.CharField(max_length=3)
    ddc_name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ddc_german'


class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'language'


class LocAssign(models.Model):
    loc_assign_id = models.BigAutoField(primary_key=True)
    loc = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    orig = models.ForeignKey('Original', models.DO_NOTHING, blank=True, null=True)
    trans = models.ForeignKey('Translation', models.DO_NOTHING, blank=True, null=True)
    signatur = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    loc_new = models.ForeignKey('LocationNew', models.DO_NOTHING, blank=True, null=True)
    orig_new = models.ForeignKey('OriginalNew', models.DO_NOTHING, blank=True, null=True)
    trans_new = models.ForeignKey('TranslationNew', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_assign'


class Location(models.Model):
    loc_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'location'


class LocationNew(models.Model):
    loc_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'location_new'


class OrigAssign(models.Model):
    orig_assign_id = models.BigAutoField(primary_key=True)
    orig = models.ForeignKey('Original', models.DO_NOTHING, blank=True, null=True, related_name='origassign_orig')
    trans = models.ForeignKey('Translation', models.DO_NOTHING, blank=True, null=True, related_name='origassign_trans')
    orig_diff = models.ForeignKey('Original', models.DO_NOTHING, blank=True, null=True, related_name='origassign_orig_diff')
    trans_diff = models.ForeignKey('Translation', models.DO_NOTHING, blank=True, null=True, related_name='origassign_trans_diff')
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    orig_new = models.ForeignKey('OriginalNew', models.DO_NOTHING, blank=True, null=True, related_name='origassign_new_orig')
    trans_new = models.ForeignKey('TranslationNew', models.DO_NOTHING, blank=True, null=True, related_name='origassign_new_trans')
    orig_diff_new = models.ForeignKey('OriginalNew', models.DO_NOTHING, blank=True, null=True, related_name='origassign_new_orig_diff')
    trans_diff_new = models.ForeignKey('TranslationNew', models.DO_NOTHING, blank=True, null=True, related_name='origassign_new_trans_diff')

    class Meta:
        managed = False
        db_table = 'orig_assign'


class Original(models.Model):
    orig_id = models.BigIntegerField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author0 = models.ForeignKey(Author, models.DO_NOTHING, related_name='original_author0')
    author1 = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True, related_name='original_author1')
    author2 = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True, related_name='original_author2')
    author3 = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True, related_name='original_author3')
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
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    author0_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_author0_new')
    author1_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_author1_new')
    author2_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_author2_new')
    author3_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_author3_new')

    class Meta:
        managed = False
        db_table = 'original'


class OriginalNew(models.Model):
    orig_id = models.BigIntegerField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author0 = models.ForeignKey(Author, models.DO_NOTHING, related_name='original_new_author0')
    author1 = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True, related_name='original_new_author1')
    author2 = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True, related_name='original_new_author2')
    author3 = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True, related_name='original_new_author3')
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
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    author0_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_new_author0_new')
    author1_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_new_author1_new')
    author2_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_new_author2_new')
    author3_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True, related_name='original_new_author3_new')

    class Meta:
        managed = False
        db_table = 'original_new'


class Translation(models.Model):
    trans_id = models.BigIntegerField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    translator0 = models.ForeignKey('Translator', models.DO_NOTHING, related_name='translation_tranlator0')
    translator1 = models.ForeignKey('Translator', models.DO_NOTHING, blank=True, null=True, related_name='translation_tranlator1')
    translator2 = models.ForeignKey('Translator', models.DO_NOTHING, blank=True, null=True, related_name='translation_tranlator2')
    translator3 = models.ForeignKey('Translator', models.DO_NOTHING, blank=True, null=True, related_name='translation_tranlator3')
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    via_language_id = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    translator0_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_tranlator0_new')
    translator1_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_tranlator1_new')
    translator2_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_tranlator2_new')
    translator3_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_tranlator3_new')
    author_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'translation'


class TranslationNew(models.Model):
    trans_id = models.BigIntegerField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    translator0 = models.ForeignKey('Translator', models.DO_NOTHING,  related_name='translation_new_tranlator0')
    translator1 = models.ForeignKey('Translator', models.DO_NOTHING, blank=True, null=True, related_name='translation_new_tranlator1')
    translator2 = models.ForeignKey('Translator', models.DO_NOTHING, blank=True, null=True, related_name='translation_new_tranlator2')
    translator3 = models.ForeignKey('Translator', models.DO_NOTHING, blank=True, null=True, related_name='translation_new_tranlator3')
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    via_language_id = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    translator0_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_new_tranlator0_new')
    translator1_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_new_tranlator1_new')
    translator2_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_new_tranlator2_new')
    translator3_new = models.ForeignKey('TranslatorNew', models.DO_NOTHING, blank=True, null=True, related_name='translation_new_tranlator3_new')
    author_new = models.ForeignKey(AuthorNew, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'translation_new'


class Translator(models.Model):
    translator_id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'translator'


class TranslatorNew(models.Model):
    translator_id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'translator_new'


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    loginname = models.CharField(max_length=255)
    passwort = models.CharField(max_length=12)
    anmerkungen = models.TextField()

    class Meta:
        managed = False
        db_table = 'user'
