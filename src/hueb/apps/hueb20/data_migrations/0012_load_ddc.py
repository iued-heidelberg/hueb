# Generated by Django 3.0.5 on 2020-07-09 21:55

from django.db import migrations
from hueb.apps.hueb20.models import LATEIN


def load_DdcGerman(apps, schema_editor):
    Ddc_legacy = apps.get_model("hueb_legacy_latein", "DdcGerman")

    Ddc = apps.get_model("hueb20", "DdcGerman")

    for legacy_ddc in Ddc_legacy.objects.all():
        new_ddc = Ddc()

        new_ddc.ddc_ref = legacy_ddc
        new_ddc.app = LATEIN

        new_ddc.ddc_number = legacy_ddc.ddc_number
        new_ddc.ddc_name = legacy_ddc.ddc_name
        new_ddc.save()


def unload_DdcGerman(apps, schema_editor):
    Ddc = apps.get_model("hueb20", "DdcGerman")
    Ddc.objects.filter(app=LATEIN).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0011_base"),
        ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_DdcGerman, unload_DdcGerman)]