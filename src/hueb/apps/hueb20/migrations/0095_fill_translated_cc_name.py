from django.db import migrations


def fill_transl_name(apps, schema_editor):
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")

    for circle in CulturalCircle.objects.all():
        circle.name_de = circle.name_temp
        circle.name_en = circle.name_temp
        circle.save()


def empty_transl_name(apps, schema_editor):
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")

    for circle in CulturalCircle.objects.all():
        circle.name_de = None
        circle.name_en = None
        circle.save()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0094_auto_20220413_1254"),
    ]

    operations = [migrations.RunPython(fill_transl_name, empty_transl_name)]
