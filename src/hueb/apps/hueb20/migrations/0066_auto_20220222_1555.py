# Generated by Django 3.2.5 on 2022-02-22 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
        ("hueb20", "0065_load_online_filings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="author_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.author",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="publisherOriginal_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.original",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="publisherTranslation_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.translation",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="translator_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.translator",
            ),
        ),
    ]
