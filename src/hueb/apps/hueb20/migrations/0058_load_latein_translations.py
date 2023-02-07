# flake8: noqa
from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace
from psycopg2.extras import NumericRange


def load_latein_translations(apps, schema_editor):
    TranslationNew = apps.get_model("hueb_legacy_latein", "TranslationNew")
    OrigAssign = apps.get_model("hueb_legacy_latein", "OrigAssign")
    Document = apps.get_model("hueb20", "Document")
    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")
    Comment = apps.get_model("hueb20", "Comment")
    Language = apps.get_model("hueb20", "Language")
    DDC = apps.get_model("hueb20", "DdcGerman")
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")

    for latein_new_translation in TranslationNew.objects.all():
        if latein_new_translation is not None:
            if Document.objects.filter(translation_ref=latein_new_translation).exists():
                continue
            document = Document()
            document.translation_ref = latein_new_translation
            document.app = LATEIN

            # transfer information
            document.title = latein_new_translation.title

            if latein_new_translation.subtitle is not None:
                document.subtitle = latein_new_translation.subtitle

            if latein_new_translation.subtitle1 is not None:
                document.subtitle += "\n" + latein_new_translation.subtitle1

            if (
                latein_new_translation.published_location is not None
                and "unbekannt" not in latein_new_translation.published_location.lower()
            ):
                document.published_location = latein_new_translation.published_location

            document.edition = latein_new_translation.edition

            if latein_new_translation.real_year is not None:
                if latein_new_translation.real_year == 0:
                    if latein_new_translation.year is not None and (
                        latein_new_translation.year != ""
                        and "unbekannt" not in latein_new_translation.year.lower()
                    ):
                        try:
                            document.written_in = NumericRange(
                                int(latein_new_translation.year),
                                int(latein_new_translation.year) + 1,
                            )
                        except ValueError:
                            pass
                elif latein_new_translation.real_year != 0:
                    document.written_in = NumericRange(
                        latein_new_translation.real_year,
                        latein_new_translation.real_year + 1,
                    )

            if DDC.objects.filter(ddc_ref=latein_new_translation.ddc).exists():
                document.ddc = DDC.objects.get(ddc_ref=latein_new_translation.ddc)
            elif DDC.objects.filter(
                ddc_number=latein_new_translation.ddc.ddc_number
            ).exists():
                document.ddc = DDC.objects.get(
                    ddc_number=latein_new_translation.ddc.ddc_number
                )
            else:
                raise Exception(
                    "There is no ddc assigned to " + latein_new_translation.ddc.ddc_name
                )

            if Language.objects.filter(
                language_ref=latein_new_translation.language
            ).exists():
                document.language = Language.objects.filter(language__isnull=False).get(
                    language_ref=latein_new_translation.language
                )
            elif (
                latein_new_translation.language is not None
                and latein_new_translation.language.language != ""
                and latein_new_translation.language.language is not None
            ):
                raise Exception(
                    "There is no language assigned to " + latein_new_translation.id
                )

            if CulturalCircle.objects.filter(
                country_ref=latein_new_translation.country
            ).exists():
                if (
                    latein_new_translation.country is not None
                    and latein_new_translation.country.country != ""
                    and latein_new_translation.country.country is not None
                ):
                    document.cultural_circle = CulturalCircle.objects.get(
                        country_ref=latein_new_translation.country
                    )
            elif (
                latein_new_translation.country.country != ""
                and latein_new_translation.country is not None
            ):
                raise Exception(
                    "There is no country assigned to "
                    + latein_new_translation.country.country
                )

            # save new model
            document.save()

            if OrigAssign.objects.filter(trans_new=latein_new_translation).exists():
                for orig_assign in OrigAssign.objects.filter(
                    trans_new=latein_new_translation
                ).all():
                    if (
                        orig_assign.orig_new is not None
                        and Document.objects.filter(
                            original_ref=orig_assign.orig_new
                        ).exists()
                    ):
                        for original in Document.objects.filter(
                            original_ref=orig_assign.orig_new
                        ).all():
                            document.originals.add(original)

            document.save()

            # create new Person for document's publisher and new contribution with contribution_type = PUBLISHER
            if latein_new_translation.publisher is not None:
                publishers = latein_new_translation.publisher.split(";")
                for publi in publishers:
                    if not Person.objects.filter(name__iexact=publi).exists():
                        if "unbekannt" not in publi.lower():
                            person = Person()
                            person.name = publi
                            person.publisherTranslation_ref = latein_new_translation
                            person.app = LATEIN
                            person.save()

                for publi in publishers:
                    if Person.objects.filter(name__iexact=publi).exists():
                        contribution = Contribution()
                        contribution.person = Person.objects.get(name__iexact=publi)
                        contribution.contribution_type = (
                            Contribution_Namespace.PUBLISHER
                        )
                        contribution.app = LATEIN
                        contribution.document = document
                        contribution.save()

            if (
                latein_new_translation.comment != ""
                and latein_new_translation.comment is not None
            ):
                comment = Comment()
                comment.text = latein_new_translation.comment
                comment.app = LATEIN
                comment.document = document
                comment.save()


def unload_latein_translations(apps, schema_editor):
    apps.get_model("hueb20", "Document")
    # LateinTranslation.objects.filter(app=LATEIN).filter(translation_ref__isnull=False).delete()

    apps.get_model("hueb20", "Person")
    # PublisherPerson.objects.filter(app=LATEIN).filter(publisherTranslation_ref__isnull=False).delete()

    apps.get_model("hueb20", "Contribution")
    # ContributionPublisher.objects.filter(app=LATEIN).filter(contribution_type=Contribution_Namespace.PUBLISHER).exclude(document__get_document_type=LateinTranslation.ORIGINAL).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0057_auto_20211220_1341"),
        # ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [
        migrations.RunPython(load_latein_translations, unload_latein_translations)
    ]
