# Generated by Django 3.0.5 on 2020-08-12 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0005_auto_20200811_2223"),
    ]

    operations = [
        migrations.RenameField(
            model_name="document", old_name="authors", new_name="written_by",
        ),
    ]