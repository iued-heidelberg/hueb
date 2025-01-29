from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
from hueb.apps.hueb20.models import Document
from hueb.apps.hueb20.models import Language


def fix_intermediary_latein(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    TranslationNew = apps.get_model("hueb_legacy_latein", "TranslationNew")

    for document_lat in TranslationNew.objects.all():
        document = (
            Document.objects.filter(app=LATEIN)
            .filter(translation_ref=document_lat)
            .first()
        )
        orig_lang = (
            document_lat.language.language
            if document_lat.language is not None
            else None
        )
        via_lang = (
            document_lat.via_language.language
            if document_lat.via_language is not None
            else None
        )

        if (
            via_lang == ""
            or via_lang is None
            or orig_lang == ""
            or orig_lang is None
            or via_lang == "Deutsch"
            or orig_lang == "Deutsch"
        ):
            continue

        if document is None:
            print(document_lat.title)
            continue
        if not document.originals.exists():
            # no bridge and no original. Create both
            intermediary = Document()
            intermediary.app = LATEIN
            intermediary.language = Language.objects.filter(
                language_de=via_lang
            ).first()
            intermediary.translations.add(document)
            intermediary.ddc = document.ddc
            intermediary.save()

            original = Document()
            original.app = LATEIN
            original.language = Language.objects.filter(language_de=orig_lang).first()
            original.tranlsations.add(intermediary)
            original.ddc = document.ddc
            original.save()
            continue

        if document.originals.count() > 1:
            print(document.title)
            continue

        if not document.originals.first().originals.exists():
            # either only a bridge or only an original exists
            language_of_existing = document.originals.first().language.language_de
            if language_of_existing == via_lang:
                # only a bridge exists. Create an original
                original = Document()
                original.app = LATEIN
                original.language = Language.objects.filter(
                    language_de=orig_lang
                ).first()
                original.ddc = document.ddc
                original.save()
                original.translations.add(document.originals.first())
                original.save()
            elif language_of_existing == orig_lang:
                # only an original exists. Create a bridge
                original = document.originals.first()
                document.originals.remove(original)
                document.save()

                intermediary = Document()
                intermediary.app = LATEIN
                intermediary.language = Language.objects.filter(
                    language_de=via_lang
                ).first()
                intermediary.ddc = document.ddc
                intermediary.save()
                intermediary.translations.add(document)
                intermediary.save()
                original.originals.add(intermediary)
                original.save()
            else:
                raise AssertionError("Original has neither orig nor via language")
            continue

        if document.originals.first().originals.count() > 1:
            print(document.title)
            continue

        # Assert the bridge has the via language
        assert document.originals.first().language.language_de == via_lang

        original = document.originals.first().originals.first()

        # Check if the original has the original language
        if original.language.language_de == orig_lang:
            # all good
            continue
        elif original.language.language_de == via_lang:
            # check if the original has a title
            if original.title:
                # we need to swap the original and the bridge
                intermediary = document.originals.first()
                document.originals.remove(intermediary)
                document.originals.add(original)
                intermediary.originals.remove(original)
                original.originals.add(intermediary)
                # fix the languages
                original.language = Language.objects.get(language_de=orig_lang)
                intermediary.language = Language.objects.get(language_de=via_lang)
                original.save()
                intermediary.save()
                document.save()
        else:
            raise AssertionError("Original has neither orig nor via language")


def unfix_intermediary_latein(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0137_latein_intermediary"),
    ]

    operations = [
        migrations.RunPython(fix_intermediary_latein, unfix_intermediary_latein)
    ]
