from django.db import migrations
from hueb.apps.hueb20.models import LIDOS


def load_lidos_translators(apps, schema_editor):
    Lidos_translator = apps.get_model("hueb_legacy_lidos", "Translator")

    Translator = apps.get_model("hueb20", "Person")

    for lidos_new_translator in Lidos_translator.objects.all():
        names = lidos_new_translator.name
        sep_names = names.split(";")  # returns the list with many names
        if len(sep_names) > 1:
            for nam in sep_names:
                new_lidos_translator = Translator()
                new_lidos_translator.translator_ref_lidos = lidos_new_translator
                new_lidos_translator.app = LIDOS

                new_lidos_translator.name = nam
                # save each new model
                new_lidos_translator.save()
        elif len(sep_names) == 1:
            new_lidos_translator = Translator()
            new_lidos_translator.translator_ref_lidos = lidos_new_translator
            new_lidos_translator.app = LIDOS

            new_lidos_translator.name = lidos_new_translator.name
            # save each new model
            new_lidos_translator.save()


def unload_lidos_translators(apps, schema_editor):
    Translator = apps.get_model("hueb20", "Person")
    Translator.objects.filter(app=LIDOS).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0067_lidos_authors"),
        # ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [
        migrations.RunPython(load_lidos_translators, unload_lidos_translators)
    ]
