# Generated by Django 3.0.5 on 2020-07-09 21:55

from django.db import migrations


def fill_cultural_circles(apps, schema_editor):
    apps.get_model("hueb20", "Document")
    DocumentRelationship = apps.get_model("hueb20", "DocumentRelationship")
    apps.get_model("hueb20", "CulturalCircle")
    Person = apps.get_model("hueb20", "Person")

    for person in Person.objects.all():
        circles = []
        for document in person.documents.filter().all():
            if (
                document.translations.exists() and not document.originals.exists()
            ) or DocumentRelationship.objects.filter(document_from=document).filter(
                document_to__isnull=True
            ).exists():
                # check if document is original to know for cetrain that we take an actual cc of the author not translator
                if (
                    person.contribution_set.filter(document=document)
                    .filter(contribution_type="WRITER")
                    .exists()
                ):
                    # ..add to circles
                    circles.append(document.cultural_circle)
        if not circles:
            print("circles list is empty")
        else:
            circle = max(set(circles), key=circles.count)
            person.cultural_circle = circle
            person.save()


def remove_cultural_circles(apps, schema_editor):
    Person = apps.get_model("hueb20", "Person")

    for person in Person.objects.all():
        person.cultural_circle = None


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0114_auto_20230118_1011"),
    ]

    operations = [
        migrations.RunPython(fill_cultural_circles, remove_cultural_circles),
    ]
