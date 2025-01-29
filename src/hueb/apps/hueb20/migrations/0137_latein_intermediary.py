from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
from hueb.apps.hueb20.models import Document
from hueb.apps.hueb20.models import Language


def create_intermediary_latein(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    TranslationNew = apps.get_model("hueb_legacy_latein", "TranslationNew")

    for document_lat in TranslationNew.objects.filter(
        via_language__isnull=False
    ).exclude(via_language__language=""):
        document = (
            Document.objects.filter(app=LATEIN)
            .filter(translation_ref=document_lat)
            .first()
        )
        if document is None:
            print(document_lat)
            continue
        intermediary = Document()
        intermediary.app = LATEIN
        intermediary.save()

        for original in document.originals.all():
            intermediary.originals.add(original)

        intermediary.language = Language.objects.filter(
            language_de=document_lat.via_language.language
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
    TranslationNew = apps.get_model("hueb_legacy_latein", "TranslationNew")

    for document_lat in TranslationNew.objects.filter(
        via_language__isnull=False
    ).exclude(via_language__language=""):
        document = (
            Document.objects.filter(app=LATEIN)
            .filter(translation_ref=document_lat)
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
        ("hueb20", "0136_alter_person_duplicates"),
    ]

    operations = [
        migrations.RunPython(create_intermediary_latein, delete_intermediary_latein)
    ]
