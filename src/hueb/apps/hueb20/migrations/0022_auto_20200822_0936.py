# Generated by Django 3.0.5 on 2020-08-22 09:36

from django.db import migrations
from hueb.apps.hueb20.models import LATEIN


def load_location(apps, schema_editor):
    Location_legacy = apps.get_model("hueb_legacy_latein", "LocationNew")
    Country = apps.get_model("hueb20", "Country")
    Location = apps.get_model("hueb20", "Location")

    for legacy_location in Location_legacy.objects.all():
        new_location = Location()
        new_location.app = LATEIN
        new_location.location_ref = legacy_location

        new_location.name = legacy_location.name
        new_location.adress = legacy_location.adress
        new_location.hostname = legacy_location.hostname
        new_location.ip = legacy_location.ip
        new_location.z3950_gateway = legacy_location.z3950_gateway

        if legacy_location.country is not None:
            new_location.country = Country.objects.filter(app=LATEIN).get(
                country_ref=legacy_location.country
            )
        else:
            new_location.country = None

        new_location.save()


def unload_location(apps, schema_editor):
    Location = apps.get_model("hueb20", "Location")
    Location.objects.filter(app=LATEIN).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0021_auto_20200822_0839"),
        ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_location, unload_location)]