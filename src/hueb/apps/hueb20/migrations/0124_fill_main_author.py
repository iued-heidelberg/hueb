from django.db import migrations
from django.db.models import F


def fill_main_author(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")

    for doc in Document.objects.all():
        if doc.contribution_set.filter(contribution_type="WRITER").exists():
            doc.main_author = (
                doc.contribution_set.filter(contribution_type="WRITER")
                .order_by(F("person__name").asc(nulls_last=True))
                .first()
                .person
            )
            doc.save()


def remove_main_author(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")

    for doc in Document.objects.all():
        doc.main_author = None
        doc.save()


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0123_auto_20230705_0804")]

    operations = [migrations.RunPython(fill_main_author, remove_main_author)]
