# Generated by Django 3.2.5 on 2021-07-07 13:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hueb_legacy", "0003_auto_20210707_1343"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name_plural": "Countries"},
        ),
        migrations.AlterModelOptions(
            name="ddcgerman",
            options={"verbose_name_plural": "DDC German"},
        ),
        migrations.AlterModelOptions(
            name="locassign",
            options={"verbose_name_plural": "Loc Assign"},
        ),
        migrations.AlterModelOptions(
            name="manualkeys",
            options={"verbose_name_plural": "ManualKeys"},
        ),
        migrations.AlterModelOptions(
            name="origassign",
            options={"verbose_name_plural": "OrigAssign"},
        ),
        migrations.AlterModelOptions(
            name="pndalias",
            options={"verbose_name_plural": "PndAlias"},
        ),
        migrations.AlterModelOptions(
            name="pndmain",
            options={"verbose_name_plural": "PndMain"},
        ),
        migrations.AlterModelOptions(
            name="pndtitle",
            options={"verbose_name_plural": "PndTitle"},
        ),
        migrations.AlterModelOptions(
            name="swdmain",
            options={"verbose_name_plural": "SwdMain"},
        ),
        migrations.AlterModelOptions(
            name="swdterm",
            options={"verbose_name_plural": "SwdTerm"},
        ),
    ]
