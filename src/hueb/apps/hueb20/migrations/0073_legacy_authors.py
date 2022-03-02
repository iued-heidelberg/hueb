from django.db import migrations
from hueb.apps.hueb20.models import LEGACY
import re


def load_legacy_authors(apps, schema_editor):
    Legacy_authors = apps.get_model("hueb_legacy", "Author")
    Author = apps.get_model("hueb20", "Person")

    for legacy_author in Legacy_authors.objects.all():
        names = legacy_author.name
        sep_names = names.split(";")  # returns the list with many names
        if len(sep_names) > 1:
            for nam in sep_names:
                author = Author()
                author.author_ref_legacy = legacy_author
                author.app = LEGACY
                author.name = nam

                # save each new model
                author.save()
        elif len(sep_names) == 1:
            author = Author()
            # Set reference to old entries
            author.author_ref_legacy = legacy_author
            author.app = LEGACY
            author.name = legacy_author.name

            # save new model
            author.save()


def unload_legacy_authors(apps, schema_editor):
    Author = apps.get_model("hueb20", "Person")
    Author.objects.filter(app=LEGACY).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0072_auto_20220226_1902"),
        # ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [migrations.RunPython(load_legacy_authors, unload_legacy_authors)]
