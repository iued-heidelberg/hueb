from django.db import migrations
from hueb.apps.hueb20.models import LIDOS
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace


def load_lidos_authors_trans(apps, schema_editor):
    Translations = apps.get_model("hueb_legacy_lidos", "Translation")
    Document = apps.get_model("hueb20", "Document")
    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")

    for translation in Translations.objects.all():
        for translator in Person.objects.filter(
            translator_ref_lidos=translation.translator
        ).all():
            if translator.name is None or translator.name == "":
                continue
            new_contribution_translator = Contribution()
            new_contribution_translator.app = LIDOS
            try:
                new_contribution_translator.document = Document.objects.get(
                    translation_ref_lidos=translation
                )
                new_contribution_translator.person = translator
                new_contribution_translator.contribution_type = (
                    Contribution_Namespace.WRITER
                )
                new_contribution_translator.save()
            except Exception:
                print(
                    "Could not find document linked to lidos doc:" + translation.title
                )

        # author - original
        for author in Person.objects.filter(author_ref_lidos=translation.author).all():
            if author.name is None or author.name == "":
                continue
            originals = Document.objects.filter(
                translations__translation_ref_lidos=translation
            ).all()
            for original in originals:
                new_contribution_author = Contribution()
                new_contribution_author.app = LIDOS
                new_contribution_author.person = author
                new_contribution_author.document = original
                new_contribution_author.contribution_type = (
                    Contribution_Namespace.WRITER
                )
                new_contribution_author.save()


def unload_lidos_authors_trans(apps, schema_editor):
    Contribution = apps.get_model("hueb20", "Contribution")
    Contribution.objects.filter(app=LIDOS).filter(
        contribution_type=Contribution_Namespace.WRITER
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0070_lidos_translations"),
        # ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [
        migrations.RunPython(load_lidos_authors_trans, unload_lidos_authors_trans)
    ]
