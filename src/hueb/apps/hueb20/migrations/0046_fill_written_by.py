from django.db import migrations
from hueb.apps.hueb20.models.contribution import Contribution as contri  # noqa: F401


def fill_written_by(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")

    documents = Document.objects.all()

    for document in documents:
        for contribution in document.contribution_set.filter(contribution_type=contri.WRITER):
            document.written_by.add(contribution.person)


def unfill_written_by(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    documents = Document.objects.all()

    for document in documents:
        document.written_by = None


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0045_auto_20210218_1601"),
    ]

    operations = [migrations.RunPython(fill_written_by, unfill_written_by)]
