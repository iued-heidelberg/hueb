from django.db import migrations


def remove_blank_spaces(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")

    # remove blank spaces in author names
    for doc in Document.objects.all():
        for author in doc.contribution_set.all():
            if (
                author is not None
                and author.person is not None
                and author.person.name is not None
            ):
                author.person.name = author.person.name.strip()
                author.person.save()


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0124_fill_main_author")]

    operations = [migrations.RunPython(remove_blank_spaces)]
