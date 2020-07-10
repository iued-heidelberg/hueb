# Generated by Django 3.0.5 on 2020-07-09 21:55

from django.db import migrations


def load_DdcGerman(apps, schema_editor):
    Ddc_legacy = apps.get_model("hueb_legacy_latein", "DdcGerman")

    Ddc = apps.get_model("hueb20", "DdcGerman")
    Source = apps.get_model("hueb20", "SourceReference")

    for legacy_ddc in Ddc_legacy.objects.all():
        source = Source()
        source.app = "hueb_legacy_latein"
        source.model = "DdcGerman"
        source.reference_id = legacy_ddc.id
        source.save()

        new_ddc = Ddc()
        new_ddc.source = source
        new_ddc.ddc_number = legacy_ddc.ddc_number
        new_ddc.ddc_name = legacy_ddc.ddc_name
        new_ddc.save()


def unload_DdcGerman(apps, schema_editor):
    Source = apps.get_model("hueb20", "SourceReference")
    Source.objects.filter(app="hueb_legacy_latein").filter(model="DdcGerman").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0007_load_countries"),
        ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_DdcGerman, unload_DdcGerman)]
