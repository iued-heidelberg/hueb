from django.db import migrations
from hueb.apps.hueb20.models.contribution import Contribution as contri  # noqa: F401


def create_contributions(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Contribution = apps.get_model("hueb20", "Contribution")

    documents = Document.objects.all()

    for document in documents:
        authors = document.written_by.all()
        for author in authors:
            c = Contribution(
                person=author,
                document=document,
                contribution_type=contri.WRITER,  # noqa: F811
                originalAuthor_ref=document.originalAuthor_ref,
                translationTranslator_ref=document.translationTranslator_ref,
            )
            c.save()

        publishers = document.publishers.all()
        for publisher in publishers:
            c = Contribution(
                person=publisher,
                document=document,
                contribution_type=contri.PUBLISHER,  # noqa: F811
            )
            c.save()


def uncreate_contributions(apps, schema_editor):
    Contribution = apps.get_model("hueb20", "Contribution")
    c = Contribution.objects.all()
    c.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0042_auto_20210207_1725"),
    ]

    operations = [migrations.RunPython(create_contributions, uncreate_contributions)]
