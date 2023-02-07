# Generated by Django 3.2.5 on 2022-02-27 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb_legacy", "0008_auto_20210707_1629"),
        ("hueb20", "0078_auto_20220227_1605"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filing",
            name="locAssign_legacy_ref",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="hueb20_filing_set",
                to="hueb_legacy.locassign",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfiling",
            name="locAssign_legacy_ref",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy.locassign",
            ),
        ),
    ]
