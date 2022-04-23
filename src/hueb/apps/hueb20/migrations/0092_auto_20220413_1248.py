# Generated by Django 3.2.5 on 2022-04-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hueb20', '0091_add_translation_lang_latein'),
    ]

    operations = [
        migrations.AddField(
            model_name='culturalcircle',
            name='name_temp',
            field=models.CharField(help_text='Name of the cultural circle', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalculturalcircle',
            name='name_temp',
            field=models.CharField(help_text='Name of the cultural circle', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='culturalcircle',
            name='name',
            field=models.CharField(help_text='Name of the cultural circle', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalculturalcircle',
            name='name',
            field=models.CharField(help_text='Name of the cultural circle', max_length=255, null=True),
        ),
    ]
