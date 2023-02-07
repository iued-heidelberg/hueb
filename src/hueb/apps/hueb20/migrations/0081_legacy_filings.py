import re

from django.db import migrations
from hueb.apps.hueb20.models import LEGACY


def load_filings(apps, schema_editor):
    Legacy_LocAssign = apps.get_model("hueb_legacy", "LocAssign")
    apps.get_model("hueb_legacy", "Location")
    Filing = apps.get_model("hueb20", "Filing")
    Document = apps.get_model("hueb20", "Document")
    Archive = apps.get_model("hueb20", "Archive")
    apps.get_model("hueb20", "Country")

    for legacy_loc_assign in Legacy_LocAssign.objects.all():
        new_filing = Filing()
        # Set reference to old entries
        new_filing.locAssign_legacy_ref = legacy_loc_assign
        new_filing.app = LEGACY

        # transfer information
        if Archive.objects.filter(
            name__iexact=legacy_loc_assign.location.name.strip()
        ).exists():
            new_filing.archive = Archive.objects.get(
                name__iexact=legacy_loc_assign.location.name.strip()
            )
        elif Archive.objects.filter(
            name__icontains=legacy_loc_assign.location.name.strip()
        ).exists():
            new_filing.archive = Archive.objects.get(
                name__icontains=legacy_loc_assign.location.name.strip()
            )

        elif (
            Archive.objects.filter(
                hostname__iexact=legacy_loc_assign.location.hostname
            ).exists()
            and legacy_loc_assign.location.hostname is not None
            and legacy_loc_assign.location.hostname != ""
        ):
            try:
                new_filing.archive = Archive.objects.get(
                    hostname__iexact=legacy_loc_assign.location.hostname
                )
            except Exception:
                print(
                    "Multiple candidates: ",
                    Archive.objects.filter(
                        hostname__iexact=legacy_loc_assign.location.hostname
                    ).all(),
                )
        elif (
            Archive.objects.filter(
                adress__iexact=legacy_loc_assign.location.adress
            ).exists()
            and legacy_loc_assign.location.adress is not None
            and legacy_loc_assign.location.adress != ""
        ):
            try:
                new_filing.archive = Archive.objects.get(
                    adress__iexact=legacy_loc_assign.location.adress
                )
            except Exception:
                new_filing.archive = Archive.objects.filter(
                    adress__iexact=legacy_loc_assign.location.adress
                ).first()

        else:
            found_archive = False
            name_words = re.split(r"\W", legacy_loc_assign.location.name)
            name_words = [re.sub(r"[\W]+", "", word) for word in name_words]
            name_words = [word for word in name_words if word != ""]

            if all(
                Archive.objects.filter(name__icontains=word).exists()
                for word in name_words
            ):
                matching_archives = []
                for word in name_words:
                    matching_archives.append(
                        set(Archive.objects.filter(name__icontains=word).all())
                    )
                intersect = matching_archives[0].intersection(*matching_archives[1:])
                if len(intersect) == 1:
                    arch = intersect.pop()
                    new_filing.archive = arch
                    found_archive = True
                    # print("\nMatched " + legacy_loc_assign.location.name + " to " + arch.name)
                elif len(intersect) > 1:
                    arch = sorted(list(intersect), key=lambda x: len(x.name))[0]
                    new_filing.archive = arch
                    found_archive = True
                    print(
                        "\nChose " + arch.name + " out of ",
                        [x.name for x in list(intersect)],
                    )

            if (
                found_archive == False and legacy_loc_assign.location is not None
            ):  # stupid solution cause a lots new bibs that exists with different names :/
                print("Nothing found for: ", name_words)

        new_filing.signatur = legacy_loc_assign.signatur

        assert (legacy_loc_assign.original is not None) or (
            legacy_loc_assign.translation is not None
        )

        if (
            legacy_loc_assign.original is not None
            and legacy_loc_assign.original.title != ""
            and legacy_loc_assign.original.title is not None
        ):
            d = Document.objects.get(original_ref_legacy=legacy_loc_assign.original)
            new_filing.document = d
            # save new model
            new_filing.save()
            d.filing_set.add(new_filing)
            d.save()
        elif (
            legacy_loc_assign.translation is not None
            and legacy_loc_assign.translation.title != ""
            and legacy_loc_assign.translation.title is not None
        ):
            d = Document.objects.get(
                translation_ref_legacy=legacy_loc_assign.translation
            )
            new_filing.document = d
            # save new model
            new_filing.save()
            d.filing_set.add(new_filing)
            d.save()


def unload_filings(apps, schema_editor):
    Filing = apps.get_model("hueb20", "Filing")
    Filing.objects.filter(app=LEGACY).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0080_legacy_archive"),
        # ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_filings, unload_filings)]
