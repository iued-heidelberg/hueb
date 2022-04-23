from django.db import migrations, DataError

def fill_tempname(apps, schema_editor):
    Language = apps.get_model("hueb20", "Language")

    for language in Language.objects.all():
        language.language_temp = language.language
        language.save()

def empty_tempname(apps, schema_editor):
    Language = apps.get_model("hueb20", "Language")

    for language in Language.objects.all():
        language.language_temp = None
        language.save()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0100_create_language_temp"),
    ]

    operations = [
        migrations.RunPython(fill_tempname, empty_tempname)
    ]
