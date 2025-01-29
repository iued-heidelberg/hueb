from django.db import migrations
from hueb.apps.hueb20.models import LIDOS
from hueb.apps.hueb20.models import Document
from hueb.apps.hueb20.models import Language


def create_intermediary_latein(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    TranslationNew = apps.get_model("hueb_legacy", "Translation")

    for document_lat in TranslationNew.objects.filter(
        via_language__isnull=False
    ).exclude(via_language__language=""):
        if not document_lat.language or document_lat.language.language == "":
            continue
        document = (
            Document.objects.filter(app=LIDOS)
            .filter(translation_ref_legacy=document_lat)
            .first()
        )
        if document is None:
            print(document_lat)
            continue
        intermediary = Document()
        intermediary.app = LIDOS
        intermediary.save()

        for original in document.originals.all():
            intermediary.originals.add(original)

        intermediary.language = Language.objects.filter(
            language_de=document_lat.via_language.language.title()
        ).first()
        intermediary.translations.add(document)
        intermediary.ddc = document.ddc
        intermediary.save()
        # remove originals from document and add intermediary
        for original in document.originals.all():
            document.originals.remove(original)
        document.originals.add(intermediary)
        document.save()


def delete_intermediary_latein(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    TranslationNew = apps.get_model("hueb_legacy", "Translation")

    for document_lat in TranslationNew.objects.filter(
        via_language__isnull=False
    ).exclude(via_language__language=""):
        if not document_lat.language or document_lat.language.language == "":
            continue
        document = (
            Document.objects.filter(app=LIDOS)
            .filter(translation_ref_legacy=document_lat)
            .first()
        )
        if document is None:
            continue
        intermediary = document.originals.first()
        document.originals.remove(intermediary)
        for original in intermediary.originals.all():
            document.originals.add(original)
            intermediary.originals.remove(original)
        document.save()
        intermediary.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0138_latein_intermediary_fix"),
    ]

    operations = [
        migrations.RunPython(create_intermediary_latein, delete_intermediary_latein)
    ]
