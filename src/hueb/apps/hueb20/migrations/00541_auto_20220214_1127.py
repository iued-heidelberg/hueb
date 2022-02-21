# Generated by Django 3.2.5 on 2022-02-14 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "hueb_legacy_latein",
            "0009_rename_original_new_originalnewauthornew_original",
        ),
        ("hueb20", "0049_update_cultural_circles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="publisherOriginal_ref",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_latein.originalnew",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="publisherTranslation_ref",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_latein.translationnew",
            ),
        ),
    ]