# Generated by Django 3.0.5 on 2020-08-16 12:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0016_auto_20200816_1129"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="is_alias",
        ),
    ]
