# Generated by Django 3.2.5 on 2021-07-06 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SuebLidosAuthor",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("comment", models.TextField(blank=True, null=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
            ],
            options={
                "db_table": "sueb_lidos_author",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosDdcGerman",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("ddc_number", models.CharField(max_length=3)),
                ("ddc_name", models.CharField(max_length=255)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
            ],
            options={
                "db_table": "sueb_lidos_ddc_german",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosFilter",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("a", models.CharField(blank=True, max_length=255, null=True)),
                ("b", models.CharField(blank=True, max_length=255, null=True)),
                ("c", models.CharField(blank=True, max_length=255, null=True)),
                ("d", models.TextField(blank=True, null=True)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
            ],
            options={
                "db_table": "sueb_lidos_filter",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosLanguage",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("language", models.CharField(max_length=255)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
            ],
            options={
                "db_table": "sueb_lidos_language",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosLidosEx",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "number_01",
                    models.CharField(
                        blank=True, db_column="01", max_length=255, null=True
                    ),
                ),
                (
                    "number_03",
                    models.CharField(
                        blank=True, db_column="03", max_length=255, null=True
                    ),
                ),
                (
                    "number_04",
                    models.CharField(
                        blank=True, db_column="04", max_length=255, null=True
                    ),
                ),
                (
                    "number_05",
                    models.CharField(
                        blank=True, db_column="05", max_length=255, null=True
                    ),
                ),
                (
                    "number_06",
                    models.CharField(
                        blank=True, db_column="06", max_length=255, null=True
                    ),
                ),
                (
                    "number_11",
                    models.CharField(
                        blank=True, db_column="11", max_length=255, null=True
                    ),
                ),
                (
                    "number_1a",
                    models.CharField(
                        blank=True, db_column="1a", max_length=255, null=True
                    ),
                ),
                (
                    "number_12",
                    models.CharField(
                        blank=True, db_column="12", max_length=255, null=True
                    ),
                ),
                (
                    "number_13",
                    models.CharField(
                        blank=True, db_column="13", max_length=255, null=True
                    ),
                ),
                (
                    "number_15",
                    models.CharField(
                        blank=True, db_column="15", max_length=255, null=True
                    ),
                ),
                (
                    "number_20",
                    models.CharField(
                        blank=True, db_column="20", max_length=255, null=True
                    ),
                ),
                (
                    "number_21",
                    models.CharField(
                        blank=True, db_column="21", max_length=255, null=True
                    ),
                ),
                (
                    "number_2a",
                    models.CharField(
                        blank=True, db_column="2a", max_length=255, null=True
                    ),
                ),
                (
                    "number_22",
                    models.CharField(
                        blank=True, db_column="22", max_length=255, null=True
                    ),
                ),
                (
                    "number_23",
                    models.CharField(
                        blank=True, db_column="23", max_length=255, null=True
                    ),
                ),
                (
                    "number_51",
                    models.CharField(
                        blank=True, db_column="51", max_length=255, null=True
                    ),
                ),
                (
                    "number_52",
                    models.CharField(
                        blank=True, db_column="52", max_length=255, null=True
                    ),
                ),
                (
                    "number_60",
                    models.CharField(
                        blank=True, db_column="60", max_length=255, null=True
                    ),
                ),
                (
                    "number_61",
                    models.CharField(
                        blank=True, db_column="61", max_length=255, null=True
                    ),
                ),
                (
                    "number_62",
                    models.CharField(
                        blank=True, db_column="62", max_length=255, null=True
                    ),
                ),
                (
                    "number_63",
                    models.CharField(
                        blank=True, db_column="63", max_length=255, null=True
                    ),
                ),
                (
                    "deskriptoren",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "number_25",
                    models.CharField(
                        blank=True, db_column="25", max_length=255, null=True
                    ),
                ),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
            ],
            options={
                "db_table": "sueb_lidos_lidos_ex",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosManualKeys",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("term", models.CharField(max_length=255)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
            ],
            options={
                "db_table": "sueb_lidos_manual_keys",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosTranslator",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("comment", models.TextField(blank=True, null=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
            ],
            options={
                "db_table": "sueb_lidos_translator",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosTranslation",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.TextField(blank=True, null=True)),
                ("subtitle", models.TextField(blank=True, null=True)),
                ("year", models.CharField(blank=True, max_length=100, null=True)),
                ("publisher", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "published_location",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("edition", models.TextField(blank=True, null=True)),
                ("language_id", models.IntegerField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "manual_keys_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("real_year", models.IntegerField(blank=True, null=True)),
                ("invisible", models.IntegerField(blank=True, null=True)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidosauthor",
                    ),
                ),
                (
                    "ddc",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidosddcgerman",
                    ),
                ),
                (
                    "translator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidostranslator",
                    ),
                ),
                (
                    "via_language",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidoslanguage",
                    ),
                ),
            ],
            options={
                "db_table": "sueb_lidos_translation",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosOriginal",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.TextField(blank=True, null=True)),
                ("subtitle", models.TextField(blank=True, null=True)),
                ("year", models.CharField(blank=True, max_length=100, null=True)),
                ("publisher", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "published_location",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("edition", models.TextField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("real_year", models.IntegerField(blank=True, null=True)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidosauthor",
                    ),
                ),
                (
                    "ddc",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidosddcgerman",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidoslanguage",
                    ),
                ),
                (
                    "manual_keys",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidosmanualkeys",
                    ),
                ),
            ],
            options={
                "db_table": "sueb_lidos_original",
            },
        ),
        migrations.CreateModel(
            name="SuebLidosOrigAssign",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "migration_notes",
                    models.CharField(blank=True, max_length=1023, null=True),
                ),
                ("migration_generated", models.BooleanField()),
                (
                    "original",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidosoriginal",
                    ),
                ),
                (
                    "translation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_lidos.sueblidostranslation",
                    ),
                ),
            ],
            options={
                "db_table": "sueb_lidos_orig_assign",
            },
        ),
        migrations.AddField(
            model_name="sueblidosmanualkeys",
            name="original",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.sueblidosoriginal",
            ),
        ),
        migrations.AddField(
            model_name="sueblidosmanualkeys",
            name="translation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_lidos.sueblidostranslation",
            ),
        ),
    ]
