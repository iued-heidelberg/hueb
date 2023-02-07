from django.db import migrations


def create_reviews(apps, schema_editor):
    Archive = apps.get_model("hueb20", "Archive")
    Country = apps.get_model("hueb20", "Country")
    CulturalCircle = apps.get_model("hueb20", "CulturalCircle")
    DdcGerman = apps.get_model("hueb20", "DdcGerman")
    Document = apps.get_model("hueb20", "Document")
    Filing = apps.get_model("hueb20", "Filing")
    Language = apps.get_model("hueb20", "Language")
    Person = apps.get_model("hueb20", "Person")

    models = [
        (Archive, "archive"),
        (Country, "country"),
        (CulturalCircle, "cultural_circle"),
        (DdcGerman, "ddc_german"),
        (Document, "document"),
        (Filing, "filing"),
        (Language, "language"),
        (Person, "person"),
    ]

    Review = apps.get_model("hueb20", "Review")

    for model, reference_name in models:
        reviews = []
        for inst in model.objects.all():
            rev = Review()
            setattr(rev, reference_name, inst)
            reviews.append(rev)

        Review.objects.bulk_create(reviews)


def uncreate_reviews(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0035_historicalreview_review"),
    ]

    operations = [migrations.RunPython(create_reviews, uncreate_reviews)]
