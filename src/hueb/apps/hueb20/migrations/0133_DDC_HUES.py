# flake8: noqa
import csv
import re

from django.db import migrations
from psycopg2.extras import NumericRange


def add_DDC(apps, schema_editor):
    # add DDC 800 to all documents from tenant HUES
    HUES = "HUES"
    Document = apps.get_model("hueb20", "Document")
    DDC_Object = apps.get_model("hueb20", "DdcGerman")
    # get DDC 800
    if DDC_Object.objects.filter(ddc_number="800").exists():
        DDC_800 = DDC_Object.objects.get(ddc_number="800")

        documents = Document.objects.filter(tenant__app=HUES).all()
        for document in documents:
            document.ddc = DDC_800
            document.save()
            print(f"DDC added to {document.title}")


def remove_DDC(apps, schema_editor):
    # remove DDC 800 from all documents from tenant HUES
    HUES = "HUES"
    Document = apps.get_model("hueb20", "Document")
    documents = Document.objects.filter(tenant__app=HUES).all()
    for document in documents:
        document.ddc = None
        document.save()
        print(f"DDC removed from {document.title}")


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0132_old_trans_removal_HUES")]
    operations = [migrations.RunPython(add_DDC, remove_DDC)]
