import csv

from django.http import HttpResponse
from django.views.generic.detail import DetailView
from hueb.apps.hueb20.models import Document


class DocumentDetailView(DetailView):
    # specify the model to use
    model = Document
    template_name = "hueb20/document_details/detail_view.html"

    def download_csv(request, pk):
        document = Document.objects.get(id=pk)

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="export.csv"'

        # the csv writer
        writer = csv.writer(
            response, delimiter=";", dialect="excel", quoting=csv.QUOTE_ALL
        )
        # Write a first row with header information
        writer.writerow(
            [
                "Titel",
                "Intertitel",
                "Ausgabe",
                "Jahr",
                "Originalsprache",
                "Sprache",
                "Kulturkreis",
                "Autor",
                "Übersetzer",
                "Verlag",
                "Erscheinungsort",
                "DDC",
                "Standorte",
                "Orginaltitel",
            ]
        )
        writer.writerow(
            [
                document.title if document.title != "" else "-",
                document.subtitle if document.subtitle != "" else "-",
                document.edition if document.edition != "" else "-",
                document.serialize_written_in()
                if not document.serialize_written_in() is None
                else "-",
                document.get_language()
                if document.get_language() != ""
                else "-",  # ORIGINAL!
                document.get_language() if document.get_language() != "" else "-",
                document.cultural_circle if document.cultural_circle != "" else "-",
                ", ".join(
                    [
                        author.person.name
                        for author in document.get_original_attr("get_authors")
                    ]
                )
                if document.get_original_attr("get_authors")
                else "-",  # original authors repair!
                ", ".join([authors.person.name for authors in document.get_authors()])
                if document.get_authors().exists()
                else "-",  # evtl Translators
                ", ".join(
                    [publishers.person.name for publishers in document.get_publishers()]
                )
                if document.get_publishers().exists()
                else "-",
                document.published_location
                if document.published_location != ""
                else "-",
                document.ddc if document.ddc != "" else "-",
                ", ".join([filing.archive.name for filing in document.get_filings()])
                if document.get_filings().exists()
                else "-",
                ", ".join([title for title in document.get_original_attr("title")])
                if document.get_original_attr("title")
                else "-",
            ]
        )

        return response

    def download_bib(request, pk):
        document = Document.objects.get(id=pk)

        # Written in
        writtenIn = ""
        if not document.written_in.isempty:
            writtenIn = str(document.written_in.lower)

        content = (
            "@misc{"
            + document.get_authors().get().person.name.split(",")[0].lower()
            + writtenIn
            + ",\n"
        )

        # Title
        content += '\t title \t= "' + document.title + '" ,\n'
        content += (
            '\t author \t= "'
            + " and\n".join(document.get_contributor_names("WRITER"))
            + '" ,\n'
        )
        content += '\t year \t= "' + writtenIn + '" ,\n'
        content += '\t address \t= "' + document.published_location + '" ,\n'
        content += (
            '\t publisher \t= "'
            + " and ".join(document.get_contributor_names("PUBLISHER"))
            + '" ,\n'
        )
        content += '\t language \t= "' + str(document.language) + '" ,\n'
        content += "}"

        response = HttpResponse(content, content_type="text/bibtex")
        response["Content-Disposition"] = 'attachment; filename="export.bib"'
        return response
