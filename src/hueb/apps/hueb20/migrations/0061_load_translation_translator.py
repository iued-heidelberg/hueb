from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
from hueb.apps.hueb20.models.document import Document as Document_Namespace
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace


def load_translation_translator(apps, schema_editor):
    Legacy_TranslationTranslator = apps.get_model(
        "hueb_legacy_latein", "TranslationNewTranslatorNew"
    )

    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")
    Document = apps.get_model("hueb20", "Document")

    for legacy_translation_translator in Legacy_TranslationTranslator.objects.all():
        if Contribution.objects.filter(
            translationTranslator_ref=legacy_translation_translator
        ).exists():
            continue
        new_contribution = Contribution()
        # Set reference to old entries
        new_contribution.translationTranslator_ref = legacy_translation_translator
        new_contribution.app = LATEIN

        # transfer information
        try:
            new_contribution.person = Person.objects.get(
                translator_ref=legacy_translation_translator.translator
            )
        except Exception:
            try:
                new_contribution.person = Person.objects.get(
                    name__iexact=legacy_translation_translator.translator.name
                )
            except Exception:
                print(
                    "Could not find person "
                    + legacy_translation_translator.translator.name
                )
                continue
        new_contribution.document = Document.objects.get(
            translation_ref=legacy_translation_translator.translation
        )
        new_contribution.contribution_type = Contribution_Namespace.WRITER

        # save new model
        new_contribution.save()


def unload_translation_translator(apps, schema_editor):
    Contribution = apps.get_model("hueb20", "Contribution")
    Document = apps.get_model("hueb20", "Document")
    # Contribution.objects.filter(app=LATEIN).filter(document__get_document_type=Document_Namespace.TRANSLATION).filter(contribution_type=Contribution_Namespace.WRITER).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0060_load_original_author"),
    ]

    operations = [
        migrations.RunPython(load_translation_translator, unload_translation_translator)
    ]
