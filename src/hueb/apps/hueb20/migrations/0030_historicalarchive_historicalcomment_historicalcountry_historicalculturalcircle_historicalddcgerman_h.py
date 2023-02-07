# Generated by Django 3.0.5 on 2020-08-25 21:59

import django.contrib.postgres.fields.ranges
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb_legacy_latein", "0007_auto_20200822_1500"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hueb20", "0029_auto_20200825_2110"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalPerson",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "lifetime_start",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True, null=True
                    ),
                ),
                (
                    "lifetime_end",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True, null=True
                    ),
                ),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "alias",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.Person",
                    ),
                ),
                (
                    "author_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.AuthorNew",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "publisherOriginal_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.OriginalNew",
                    ),
                ),
                (
                    "publisherTranslation_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.TranslationNew",
                    ),
                ),
                (
                    "translator_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.TranslatorNew",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical person",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalLanguage",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("language", models.CharField(max_length=255)),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "language_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.Language",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical language",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalFiling",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("signatur", models.CharField(max_length=255)),
                ("link", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "archive",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.Archive",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.Document",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "locAssign_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.LocAssign",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical filing",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalDocument",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("title", models.TextField(blank=True, null=True)),
                ("subtitle", models.TextField(blank=True, null=True)),
                (
                    "written_in",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True, null=True
                    ),
                ),
                (
                    "published_location",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("edition", models.TextField(blank=True, null=True)),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "cultural_circle",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.CulturalCircle",
                    ),
                ),
                (
                    "ddc",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.DdcGerman",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.Language",
                    ),
                ),
                (
                    "originalAuthor_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.OriginalNewAuthorNew",
                    ),
                ),
                (
                    "original_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.OriginalNew",
                    ),
                ),
                (
                    "translationTranslator_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.TranslationNewTranslatorNew",
                    ),
                ),
                (
                    "translation_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.TranslationNew",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical document",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalDdcGerman",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("ddc_number", models.CharField(max_length=3)),
                ("ddc_name", models.CharField(max_length=255)),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "ddc_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.DdcGerman",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical DDC",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalCulturalCircle",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the cultural circle", max_length=255
                    ),
                ),
                (
                    "start",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True, null=True
                    ),
                ),
                (
                    "end",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True, null=True
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical cultural circle",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalCountry",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                (
                    "country",
                    models.CharField(help_text="Name of the country", max_length=255),
                ),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "country_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.Country",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical country",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalComment",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("text", models.TextField(blank=True, null=True)),
                (
                    "external",
                    models.BooleanField(
                        default=False,
                        help_text="External comments will be displayed on the public website.",
                    ),
                ),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "cultural_circle",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.CulturalCircle",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.Document",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.Person",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical comment",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalArchive",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("name", models.CharField(max_length=255, null=True)),
                ("adress", models.TextField(blank=True, null=True)),
                ("hostname", models.CharField(blank=True, max_length=255, null=True)),
                ("ip", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "z3950_gateway",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("LATEIN", "HÜB Latein Datensatz"),
                            ("LIDOS ", "HÜB Lidos Datensatz"),
                            ("LEGACY", "HÜB Basis Datensatz"),
                            ("HUEB20", "HÜB 2020 Datensatz"),
                        ],
                        default="HUEB20",
                        max_length=6,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.Country",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "location_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.LocationNew",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical archive",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
