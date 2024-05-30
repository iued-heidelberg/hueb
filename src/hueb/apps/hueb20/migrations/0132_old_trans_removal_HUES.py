# flake8: noqa
import csv
import re

from django.db import migrations
from psycopg2.extras import NumericRange


def remove_old_translations(apps, schema_editor):
    # remove translation-documents from HUES that are older than 1500
    HUES = "HUES"
    Document = apps.get_model("hueb20", "Document")
    DocumentRelationship = apps.get_model("hueb20", "DocumentRelationship")
    document_relationships = DocumentRelationship.objects.all()
    documents = Document.objects.filter(tenant__app=HUES).all()
    # get only those that are in german
    for document in documents:
        if document.originals.exists() and not document.translations.exists():
            if document.written_in is not None and document.written_in.lower < 1500:
                pairs = document_relationships.filter(document_to=document)
                for pair in pairs:
                    pair.delete()
                document.delete()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0131_germ_removal")]
    operations = [migrations.RunPython(remove_old_translations, reverse)]
