# Generated by Django 3.2.5 on 2022-04-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0101_fill_lang_temp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="language",
            name="language",
        ),
        migrations.RemoveField(
            model_name="historicallanguage",
            name="language",
        ),
        migrations.AddField(
            model_name="language",
            name="language_de",
            field=models.CharField(max_length=255, null=True, verbose_name="language"),
        ),
        migrations.AddField(
            model_name="language",
            name="language_en",
            field=models.CharField(max_length=255, null=True, verbose_name="language"),
        ),
        migrations.AddField(
            model_name="historicallanguage",
            name="language_de",
            field=models.CharField(max_length=255, null=True, verbose_name="language"),
        ),
        migrations.AddField(
            model_name="historicallanguage",
            name="language_en",
            field=models.CharField(max_length=255, null=True, verbose_name="language"),
        ),
    ]