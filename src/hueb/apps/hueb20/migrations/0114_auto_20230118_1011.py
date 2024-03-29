# Generated by Django 3.2.5 on 2023-01-18 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0113_validate_links2"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalperson",
            name="cultural_circle",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb20.culturalcircle",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="cultural_circle",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb20.culturalcircle",
            ),
        ),
    ]
