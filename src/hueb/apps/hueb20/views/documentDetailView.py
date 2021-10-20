from django.views.generic.detail import DetailView
from django import forms
from hueb.apps.hueb20.models import Document
from django.http import HttpResponse
import csv


class DocumentDetailView(DetailView):
    # specify the model to use
    model = Document
    template_name = "hueb20/document_details/detail_view.html"

    def download_csv(request, pk):
        document = Document.objects.get(id=pk)
        model_fields = document._meta.fields + document._meta.many_to_many
        field_names = [field.name for field in model_fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="export.csv"'

        # the csv writer
        writer = csv.writer(response, delimiter=";", dialect="excel")
        # Write a first row with header information
        writer.writerow(field_names)
        # Write data row
        values = []
        for field in field_names:
            value = getattr(document, field)
            if callable(value):
                try:
                    value = value() or ""
                except:
                    value = "Error retrieving value"
            if value is None:
                value = ""
            values.append(value)
        writer.writerow(values)

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
