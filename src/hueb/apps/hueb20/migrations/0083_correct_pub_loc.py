from django.db import migrations
from hueb.apps.hueb20.models import LEGACY


def correct_pub_loc(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")

    for document in Document.objects.filter(app=LEGACY).all():
        if (
            document.published_location is not None
            and document.published_location != ""
        ):
            document.published_location = document.published_location.strip("[]")
            document.save()


def uncorrect_pub_loc(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0082_latein_correction_name"),
        # ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(correct_pub_loc, uncorrect_pub_loc)]
