from django.db import migrations
from hueb.apps.hueb20.models import LIDOS
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace
from psycopg2.extras import NumericRange


import re


def load_lidos_originals(apps, schema_editor):
    Originals = apps.get_model("hueb_legacy_lidos", "Original")
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    DDC = apps.get_model("hueb20", "DdcGerman")
    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")
    Comment = apps.get_model("hueb20", "Comment")

    for original in Originals.objects.all():
        document = Document()
        # Set reference to old entries
        document.original_ref_lidos = original
        document.app = LIDOS
        document.title = original.title

        if original.subtitle is not None:
            document.subtitle = original.subtitle

        if DDC.objects.filter(ddc_number=original.ddc.ddc_number).exists():
            document.ddc = DDC.objects.get(ddc_number=original.ddc.ddc_number)
        else:
            raise Exception("There is no ddc assigned to " + original.ddc.ddc_name)

        if original.real_year is not None:
            if original.real_year == 0:
                if original.year is not None and (
                    original.year != "" and "unbekannt" not in original.year.lower()
                ):
                    try:
                        document.written_in = NumericRange(
                            int(original.year), int(original.year) + 1
                        )
                    except ValueError:
                        pass
            elif original.real_year != 0:
                document.written_in = NumericRange(
                    original.real_year, original.real_year + 1
                )
        if (
            original.published_location is not None
            and "unbekannt" not in original.published_location.lower()
        ):
            document.published_location = original.published_location

        document.edition = original.edition

        if (
            original.language is not None
            and original.language.language is not None
            and original.language.language != ""
        ):
            if Language.objects.filter(
                language__iexact=original.language.language
            ).exists():
                lang = Language.objects.get(language__iexact=original.language.language)
                if lang.language != "" and lang.language is not None:
                    document.language = Language.objects.get(
                        language__iexact=original.language.language
                    )

        document.save()

        if original.publisher is not None and original.publisher != "":
            publishers = original.publisher.split(";")
            for publi in publishers:
                if publi != "":
                    if not Person.objects.filter(name__iexact=publi).exists():
                        if "unbekannt" not in publi.lower():
                            person = Person()
                            person.name = publi
                            person.publisherOriginal_ref_lidos = original
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
        if original.comment != "" and original.comment is not None:
            comment = Comment()
            comment.text = original.comment
            comment.app = LIDOS
            comment.document = document
            comment.save()


def unload_lidos_originals(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Document.objects.filter(app=LIDOS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0068_lidos_translators"),
        # ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [migrations.RunPython(load_lidos_originals, unload_lidos_originals)]
