# Generated by Django 3.0.5 on 2020-08-14 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0009_auto_20200814_2103"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="documentrelationship",
            name="relationship_type",
        ),
    ]
