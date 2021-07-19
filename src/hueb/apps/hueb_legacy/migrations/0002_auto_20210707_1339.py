# Generated by Django 3.2.5 on 2021-07-07 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hueb_legacy", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SuebManualKeys",
            new_name="ManualKeys",
        ),
        migrations.RenameModel(
            old_name="SuebAuthor",
            new_name="Author",
        ),
        migrations.RenameModel(
            old_name="SuebCollection",
            new_name="Collection",
        ),
        migrations.RenameModel(
            old_name="SuebCountry",
            new_name="Country",
        ),
        migrations.RenameModel(
            old_name="SuebDdcGerman",
            new_name="DdcGerman",
        ),
        migrations.RenameModel(
            old_name="SuebLanguage",
            new_name="Language",
        ),
        migrations.RenameModel(
            old_name="SuebLocAssign",
            new_name="LocAssign",
        ),
        migrations.RenameModel(
            old_name="SuebLocation",
            new_name="Location",
        ),
        migrations.RenameModel(
            old_name="SuebOrigAssign",
            new_name="OrigAssign",
        ),
        migrations.RenameModel(
            old_name="SuebPndAlias",
            new_name="PndAlias",
        ),
        migrations.RenameModel(
            old_name="SuebPndMain",
            new_name="PndMain",
        ),
        migrations.RenameModel(
            old_name="SuebPndTitle",
            new_name="PndTitle",
        ),
        migrations.RenameModel(
            old_name="SuebSwdMain",
            new_name="SwdMain",
        ),
        migrations.RenameModel(
            old_name="SuebSwdTerm",
            new_name="SwdTerm",
        ),
        migrations.RenameModel(
            old_name="SuebTranslator",
            new_name="Translator",
        ),
        migrations.RenameModel(
            old_name="SuebOriginal",
            new_name="Original",
        ),
        migrations.RenameModel(
            old_name="SuebTranslation",
            new_name="Translation",
        ),
    ]