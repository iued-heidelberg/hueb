from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace


def load_original_author(apps, schema_editor):
    Legacy_OriginalAuthor = apps.get_model("hueb_legacy_latein", "OriginalNewAuthorNew")

    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")
    Document = apps.get_model("hueb20", "Document")

    for legacy_original_author in Legacy_OriginalAuthor.objects.all():
        if Contribution.objects.filter(
            originalAuthor_ref=legacy_original_author
        ).exists():
            continue
        new_contribution = Contribution()
        # Set reference to old entries
        new_contribution.originalAuthor_ref = legacy_original_author
        new_contribution.app = LATEIN

        # transfer information

        try:
            new_contribution.person = Person.objects.get(
                author_ref=legacy_original_author.author
            )
        except Exception:
            try:
                new_contribution.person = Person.objects.get(
                    name__iexact=legacy_original_author.author.name
                )
            except Exception:
                print("Could not find person " + legacy_original_author.author.name)
                continue
        new_contribution.document = Document.objects.get(
            original_ref=legacy_original_author.original
        )
        new_contribution.contribution_type = Contribution_Namespace.WRITER

        # save new model
        new_contribution.save()


def unload_original_author(apps, schema_editor):
    apps.get_model("hueb20", "Contribution")
    apps.get_model("hueb20", "Document")
    # Contribution.objects.filter(app=LATEIN).filter(document__get_document_type=Document_Namespace.ORIGINAL).filter(contribution_type=Contribution_Namespace.WRITER).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0059_load_fillings"),
    ]

    operations = [migrations.RunPython(load_original_author, unload_original_author)]
