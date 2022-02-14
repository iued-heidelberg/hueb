from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
from hueb.apps.hueb20.models.contribution import Contribution as Contribution_Namespace
from psycopg2.extras import NumericRange
import re


def load_latein_originals(apps, schema_editor):
    Latein_originals = apps.get_model("hueb_legacy_latein", "OriginalNew")
    Document = apps.get_model("hueb20", "Document")
    Contribution = apps.get_model("hueb20", "Contribution")
    Person = apps.get_model("hueb20", "Person")
    Comment = apps.get_model("hueb20", "Comment")
    Language = apps.get_model("hueb20", "Language")
    DDC = apps.get_model("hueb20", "DdcGerman")
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")

    for latein_original in Latein_originals.objects.all():
        if latein_original is not None:
            if Document.objects.filter(original_ref=latein_original).exists():
                continue
            original = Document()
            # Set reference to old entries
            original.original_ref = latein_original
            original.app = LATEIN

            # transfer information
            original.title = latein_original.title
            if latein_original.subtitle is not None:
                original.subtitle = latein_original.subtitle
            if latein_original.subtitle1 is not None:
                original.subtitle += "\n" + latein_original.subtitle1
            original.edition = latein_original.edition
            if (
                latein_original.published_location is not None
                and "unbekannt" not in latein_original.published_location.lower()
            ):
                original.published_location = latein_original.published_location

            if latein_original.real_year is not None:
                if latein_original.real_year == 0:
                    if latein_original.year is not None and (
                        latein_original.year != ""
                        and "unbekannt" not in latein_original.year.lower()
                    ):
                        try:
                            original.written_in = NumericRange(
                                int(latein_original.year), int(latein_original.year) + 1
                            )
                        except ValueError:
                            pass
                elif latein_original.real_year != 0:
                    original.written_in = NumericRange(
                        latein_original.real_year, latein_original.real_year + 1
                    )

            if DDC.objects.filter(ddc_ref=latein_original.ddc).exists():
                original.ddc = DDC.objects.get(ddc_ref=latein_original.ddc)
            elif DDC.objects.filter(ddc_number=latein_original.ddc.ddc_number).exists():
                original.ddc = DDC.objects.get(
                    ddc_number=latein_original.ddc.ddc_number
                )
            else:
                raise Exception(
                    "There is no ddc assigned to " + latein_original.ddc.ddc_name
                )

            if Language.objects.filter(language_ref=latein_original.language).exists():
                lang = Language.objects.get(language_ref=latein_original.language)
                if lang.language != "" and lang.language is not None:
                    original.language = Language.objects.get(
                        language_ref=latein_original.language
                    )
            elif (
                latein_original.language is not None
                and latein_original.language.language != ""
                and latein_original.language.language is not None
            ):
                raise Exception(
                    "There is no language assigned to "
                    + latein_original.language.language
                )

            if CulturalCircle.objects.filter(
                country_ref=latein_original.country
            ).exists():
                if (
                    latein_original.country is not None
                    and latein_original.country.country != ""
                    and latein_original.country.country is not None
                ):
                    original.cultural_circle = CulturalCircle.objects.get(
                        country_ref=latein_original.country
                    )
            elif (
                latein_original.country is not None
                and latein_original.country.country != ""
                and latein_original.country.country is not None
            ):
                raise Exception(
                    "There is no country assigned to " + latein_original.country.country
                )

            # save new model
            original.save()
            # create new Person for document's publisher and new contribution with contribution_type = PUBLISHER
            if latein_original.publisher is not None:
                publishers = latein_original.publisher.split(";")
                for publi in publishers:
                    if not Person.objects.filter(name__iexact=publi).exists():
                        if "unbekannt" not in publi.lower():
                            person = Person()
                            person.name = publi
                            person.publisherOriginal_ref = latein_original
                            person.app = LATEIN
                            person.save()

                for publi in publishers:
                    if Person.objects.filter(name__iexact=publi).exists():
                        try:
                            publ_pers = Person.objects.get(name__iexact=publi)
                        except Exception:
                            print(
                                [
                                    p.name
                                    for p in Person.objects.filter(
                                        name__iexact=publi
                                    ).all()
                                ]
                            )
                        contribution = Contribution()
                        contribution.person = publ_pers
                        contribution.contribution_type = (
                            Contribution_Namespace.PUBLISHER
                        )
                        contribution.app = LATEIN
                        contribution.document = original
                        contribution.save()

            if latein_original.comment != "" and latein_original.comment is not None:
                comment = Comment()
                comment.text = latein_original.comment
                comment.app = LATEIN
                comment.document = original
                comment.save()


def unload_latein_originals(apps, schema_editor):
    LateinOriginal = apps.get_model("hueb20", "Document")
    # LateinOriginal.objects.filter(app=LATEIN).delete()
    PublisherPerson = apps.get_model("hueb20", "Person")
    # PublisherPerson.objects.filter(app=LATEIN).filter(publisherOriginal_ref__isnull=False).delete()
    ContributionPublisher = apps.get_model("hueb20", "Contribution")
    # ContributionPublisher.objects.filter(app=LATEIN).filter(contribution_type=Contribution_Namespace.PUBLISHER).exclude(document__get_document_type=LateinTranslation.TRANSLATION).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0054_load_latein_translators"),
        # ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_latein_originals, unload_latein_originals)]
