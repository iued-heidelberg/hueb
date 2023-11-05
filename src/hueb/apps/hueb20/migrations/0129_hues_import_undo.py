# flake8: noqa
import csv
import re

from django.db import migrations
from psycopg2.extras import NumericRange


def undo_hues_docs(apps, schema_editor):
    HUES = "HUES"
    Hues_comment = apps.get_model("hueb20", "Comment")
    Hues_comment.objects.filter(app=HUES).all().delete()
    Hues_document_relationship = apps.get_model("hueb20", "DocumentRelationship")
    Hues_document_relationship.objects.filter(document_from__app=HUES).filter(
        document_to__app=HUES
    ).all().delete()
    Hues_document = apps.get_model("hueb20", "Document")
    Hues_document.objects.filter(app=HUES).all().delete()
    Hues_Contribution = apps.get_model("hueb20", "Contribution")
    Hues_Contribution.objects.filter(app=HUES).all().delete()
    Hues_filing = apps.get_model("hueb20", "Filing")
    Hues_filing.objects.filter(app=HUES).all().delete()


def unundo_hues_docs(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0128_hues_import_2")]
    operations = [migrations.RunPython(undo_hues_docs, unundo_hues_docs)]
