# flake8: noqa
from django.db import migrations
from hueb.apps.hueb20.models import LEGACY
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace
from psycopg2.extras import NumericRange


def load_legacy_originals(apps, schema_editor):
    Legacy_Originals = apps.get_model("hueb_legacy", "Original")
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    DDC = apps.get_model("hueb20", "DdcGerman")
    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")
    Comment = apps.get_model("hueb20", "Comment")

    for legacy_original in Legacy_Originals.objects.all():
        document = Document()
        # Set reference to old entries
        document.original_ref_legacy = legacy_original
        document.app = LEGACY
        if legacy_original.title is None:
            continue
        document.title = legacy_original.title

        if legacy_original.subtitle is not None:
            document.subtitle = legacy_original.subtitle

        if DDC.objects.filter(ddc_number=legacy_original.ddc.ddc_number).exists():
            document.ddc = DDC.objects.get(ddc_number=legacy_original.ddc.ddc_number)
        else:
            raise Exception(
                "There is no ddc assigned to " + legacy_original.ddc.ddc_name
            )

        if legacy_original.real_year is not None:
            if legacy_original.real_year == 0:
                if legacy_original.year is not None and (
                    legacy_original.year != ""
                    and "unbekannt" not in legacy_original.year.lower()
                ):
                    try:
                        document.written_in = NumericRange(
                            int(legacy_original.year), int(legacy_original.year) + 1
                        )
                    except ValueError:
                        pass
            elif legacy_original.real_year != 0:
                document.written_in = NumericRange(
                    legacy_original.real_year, legacy_original.real_year + 1
                )
        if (
            legacy_original.published_location is not None
            and "unbekannt" not in legacy_original.published_location.lower()
        ):
            document.published_location = legacy_original.published_location

        document.edition = legacy_original.edition

        if (
            legacy_original.language is not None
            and legacy_original.language.language is not None
            and legacy_original.language.language != ""
        ):
            if Language.objects.filter(
                language__iexact=legacy_original.language.language
            ).exists():
                lang = Language.objects.get(
                    language__iexact=legacy_original.language.language
                )
                if lang.language != "" and lang.language is not None:
                    document.language = Language.objects.get(
                        language__iexact=legacy_original.language.language
                    )

        document.save()

        if legacy_original.publisher is not None and legacy_original.publisher != "":
            publishers = legacy_original.publisher.split(";")
            for publi in publishers:
                if publi != "":
                    if not Person.objects.filter(name__iexact=publi).exists():
                        if "unbekannt" not in publi.lower():
                            person = Person()
                            person.name = publi
                            person.publisherOriginal_ref_legacy = legacy_original
                            person.app = LEGACY
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
                            contribution.app = LEGACY
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
        if legacy_original.comment != "" and legacy_original.comment is not None:
            comment = Comment()
            comment.text = legacy_original.comment
            comment.app = LEGACY
            comment.document = document
            comment.save()


def unload_legacy_originals(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    DocumentRelationship = apps.get_model("hueb20", "DocumentRelationship")
    DocumentRelationship.objects.filter(document_from__app=LEGACY).delete()
    DocumentRelationship.objects.filter(document_to__app=LEGACY).delete()
    Document.objects.filter(app=LEGACY).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0074_legacy_translators"),
        # ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [migrations.RunPython(load_legacy_originals, unload_legacy_originals)]
