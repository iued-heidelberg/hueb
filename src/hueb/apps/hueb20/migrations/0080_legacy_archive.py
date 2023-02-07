import re

from django.db import migrations
from hueb.apps.hueb20.models import LEGACY


def load_archives(apps, schema_editor):
    Legacy_Location = apps.get_model("hueb_legacy", "Location")
    Archive = apps.get_model("hueb20", "Archive")
    Country = apps.get_model("hueb20", "Country")

    for legacy_location in Legacy_Location.objects.all():
        # transfer information
        if Archive.objects.filter(name__iexact=legacy_location.name.strip()).exists():
            continue
        elif Archive.objects.filter(
            name__icontains=legacy_location.name.strip()
        ).exists():
            continue
        elif (
            Archive.objects.filter(hostname__iexact=legacy_location.hostname).exists()
            and legacy_location.hostname is not None
            and legacy_location.hostname != ""
        ):
            continue
        elif (
            Archive.objects.filter(adress__iexact=legacy_location.adress).exists()
            and legacy_location.adress is not None
            and legacy_location.adress != ""
        ):
            continue
        else:
            name_words = re.split(r"\W", legacy_location.name)
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
                if len(intersect) > 0:
                    continue

            if (
                legacy_location.name is not None and legacy_location.name != ""
            ):  # stupid solution cause a lots new bibs that exists with different names :/
                print("Nothing found for: ", name_words)
                archive = Archive()
                archive.name = legacy_location.name
                archive.adress = legacy_location.adress
                if not Country.objects.filter(
                    country=legacy_location.country.country
                ).exists():
                    print("No country called: " + legacy_location.country.country)
                else:
                    archive.country = Country.objects.get(
                        country=legacy_location.country.country
                    )
                archive.hostname = legacy_location.hostname
                archive.ip = legacy_location.ip
                archive.z3950_gateway = legacy_location.z3950_gateway
                archive.app = LEGACY
                archive.save()


def unload_archives(apps, schema_editor):
    Archive = apps.get_model("hueb20", "Archive")
    Archive.objects.filter(app=LEGACY).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0079_auto_20220227_1623"),
        # ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_archives, unload_archives)]
