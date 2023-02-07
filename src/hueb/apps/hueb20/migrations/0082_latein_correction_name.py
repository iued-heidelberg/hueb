from django.db import migrations
from hueb.apps.hueb20.models import LATEIN


def correct_persons(apps, schema_editor):
    Person = apps.get_model("hueb20", "Person")
    # Latein_authors = apps.get_model("hueb_legacy_latein", "AuthorNew")
    # Latein_translators = apps.get_model("hueb_legacy_latein", "TranslatorNew")

    for person in Person.objects.filter(app=LATEIN).filter(name__icontains=")").all():
        if person.name[-1] == ")":
            if person.translator_ref:
                latein_name = person.translator_ref.name
            elif person.author_ref:
                latein_name = person.author_ref.name
            else:
                continue
            idx = latein_name.rfind(person.name[-3:])
            person.name = latein_name[: idx + 3]
            person.save()


def uncorrect_persons(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0081_legacy_filings"),
        # ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(correct_persons, uncorrect_persons)]
