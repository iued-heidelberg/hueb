# Generated by Django 3.0.5 on 2020-07-09 21:55

from django.db import migrations
from hueb.apps.hueb20.models import LATEIN


def load_countries(apps, schema_editor):
    Country_legacy = apps.get_model("hueb_legacy_latein", "Country")

    Country = apps.get_model("hueb20", "Country")

    for legacy_country in Country_legacy.objects.all():

        new_country = Country()
        # Set reference to old entries
        new_country.country_ref = legacy_country
        new_country.app = LATEIN

        # transfer information
        new_country.country = legacy_country.country

        # save new model
        new_country.save()


def unload_countries(apps, schema_editor):
    Country = apps.get_model("hueb20", "Country")
    Country.objects.filter(app=LATEIN).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0013_load_language"),
        ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_countries, unload_countries)]
