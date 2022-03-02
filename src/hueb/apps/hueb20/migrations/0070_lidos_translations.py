from django.db import migrations
from hueb.apps.hueb20.models import LIDOS
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace
from psycopg2.extras import NumericRange


import re


def load_lidos_translations(apps, schema_editor):
    OrigAssign = apps.get_model("hueb_legacy_lidos", "OrigAssign")
    Translations = apps.get_model("hueb_legacy_lidos", "Translation")
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    DDC = apps.get_model("hueb20", "DdcGerman")
    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")
    Comment = apps.get_model("hueb20", "Comment")

    for translation in Translations.objects.all():
        document = Document()
        # Set reference to old entries
        document.translation_ref_lidos = translation
        document.app = LIDOS
        document.title = translation.title

        if translation.subtitle is not None:
            document.subtitle = translation.subtitle

        if DDC.objects.filter(ddc_number=translation.ddc.ddc_number).exists():
            document.ddc = DDC.objects.get(ddc_number=translation.ddc.ddc_number)
        else:
            raise Exception("There is no ddc assigned to " + translation.ddc.ddc_name)

        if translation.real_year is not None:
            if translation.real_year == 0:
                if translation.year is not None and (
                    translation.year != ""
                    and "unbekannt" not in translation.year.lower()
                ):
                    try:
                        document.written_in = NumericRange(
                            int(translation.year), int(translation.year) + 1
                        )
                    except ValueError:
                        pass
            elif translation.real_year != 0:
                document.written_in = NumericRange(
                    translation.real_year, translation.real_year + 1
                )
        if (
            translation.published_location is not None
            and "unbekannt" not in translation.published_location.lower()
        ):
            document.published_location = translation.published_location

        document.edition = translation.edition

        if (
            translation.language is not None
            and translation.language.language is not None
            and translation.language.language != ""
        ):
            if Language.objects.filter(
                language__iexact=translation.language.language
            ).exists():
                lang = Language.objects.get(
                    language__iexact=translation.language.language
                )
                if lang.language != "" and lang.language is not None:
                    document.language = Language.objects.get(
                        language__iexact=translation.language.language
                    )
        # save new model
        document.save()

        if OrigAssign.objects.filter(translation=translation).exists():
            for orig_assign in OrigAssign.objects.filter(translation=translation).all():
                if (
                    orig_assign.original is not None
                    and Document.objects.filter(
                        original_ref_lidos=orig_assign.original
                    ).exists()
                ):
                    for original in Document.objects.filter(
                        original_ref_lidos=orig_assign.original
                    ).all():
                        document.originals.add(original)
        # save updated model
        document.save()

        if translation.publisher is not None and translation.publisher != "":
            publishers = translation.publisher.split(";")
            for publi in publishers:
                if publi != "":
                    if not Person.objects.filter(name__iexact=publi).exists():
                        if "unbekannt" not in publi.lower():
                            person = Person()
                            person.name = publi
                            person.publisherTranslation_ref_lidos = translation
                            person.app = LIDOS
                            person.save()

            for publi in publishers:
                if publi != "":
                    if Person.objects.filter(name__iexact=publi).exists():
                        try:
                            publ_pers = Person.objects.get(name__iexact=publi)
                            contribution = Contribution()
                            contribution.person = publ_pers
                            contribution.contribution_type = (
                                Contribution_Namespace.PUBLISHER
                            )
                            contribution.app = LIDOS
                            contribution.document = document
                            contribution.save()
                        except Exception:
                            print(
                                [
                                    p.name
                                    for p in Person.objects.filter(
                                        name__iexact=publi
                                    ).all()
                                ]
                            )
        if translation.comment != "" and translation.comment is not None:
            comment = Comment()
            comment.text = translation.comment
            comment.app = LIDOS
            comment.document = document
            comment.save()


def unload_lidos_translations(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Document.objects.filter(app=LIDOS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0069_lidos_originals"),
        # ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [
        migrations.RunPython(load_lidos_translations, unload_lidos_translations)
    ]
