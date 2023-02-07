from django.db import migrations


def fill_tempname(apps, schema_editor):
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")

    for circle in CulturalCircle.objects.all():
        circle.name_temp = circle.name
        circle.save()


def empty_tempname(apps, schema_editor):
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")

    for circle in CulturalCircle.objects.all():
        circle.name_temp = None
        circle.save()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0092_auto_20220413_1248"),
    ]

    operations = [migrations.RunPython(fill_tempname, empty_tempname)]
