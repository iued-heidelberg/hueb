# Generated by Django 3.2.5 on 2022-02-12 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hueb_legacy_lidos", "0009_alter_original_manual_keys"),
        ("hueb20", "0061_load_translation_translator"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="original_ref_lidos",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.original",
            ),
        ),
        migrations.AddField(
            model_name="document",
            name="translation_ref_lidos",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.translation",
            ),
        ),
        migrations.AddField(
            model_name="historicaldocument",
            name="original_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy_lidos.original",
            ),
        ),
        migrations.AddField(
            model_name="historicaldocument",
            name="translation_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy_lidos.translation",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="author_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy_lidos.author",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="publisherOriginal_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy_lidos.original",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="publisherTranslation_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy_lidos.translation",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="translator_ref_lidos",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="hueb_legacy_lidos.translator",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="author_ref_lidos",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.author",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="publisherOriginal_ref_lidos",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.original",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="publisherTranslation_ref_lidos",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.translation",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="translator_ref_lidos",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.translator",
            ),
        ),
        migrations.AlterField(
            model_name="archive",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="contribution",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="culturalcircle",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="ddcgerman",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="documentrelationship",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="filing",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalarchive",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomment",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcontribution",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcountry",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalculturalcircle",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalddcgerman",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldocument",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldocumentrelationship",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalfiling",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicallanguage",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalperson",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
    ]
