from django.db import migrations
from hueb.apps.hueb20.models import LIDOS
import re


def load_lidos_authors(apps, schema_editor):
    Lidos_authors = apps.get_model("hueb_legacy_lidos", "Author")

    Author = apps.get_model("hueb20", "Person")

    for lidos_new_author in Lidos_authors.objects.all():
        names = lidos_new_author.name
        sep_names = names.split(";")  # returns the list with many names
        if len(sep_names) > 1:
            for nam in sep_names:
                new_lidos_author = Author()
                new_lidos_author.author_ref_lidos = lidos_new_author
                new_lidos_author.app = LIDOS
                new_lidos_author.name = nam

                # save each new model
                new_lidos_author.save()
        elif len(sep_names) == 1:
            new_lidos_author = Author()
            # Set reference to old entries
            new_lidos_author.author_ref_lidos = lidos_new_author
            new_lidos_author.app = LIDOS
            new_lidos_author.name = lidos_new_author.name

            # save new model
            new_lidos_author.save()


def unload_lidos_authors(apps, schema_editor):
    Author = apps.get_model("hueb20", "Person")
    Author.objects.filter(app=LIDOS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0066_auto_20220222_1555"),
        ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
    ]

    operations = [migrations.RunPython(load_lidos_authors, unload_lidos_authors)]
