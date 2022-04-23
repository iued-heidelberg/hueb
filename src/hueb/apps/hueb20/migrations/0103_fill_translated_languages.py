from django.db import migrations, DataError

def fill_transl_name(apps, schema_editor):
    Language = apps.get_model("hueb20", "Language")

    for language in Language.objects.all():
        language.language_de = language.language_temp
        language.language_en = language.language_temp
        language.save()

def empty_transl_name(apps, schema_editor):
    Language = apps.get_model("hueb20", "Language")

    for language in Language.objects.all():
        language.language_de = None
        language.language_en = None
        language.save()

class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0102_create_de_en"),
    ]

    operations = [
        migrations.RunPython(fill_transl_name, empty_transl_name)
    ]
