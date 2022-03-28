# Generated by Django 3.2.5 on 2022-02-26 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hueb_legacy", "0008_auto_20210707_1629"),
        ("hueb20", "0071_lidos_authors_translators"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="original_ref_legacy",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy.original",
            ),
        ),
        migrations.AddField(
            model_name="document",
            name="translation_ref_legacy",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy.translation",
            ),
        ),
        migrations.AddField(
            model_name="historicaldocument",
            name="original_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy.original",
            ),
        ),
        migrations.AddField(
            model_name="historicaldocument",
            name="translation_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy.translation",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="author_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy.author",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="publisherOriginal_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy.original",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="publisherTranslation_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy.translation",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="translator_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy.translator",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="author_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy.author",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="publisherOriginal_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy.original",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="publisherTranslation_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy.translation",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="translator_ref_legacy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy.translator",
            ),
        ),
    ]