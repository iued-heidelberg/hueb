from django.db import migrations, DataError

def fill_transl_name(apps, schema_editor):
    DdcGerman = apps.get_model("hueb20", "DdcGerman")

    for ddc in DdcGerman.objects.all():
        ddc.ddc_name_de = ddc.ddc_name_temp
        ddc.ddc_name_en = ddc.ddc_name_temp
        ddc.save()

def empty_transl_name(apps, schema_editor):
    DdcGerman = apps.get_model("hueb20", "DdcGerman")

    for ddc in DdcGerman.objects.all():
        ddc.ddc_name_de = None
        ddc.ddc_name_en = None
        ddc.save()

class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0098_auto_20220413_1426"),
    ]

    operations = [
        migrations.RunPython(fill_transl_name, empty_transl_name)
    ]
