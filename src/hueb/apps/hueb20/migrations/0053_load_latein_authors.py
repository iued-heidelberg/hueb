from django.db import migrations
from hueb.apps.hueb20.models import LATEIN
import re
from psycopg2.extras import NumericRange


def load_latein_authors(apps, schema_editor):
    Latein_authors = apps.get_model("hueb_legacy_latein", "AuthorNew")
    Person = apps.get_model("hueb20", "Person")

    for latein_author in Latein_authors.objects.all():
        if Person.objects.filter(name__iexact=latein_author.name).exists():
            p = Person.objects.get(name__iexact=latein_author.name)
            p.author_ref = latein_author
            p.save()

        else:
            new_author = Person()
            # Set reference to old entries
            new_author.author_ref = latein_author
            new_author.app = LATEIN

            # transfer information#
            name_with_year = latein_author.name
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
                    match.author_ref = latein_author
                    match.save()
                continue
            new_author.name = name

            # lifetime is taken from the name in the old model. Cases with Century are ignored.
            if year is not None:
                pattern = re.compile(r".*\d{4}-.*\d{4}")
                if pattern.search(year) is not None:
                    pattern = re.compile(r"\d{4}")
                    years = re.findall(pattern, year)
                    if len(years) == 2:
                        start, end = years
                    else:
                        start = years[0]
                        end = years[-1]
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
                    new_author.lifetime_start = NumericRange(int(start), int(start) + 1)
                if end is not None:
                    new_author.lifetime_end = NumericRange(int(end), int(end) + 1)

            # save new model
            new_author.save()


def unload_latein_authors(apps, schema_editor):
    LateinAuthor = apps.get_model("hueb20", "Person")
    LateinAuthor.objects.filter(app=LATEIN).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "00541_auto_20220214_1127"),
        # ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_latein_authors, unload_latein_authors)]
