# flake8: noqa
import csv
import re

from django.db import migrations
from psycopg2.extras import NumericRange


def parse_year(year):
    # check if digit - digit pattern exists with regex
    year = year.strip().replace(".", "")
    if re.match(r"\d+-\d+", year):
        vchr = (
            "v.Chr." in year or "v. Chr." in year or "v.Chr" in year or "v. Chr" in year
        )
        start = year.strip().split("-")[0]
        end = year.strip().split("-")[1]
        end = "".join([s for s in end.split() if s.isdigit()])
        print(year)
        if vchr:
            start = "-" + start
            end = "-" + end
        numrange = NumericRange(int(start), int(end))
    else:
        vchr = (
            "v.Chr." in year or "v. Chr." in year or "v.Chr" in year or "v. Chr" in year
        )
        date = "".join([s for s in year.split() if s.isdigit()])
        if vchr:
            date = "-" + date
        if date == "" or date == "-":
            numrange = None
        else:
            numrange = NumericRange(int(date), int(date) + 1)
    return numrange


def load_hues_docs(apps, schema_editor):
    Person = apps.get_model("hueb20", "Person")
    Language = apps.get_model("hueb20", "Language")
    Comment = apps.get_model("hueb20", "Comment")
    Document = apps.get_model("hueb20", "Document")
    Contribution = apps.get_model("hueb20", "Contribution")
    Filing = apps.get_model("hueb20", "Filing")
    Archive = apps.get_model("hueb20", "Archive")
    Tenant = apps.get_model("tenants", "Tenant")
    huestenant = Tenant.objects.get(app="HUES")

    for file in [
        "./hueb/apps/hueb20/migrations/data/hues_import.csv",
        "./hueb/apps/hueb20/migrations/data/hues_import2.csv",
    ]:
        with open(file) as f:
            reader = csv.reader(f, delimiter=";", quotechar='"')
            next(reader)
            next(reader)
            for row in reader:
                # TRANSLATIONS

                # translator
                translator = row[2]
                translator = translator.strip()
                translator = translator.replace("u.", "/")
                translator = translator.replace(";", "/")
                translators = translator.split("/")
                translators = [t.strip() for t in translators]
                for translator in translators:
                    if translator:
                        if Person.objects.filter(name=translator).exists():
                            pass
                        elif translator == "?":
                            pass
                        elif not Person.objects.filter(name=translator).exists():
                            new_hues_author = Person()
                            new_hues_author.app = "HUES"
                            new_hues_author.tenant = huestenant
                            new_hues_author.name = translator
                            new_hues_author.save()

                publisher = row[7].strip()
                publisher = publisher.replace("u.", "/")
                publisher = publisher.replace(";", "/")
                publishers = publisher.split("/")
                publishers = [p.strip() for p in publishers]
                for p in publishers:
                    if publisher is None or publisher == "" or publisher == "?":
                        pass
                    elif p and not Person.objects.filter(name=p).exists():
                        new_contributor = Person()
                        new_contributor.app = "HUES"
                        new_contributor.tenant = huestenant
                        new_contributor.name = p
                        new_contributor.save()

                # ORIGINALS
                author_org = row[11].strip()
                author_org = author_org.replace("u.", "/")
                author_org = author_org.replace(";", "/")
                authors_org = author_org.split("/")
                authors_org = [a.strip() for a in authors_org]
                for author_org in authors_org:
                    # author
                    if author_org:
                        if Person.objects.filter(name=author_org).exists():
                            pass
                        elif author_org == "?":
                            pass
                        elif not Person.objects.filter(name=author_org).exists():
                            new_hues_author = Person()
                            new_hues_author.app = "HUES"
                            new_hues_author.tenant = huestenant
                            new_hues_author.name = author_org
                            new_hues_author.save()

                # INTERMEDIARY
                author_inter = row[15].strip()
                author_inter = author_inter.replace("u.", "/")
                author_inter = author_inter.replace(";", "/")
                authors_inter = author_inter.split("/")
                # intermediary translator
                authors_inter = [a.strip() for a in authors_inter]
                for author_inter in authors_inter:
                    if author_inter:
                        if Person.objects.filter(name=author_inter).exists():
                            pass
                        elif author_inter == "?":
                            pass
                        elif not Person.objects.filter(name=author_inter).exists():
                            new_hues_author = Person()
                            new_hues_author.app = "HUES"
                            new_hues_author.tenant = huestenant
                            new_hues_author.name = author_inter
                            new_hues_author.save()


def unload_hues_docs(apps, schema_editor):
    HUES = "HUES"
    Hues_authors = apps.get_model("hueb20", "Person")
    Hues_authors.objects.filter(app=HUES).all().delete()


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0126_trigram_extension")]
    operations = [migrations.RunPython(load_hues_docs, unload_hues_docs)]
