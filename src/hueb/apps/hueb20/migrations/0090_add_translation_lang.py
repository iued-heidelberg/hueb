from django.db import migrations
from hueb.apps.hueb20.models import LEGACY


def add_translation_language(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    # german = Language.objects.get(language__iexact="deutsch")
    # Filter translations
    for document in (
        Document.objects.filter(app=LEGACY)
        .filter(translation_ref_legacy__isnull=False)
        .all()
    ):
        if (document.language is None) or (document.language.language == ""):
            document.language = Language.objects.get(language__iexact="deutsch")
        else:
            document.language_orig = document.language
            document.language = Language.objects.get(language__iexact="deutsch")
            document.save()


def remove_translation_language(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    for document in (
        Document.objects.filter(app=LEGACY)
        .filter(translation_ref_legacy__isnull=False)
        .all()
    ):
        document.language = document.language_orig
        document.language_orig = None


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0089_auto_20220317_0902"),
    ]

    operations = [
        migrations.RunPython(add_translation_language, remove_translation_language)
    ]
