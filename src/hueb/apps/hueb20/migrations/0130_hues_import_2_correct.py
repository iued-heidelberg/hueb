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

                # translation
                translation = row[4].strip()
                if translation == "?" or translation == "":
                    translation = (
                        "Unbekannter Titel der Übersetzung von " + row[13].strip()
                    )

                # language_trans = row[5].strip()
                # if language_trans == "?":
                #    language_trans = None
                language_trans_obj = Language.objects.get(language_de="Deutsch")

                if (
                    not Document.objects.filter(app="HUES")
                    .filter(title=translation)
                    .filter(language=language_trans_obj)
                    .exists()
                ):
                    new_hues_document = Document()
                    new_hues_document.app = "HUES"
                    new_hues_document.tenant = huestenant
                    new_hues_document.title = translation

                    # year
                    year = row[3]

                    new_hues_document.written_in = parse_year(year)

                    new_hues_document.language = language_trans_obj
                    location = row[6]
                    if location is None or location == "" or location == "?":
                        pass
                    else:
                        new_hues_document.published_location = location

                    new_hues_document.save()
                new_hues_document = (
                    Document.objects.filter(app="HUES")
                    .filter(language=language_trans_obj)
                    .get(title=translation)
                )

                translators = [p.strip() for p in translators]
                for translator in translators:
                    if translator:
                        if translator == "?":
                            pass
                        else:
                            person = (
                                Person.objects.filter(name=translator).all().first()
                            )
                            if (
                                person
                                in Document.objects.filter(language=language_trans_obj)
                                .filter(app="HUES")
                                .get(title=translation)
                                .contributions.all()
                            ):
                                pass
                            else:
                                new_contribution = Contribution()
                                new_contribution.app = "HUES"
                                new_contribution.tenant = huestenant
                                new_contribution.contribution_type = "WRITER"
                                new_contribution.person = person
                                new_contribution.document = (
                                    Document.objects.filter(language=language_trans_obj)
                                    .filter(app="HUES")
                                    .get(title=translation)
                                )
                                new_contribution.save()
                if (
                    len(translators) > 0
                    and translators[0]
                    and translators[0] is not "?"
                ):
                    doc = (
                        Document.objects.filter(app="HUES")
                        .filter(language=language_trans_obj)
                        .get(title=translation)
                    )
                    doc.main_author = Person.objects.get(
                        name=sorted([t for t in translators if t and t is not "?"])[0]
                    )
                    doc.save()

                for index in [1, 8, 9, 19, 20]:
                    comment = row[index]
                    if comment:
                        new_comment = Comment()
                        new_comment.app = "HUES"
                        new_comment.tenant = huestenant
                        new_comment.text = comment
                        new_comment.external = True
                        new_comment.document = (
                            Document.objects.filter(language=language_trans_obj)
                            .filter(app="HUES")
                            .get(title=translation)
                        )
                        new_comment.save()

                publisher = row[7].strip()
                publisher = publisher.replace("u.", "/")
                publisher = publisher.replace(";", "/")
                publishers = publisher.split("/")
                publishers = [p.strip() for p in publishers]
                for publisher in publishers:
                    if publisher:
                        if publisher == "?":
                            pass
                        else:
                            person = Person.objects.filter(name=publisher).all().first()
                            new_contribution = Contribution()
                            new_contribution.app = "HUES"
                            new_contribution.tenant = huestenant
                            new_contribution.contribution_type = "PUBLISHER"
                            new_contribution.person = person
                            new_contribution.document = (
                                Document.objects.filter(language=language_trans_obj)
                                .filter(app="HUES")
                                .get(title=translation)
                            )
                            new_contribution.save()

                # filing - digitalization
                filing = row[10]
                new_filing = Filing()
                new_filing.app = "HUES"
                new_filing.tenant = huestenant
                if Archive.objects.filter(name="Online-Version").exists():
                    new_filing.archive = Archive.objects.get(name="Online-Version")
                new_filing.link = filing
                new_filing.document = (
                    Document.objects.filter(language=language_trans_obj)
                    .filter(app="HUES")
                    .get(title=translation)
                )
                try:
                    new_filing.save()
                except Exception:
                    raise Exception("Link is too long")

                # ORIGINALS
                author_org = row[11].strip()
                author_org = author_org.replace("u.", "/")
                author_org = author_org.replace(";", "/")
                authors_org = author_org.split("/")

                year_org = row[12]
                title_org = row[13].strip()
                if title_org == "?" or title_org == "":
                    title_org = "Unbekannter Titel des Originals von " + translation
                language_org = row[14].strip()
                if language_org == "?":
                    language_org = None
                language_org_obj = Language.objects.filter(
                    language_de=language_org
                ).first()

                # original document
                if (
                    not Document.objects.filter(app="HUES")
                    .filter(title=title_org)
                    .filter(language=language_org_obj)
                    .exists()
                ):
                    new_hues_original = Document()
                    new_hues_original.app = "HUES"
                    new_hues_original.tenant = huestenant
                    new_hues_original.title = title_org

                    # adjust year
                    new_hues_original.year = parse_year(year_org)

                    new_hues_original.language = language_org_obj
                    # new_hues_original.translations.add(Document.objects.get(
                    #    title=translation
                    # )) Do that only if no intermediary
                    new_hues_original.save()
                new_hues_original = (
                    Document.objects.filter(language=language_org_obj)
                    .filter(app="HUES")
                    .get(title=title_org)
                )

                authors_org = [p.strip() for p in authors_org]
                for author_org in authors_org:
                    # author
                    if author_org:
                        if author_org == "?":
                            pass
                        else:
                            person = (
                                Person.objects.filter(name=author_org).all().first()
                            )
                            if (
                                person
                                in Document.objects.filter(language=language_org_obj)
                                .filter(app="HUES")
                                .get(title=title_org)
                                .contributions.all()
                            ):
                                pass
                            else:
                                new_contribution = Contribution()
                                new_contribution.app = "HUES"
                                new_contribution.tenant = huestenant
                                new_contribution.contribution_type = "WRITER"
                                new_contribution.person = person
                                new_contribution.document = (
                                    Document.objects.filter(language=language_org_obj)
                                    .filter(app="HUES")
                                    .get(title=title_org)
                                )
                                new_contribution.save()
                if (
                    len(authors_org) > 0
                    and authors_org[0]
                    and authors_org[0] is not "?"
                ):
                    doc = (
                        Document.objects.filter(language=language_org_obj)
                        .filter(app="HUES")
                        .get(title=title_org)
                    )
                    doc.main_author = Person.objects.get(
                        name=sorted([t for t in authors_org if t and t is not "?"])[0]
                    )
                    doc.save()

                # INTERMEDIARY
                author_inter = row[15].strip()
                author_inter = author_inter.replace("u.", "/")
                author_inter = author_inter.replace(";", "/")
                authors_inter = author_inter.split("/")

                year_inter = row[16]
                title_inter = row[17].strip()
                if title_inter == "?" or title_inter == "":
                    title_inter = (
                        "Unbekannter Titel der Brückenübersetzung von " + title_org
                    )
                language_inter = row[18].strip()
                if language_inter == "?":
                    language_inter = None

                # intermediary translation
                if any([author_inter, year_inter, row[17].strip(), language_inter]):
                    if (
                        not Document.objects.filter(app="HUES")
                        .filter(title=title_inter)
                        .exists()
                    ):
                        new_hues_inter = Document()
                        new_hues_inter.app = "HUES"
                        new_hues_inter.tenant = huestenant
                        new_hues_inter.title = title_inter
                        new_hues_inter.year = parse_year(year_inter)
                        if language_inter:
                            if Language.objects.filter(
                                language_de=language_inter
                            ).exists():
                                new_hues_inter.language = Language.objects.get(
                                    language_de=language_inter
                                )
                        new_hues_inter.save()

                    new_hues_inter = Document.objects.filter(app="HUES").get(
                        title=title_inter
                    )
                    new_hues_inter.translations.add(
                        Document.objects.filter(language=language_trans_obj)
                        .filter(app="HUES")
                        .get(title=translation)
                    )
                    new_hues_inter.originals.add(
                        Document.objects.filter(language=language_org_obj)
                        .filter(app="HUES")
                        .get(title=title_org)
                    )
                    new_hues_inter.save()
                    authors_inter = [p.strip() for p in authors_inter]
                    for author_inter in authors_inter:
                        # author
                        if author_inter:
                            if author_inter == "?":
                                pass
                            else:
                                person = (
                                    Person.objects.filter(name=author_inter)
                                    .all()
                                    .first()
                                )
                                new_contribution = Contribution()
                                new_contribution.app = "HUES"
                                new_contribution.tenant = huestenant
                                new_contribution.contribution_type = "WRITER"
                                new_contribution.person = person
                                new_contribution.document = Document.objects.filter(
                                    app="HUES"
                                ).get(title=title_inter)
                                new_contribution.save()

                    if (
                        len(authors_inter) > 0
                        and authors_inter[0]
                        and authors_inter[0] is not "?"
                    ):
                        doc = Document.objects.filter(app="HUES").get(title=title_inter)
                        doc.main_author = Person.objects.get(
                            name=sorted(
                                [t for t in authors_inter if t and t is not "?"]
                            )[0]
                        )
                        doc.save()
                else:
                    hues_original = (
                        Document.objects.filter(language=language_org_obj)
                        .filter(app="HUES")
                        .get(title=title_org)
                    )
                    print(translation)
                    hues_translation = (
                        Document.objects.filter(language=language_trans_obj)
                        .filter(app="HUES")
                        .get(title=translation)
                    )
                    hues_original.translations.add(hues_translation)


def unload_hues_docs(apps, schema_editor):
    HUES = "HUES"
    Hues_comment = apps.get_model("hueb20", "Comment")
    Hues_comment.objects.filter(app=HUES).all().delete()
    Hues_document_relationship = apps.get_model("hueb20", "DocumentRelationship")
    Hues_document_relationship.objects.filter(document_from__app=HUES).filter(
        document_to__app=HUES
    ).all().delete()
    Hues_document = apps.get_model("hueb20", "Document")
    Hues_document.objects.filter(app=HUES).all().delete()
    Hues_Contribution = apps.get_model("hueb20", "Contribution")
    Hues_Contribution.objects.filter(app=HUES).all().delete()
    Hues_filing = apps.get_model("hueb20", "Filing")
    Hues_filing.objects.filter(app=HUES).all().delete()


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0129_hues_import_undo")]
    operations = [migrations.RunPython(load_hues_docs, unload_hues_docs)]
