# Generated by Django 3.0.5 on 2020-08-16 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0015_auto_20200814_2316"),
    ]

    operations = [
        migrations.AlterField(
            model_name="yearrange",
            name="lifetime",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lifetime",
                to="hueb20.Person",
            ),
        ),
    ]
