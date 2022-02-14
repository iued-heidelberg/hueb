from django.db import migrations
from hueb.apps.hueb20.models import LATEIN


def update_cultural_circle_refs(apps, schema_editor):
    Country_legacy = apps.get_model("hueb_legacy_latein", "Country")
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")

    for legacy_country in Country_legacy.objects.all():
        if legacy_country.country == "":
            continue
        if CulturalCircle.objects.filter(name__iexact=legacy_country.country).exists():
            circle = CulturalCircle.objects.get(name__iexact=legacy_country.country)
            circle.country_ref = legacy_country
            circle.save()
        else:
            raise Exception("No Matching CulturalCircle for" + legacy_country.country)


def un_update_cultural_circle_refs(apps, schema_editor):
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")
    CulturalCircle.objects.country_ref = None


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0063_historicalculturalcircle_country_ref"),
    ]

    operations = [
        migrations.RunPython(
            update_cultural_circle_refs, un_update_cultural_circle_refs
        )
    ]
