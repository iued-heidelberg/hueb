from django.db import migrations, DataError

def fill_tempname(apps, schema_editor):
    DdcGerman = apps.get_model("hueb20", "DdcGerman")

    for ddc in DdcGerman.objects.all():
        ddc.ddc_name_temp = ddc.ddc_name
        ddc.save()

def empty_tempname(apps, schema_editor):
    DdcGerman = apps.get_model("hueb20", "DdcGerman")

    for ddc in DdcGerman.objects.all():
        ddc.ddc_name_temp = None
        ddc.save()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0096_auto_20220413_1339"),
    ]

    operations = [
        migrations.RunPython(fill_tempname, empty_tempname)
    ]
