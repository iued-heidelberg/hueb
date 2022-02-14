

from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
import re
from psycopg2.extras import NumericRange


def load_latein_translators(apps, schema_editor):
    Latein_translators = apps.get_model("hueb_legacy_latein", "TranslatorNew")
    Person = apps.get_model("hueb20", "Person")

    for latein_translator in Latein_translators.objects.all():
        if Person.objects.filter(name__iexact=latein_translator.name).exists():
            p = Person.objects.get(name__iexact=latein_translator.name)
            p.translator_ref = latein_translator
            p.save()
        else:
            new_translator = Person()
            # Set reference to old entries
            new_translator.translator_ref = latein_translator
            new_translator.app = LATEIN

            # transfer information
            name_with_year = latein_translator.name
            name_with_year = name_with_year.split(" (")
            year = None
            if len(name_with_year) > 1:
                name = " ".join(name_with_year[:-1])
                year = name_with_year[-1]
            else:
                name = "".join(name_with_year)
            if Person.objects.filter(name__iexact=name).exists():
                matches = Person.objects.filter(name__iexact=name).all()
                if len(matches) == 1:
                    match = matches[0]
                    match.translator_ref = latein_translator
                    match.save()
                continue
            new_translator.name = name

            #lifetime is taken from the name in the old model. Cases with Century are ignored.
            if year is not None:
                pattern = re.compile(r".*\d{4}-.*\d{4}")
                if pattern.search(year) is not None:
                    pattern = re.compile(r"\d{4}")
                    if len(re.findall(pattern, year)) == 2:
                        start, end = re.findall(pattern, year)
                    else:
                        start = re.findall(pattern, year)[0]
                        end = re.findall(pattern, year)[-1]
                else:
                    pattern = re.compile(r"geb\.\s\d{4}}")
                    start = pattern.search(year)
                    if start is not None:
                        pattern = re.compile(r"\d{4}")
                        start = pattern.search(year)
                        start = start[0]

                    pattern = re.compile(r"gest\.\s\d{4}}")
                    end = pattern.search(year)
                    if end is not None:
                        pattern = re.compile(r"\d{4}")
                        end = pattern.search(year)
                        end = end[0]

                if start is not None:
                    new_translator.lifetime_start = NumericRange(int(start), int(start) + 1)
                if end is not None:
                    new_translator.lifetime_end = NumericRange(int(end), int(end) + 1)

            # save new model
            new_translator.save()


def unload_latein_translators(apps, schema_editor):
    LateinTranslator = apps.get_model("hueb20", "Person")
    LateinTranslator.objects.filter(app=LATEIN).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0053_load_latein_authors"),
    ]

    operations = [migrations.RunPython(load_latein_translators, unload_latein_translators)]
