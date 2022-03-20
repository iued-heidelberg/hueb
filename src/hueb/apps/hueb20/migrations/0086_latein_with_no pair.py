from django.db import migrations, DataError
from hueb.apps.hueb20.models import LATEIN


def create_placeholder_relationships(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    DocumentRelationship = apps.get_model("hueb20", "DocumentRelationship")

    # Filter translations
    for document in (
        Document.objects.filter(app=LATEIN).filter(translation_ref__isnull=False).all()
    ):
        if document.originals.exists():
            continue
        else:
            document_relationship = DocumentRelationship()
            document_relationship.document_to = document
            document_relationship.document_from = None
            document_relationship.save()

    # Filter originals
    for document in (
        Document.objects.filter(app=LATEIN).filter(original_ref__isnull=False).all()
    ):
        if document.translations.exists():
            continue
        else:
            document_relationship = DocumentRelationship()
            document_relationship.document_from = document
            document_relationship.document_to = None
            document_relationship.save()


def uncreate_placeholder_relationships(apps, schema_editor):
    DocumentRelationship = apps.get_model("hueb20", "DocumentRelationship")
    DocumentRelationship.objects.filter(document_from__app=LATEIN).filter(
        document_to__isnull=True
    ).delete()
    DocumentRelationship.objects.filter(document_to__app=LATEIN).filter(
        document_from__isnull=True
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0085_document_with_no_pair"),
    ]

    operations = [
        migrations.RunPython(
            create_placeholder_relationships, uncreate_placeholder_relationships
        )
    ]
