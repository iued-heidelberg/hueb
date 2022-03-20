# Generated by Django 3.2.5 on 2022-03-11 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0083_correct_pub_loc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documentrelationship",
            name="document_from",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="to_original",
                to="hueb20.document",
            ),
        ),
        migrations.AlterField(
            model_name="documentrelationship",
            name="document_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="to_translation",
                to="hueb20.document",
            ),
        ),
    ]
