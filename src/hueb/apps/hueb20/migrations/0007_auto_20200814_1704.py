# Generated by Django 3.0.5 on 2020-08-14 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0006_auto_20200812_1137"),
    ]

    operations = [
        migrations.RemoveField(model_name="yearrange", name="person_lifetime",),
        migrations.AddField(
            model_name="person",
            name="lifetime",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lifetime",
                to="hueb20.YearRange",
            ),
        ),
    ]
