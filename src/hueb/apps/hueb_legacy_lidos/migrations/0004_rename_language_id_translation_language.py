# Generated by Django 3.2.5 on 2021-07-06 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hueb_legacy_lidos", "0003_auto_20210706_2345"),
    ]

    operations = [
        migrations.RenameField(
            model_name="translation",
            old_name="language_id",
            new_name="language",
        ),
    ]
