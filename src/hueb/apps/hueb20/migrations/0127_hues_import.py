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
                if translator:
                    if Person.objects.filter(name=translator).exists():
                        pass
                    elif translator == "":
                        pass
                    elif translator == "?":
                        pass
                    elif not Person.objects.filter(name=translator).exists():
                        new_hues_author = Person()
                        new_hues_author.app = "HUES"
                        new_hues_author.tenant = huestenant
                        new_hues_author.name = translator
                        new_hues_author.save()

                # translation
                translation = row[4]
                new_hues_document = Document()
                new_hues_document.app = "HUES"
                new_hues_document.tenant = huestenant
                new_hues_document.title = translation
                if translator == "":
                    pass
                elif translator == "?":
                    pass
                else:
                    new_hues_document.author = Person.objects.get(name=translator)

                # year
                year = row[3]

                new_hues_document.written_in = parse_year(year)

                language_trans = row[5].strip()
                if language_trans == "?":
                    language_trans = None
                if language_trans:
                    print(language_trans)
                    new_hues_document.language = Language.objects.get(
                        language_de=language_trans
                    )
                location = row[6]
                if location is None or location == "" or location == "?":
                    pass
                else:
                    new_hues_document.published_location = location

                new_hues_document.save()

                for index in [1, 8, 9, 19, 20]:
                    comment = row[index]
                    if comment:
                        new_comment = Comment()
                        new_comment.app = "HUES"
                        new_comment.tenant = huestenant
                        new_comment.text = comment
                        new_comment.external = True
                        new_comment.document = new_hues_document
                        new_comment.save()

                publisher = row[7]
                if publisher is None or publisher == "" or publisher == "?":
                    pass
                else:
                    publisher = publisher.replace("u.", "/")
                    publishers = publisher.split("/")
                    for p in publishers:
                        if p and not Person.objects.filter(name=p).exists():
                            new_contributor = Person()
                            new_contributor.app = "HUES"
                            new_contributor.tenant = huestenant
                            new_contributor.name = p
                            new_contributor.save()
                        if p:
                            person = Person.objects.filter(name=p).all().first()
                            new_contribution = Contribution()
                            new_contribution.app = "HUES"
                            new_contribution.tenant = huestenant
                            new_contribution.contribution_type = "PUBLISHER"
                            new_contribution.person = person
                            new_contribution.document = new_hues_document
                            new_contribution.save()

                # filing - digitalization
                filing = row[10]
                new_filing = Filing()
                new_filing.app = "HUES"
                new_filing.tenant = huestenant
                new_filing.archive = Archive.objects.get(name="Online-Version")
                new_filing.link = filing
                new_filing.document = new_hues_document
                try:
                    new_filing.save()
                except Exception:
                    raise Exception("Link is too long")

                # ORIGINALS
                author_org = row[11]
                year_org = row[12]
                title_org = row[13]
                language_org = row[14].strip()
                if language_org == "?":
                    language_org = None

                # author

                if author_org:
                    if Person.objects.filter(name=author_org).exists():
                        pass
                    elif author_org == "":
                        pass
                    elif author_org == "?":
                        pass
                    elif not Person.objects.filter(name=author_org).exists():
                        new_hues_author = Person()
                        new_hues_author.app = "HUES"
                        new_hues_author.tenant = huestenant
                        new_hues_author.name = author_org
                        new_hues_author.save()

                # original document
                new_hues_original = Document()
                new_hues_original.app = "HUES"
                new_hues_original.tenant = huestenant
                new_hues_original.title = title_org
                new_hues_original.author = new_hues_author
                # adjust year
                new_hues_original.year = parse_year(year_org)

                if language_org:
                    print(language_org)
                    new_hues_original.language = Language.objects.get(
                        language_de=language_org
                    )
                new_hues_original.translation = new_hues_document
                new_hues_original.save()

                # INTERMEDIARY
                author_inter = row[15]
                year_inter = row[16]
                title_inter = row[17]
                language_inter = row[18].strip()
                if language_inter == "?":
                    language_inter = None

                # intermediary translator
                if author_inter:
                    if Person.objects.filter(name=author_inter).exists():
                        pass
                    elif author_inter == "":
                        pass
                    elif author_inter == "?":
                        pass
                    elif not Person.objects.filter(name=author_inter).exists():
                        new_hues_author = Person()
                        new_hues_author.app = "HUES"
                        new_hues_author.tenant = huestenant
                        new_hues_author.name = author_inter
                        new_hues_author.save()

                # intermediary translation
                if any([author_inter, year_inter, title_inter, language_inter]):
                    new_hues_inter = Document()
                    new_hues_inter.app = "HUES"
                    new_hues_inter.tenant = huestenant
                    new_hues_inter.title = title_inter
                    new_hues_inter.author = author_inter
                    new_hues_inter.year = parse_year(year_inter)
                    if language_inter:
                        new_hues_inter.language = Language.objects.get(
                            language_de=language_inter
                        )
                    new_hues_inter.translation = new_hues_document
                    new_hues_inter.original = new_hues_original
                    new_hues_inter.save()


def unload_hues_docs(apps, schema_editor):
    HUES = "HUES"
    Hues_authors = apps.get_model("hueb20", "Person")
    Hues_authors.objects.filter(app=HUES).all().delete()
    Hues_comment = apps.get_model("hueb20", "Comment")
    Hues_comment.objects.filter(app=HUES).all().delete()
    Hues_document = apps.get_model("hueb20", "Document")
    Hues_document.objects.filter(app=HUES).all().delete()
    Hues_Contribution = apps.get_model("hueb20", "Contribution")
    Hues_Contribution.objects.filter(app=HUES).all().delete()
    Hues_filing = apps.get_model("hueb20", "Filing")
    Hues_filing.objects.filter(app=HUES).all().delete()


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0126_trigram_extension")]
    operations = [migrations.RunPython(load_hues_docs, unload_hues_docs)]
