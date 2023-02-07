from django.db import migrations
from hueb.apps.hueb20.models import LIDOS


def add_translation_language(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    Language = apps.get_model("hueb20", "Language")
    # lang = Language.objects.get(language__iexact="deutsch")
    # Filter translations
    for document in (
        Document.objects.filter(app=LIDOS)
        .filter(translation_ref_lidos__isnull=False)
        .all()
    ):
        if (document.language is not None) and (document.language.language != ""):
            continue
        else:
            document.language = Language.objects.get(language__iexact="deutsch")
            document.save()


def remove_translation_language(apps, schema_editor):
    Document = apps.get_model("hueb20", "Document")
    for document in (
        Document.objects.filter(app=LIDOS)
        .filter(translation_ref_lidos__isnull=False)
        .all()
    ):
        document.languege.language = ""


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0087_legacy_with_no_pair"),
    ]

    operations = [
        migrations.RunPython(add_translation_language, remove_translation_language)
    ]
