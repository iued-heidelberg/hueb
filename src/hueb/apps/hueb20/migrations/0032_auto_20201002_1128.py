# Generated by Django 3.0.5 on 2020-10-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0031_create_initial_model_history"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filing",
            name="signatur",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="historicalfiling",
            name="signatur",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
