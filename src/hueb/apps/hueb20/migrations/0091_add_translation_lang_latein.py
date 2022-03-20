from django.db import migrations, DataError
from hueb.apps.hueb20.models import LATEIN


def add_translation_language(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    german = Language.objects.get(language__iexact="deutsch")

    # Filter translations
    for document in (
        Document.objects.filter(app=LATEIN).filter(translation_ref__isnull=False).all()
    ):
        if (document.language is None) or (document.language.language == ""):
            document.language = german
        else:
            document.language_orig = document.language
            document.language = german
            document.save()


def remove_translation_language(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    for document in (
        Document.objects.filter(app=LATEIN).filter(translation_ref__isnull=False).all()
    ):
        document.language = document.language_orig
        document.language_orig = None


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0090_add_translation_lang"),
    ]

    operations = [
        migrations.RunPython(add_translation_language, remove_translation_language)
    ]
