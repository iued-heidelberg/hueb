# Generated by Django 3.1.3 on 2021-02-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0044_auto_20210209_2347"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalperson",
            name="organisation",
            field=models.BooleanField(blank=None, default=False),
        ),
        migrations.AddField(
            model_name="person",
            name="organisation",
            field=models.BooleanField(blank=None, default=False),
        ),
    ]
