# Generated by Django 3.2.5 on 2022-10-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0110_validate_links"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filing",
            name="link",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="historicalfiling",
            name="link",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
