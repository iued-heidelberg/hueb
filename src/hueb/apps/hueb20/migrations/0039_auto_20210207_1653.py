# Generated by Django 3.1.3 on 2021-02-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0038_auto_20210207_1652"),
    ]

    operations = [
        migrations.AddField(
            model_name="archive",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="country",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="culturalcircle",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ddcgerman",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="document",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="filing",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalarchive",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalcountry",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalculturalcircle",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalddcgerman",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicaldocument",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalfiling",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicallanguage",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="language",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="person",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
    ]
