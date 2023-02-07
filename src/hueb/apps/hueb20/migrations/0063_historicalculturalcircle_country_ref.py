# Generated by Django 3.2.5 on 2022-02-14 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "hueb_legacy_latein",
            "0009_rename_original_new_originalnewauthornew_original",
        ),
        ("hueb20", "0048_auto_20220214_1106"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalculturalcircle",
            name="country_ref",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy_latein.country",
            ),
        ),
    ]
