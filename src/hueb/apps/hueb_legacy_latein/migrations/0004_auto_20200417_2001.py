# Generated by Django 3.0.5 on 2020-04-17 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hueb_legacy_latein", "0003_auto_20200416_1238"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name_plural": "Author"},
        ),
        migrations.AlterModelOptions(
            name="authornew",
            options={"verbose_name_plural": "NEW Author"},
        ),
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name_plural": "Country"},
        ),
        migrations.AlterModelOptions(
            name="ddcgerman",
            options={"verbose_name_plural": "DDC"},
        ),
        migrations.AlterModelOptions(
            name="language",
            options={"verbose_name_plural": "Language"},
        ),
        migrations.AlterModelOptions(
            name="locassign",
            options={"verbose_name_plural": "LocAssign"},
        ),
        migrations.AlterModelOptions(
            name="location",
            options={"verbose_name_plural": "Location"},
        ),
        migrations.AlterModelOptions(
            name="locationnew",
            options={"verbose_name_plural": "NEW Location"},
        ),
        migrations.AlterModelOptions(
            name="original",
            options={"verbose_name_plural": "Original"},
        ),
        migrations.AlterModelOptions(
            name="originalnew",
            options={"verbose_name_plural": "NEW Original"},
        ),
        migrations.AlterModelOptions(
            name="translation",
            options={"verbose_name_plural": "Translation"},
        ),
        migrations.AlterModelOptions(
            name="translationnew",
            options={"verbose_name_plural": "NEW Translation"},
        ),
        migrations.AlterModelOptions(
            name="translator",
            options={"verbose_name_plural": "Translator"},
        ),
        migrations.AlterModelOptions(
            name="translatornew",
            options={"verbose_name_plural": "NEW Translator"},
        ),
    ]
