# Generated by Django 3.0.5 on 2020-08-11 21:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0003_auto_20200811_2104"),
    ]

    operations = [
        migrations.RenameField(
            model_name="document",
            old_name="location",
            new_name="located_in",
        ),
    ]
