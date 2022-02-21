from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
import re


def update_latein(apps, schema_editor):
    DocumentRelationship = apps.get_model("hueb20", "DocumentRelationship")
    DocumentRelationship.objects.filter(document_from__app=LATEIN).filter(
        document_from__title__isnull=True
    ).all().delete()
    DocumentRelationship.objects.filter(document_from__app=LATEIN).filter(
        document_to__title__isnull=True
    ).all().delete()


def undo_latein(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0062_auto_20220212_1534"),
    ]

    operations = [migrations.RunPython(update_latein, undo_latein)]
