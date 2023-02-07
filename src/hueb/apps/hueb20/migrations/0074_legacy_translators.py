from django.db import migrations
from hueb.apps.hueb20.models import LEGACY


def load_legacy_translators(apps, schema_editor):
    Legacy_translators = apps.get_model("hueb_legacy", "Translator")
    Translator = apps.get_model("hueb20", "Person")

    for legacy_translator in Legacy_translators.objects.all():
        names = legacy_translator.name
        sep_names = names.split(";")  # returns the list with many names
        if len(sep_names) > 1:
            for nam in sep_names:
                translator = Translator()
                translator.translator_ref_legacy = legacy_translator
                translator.app = LEGACY
                translator.name = nam

                # save each new model
                translator.save()
        elif len(sep_names) == 1:
            translator = Translator()
            # Set reference to old entries
            translator.translator_ref_legacy = legacy_translator
            translator.app = LEGACY
            translator.name = legacy_translator.name

            # save new model
            translator.save()


def unload_legacy_translators(apps, schema_editor):
    Author = apps.get_model("hueb20", "Person")
    Author.objects.filter(app=LEGACY).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0073_legacy_authors"),
        # ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [
        migrations.RunPython(load_legacy_translators, unload_legacy_translators)
    ]
