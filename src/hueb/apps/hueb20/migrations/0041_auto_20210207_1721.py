# Generated by Django 3.1.3 on 2021-02-07 17:21

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb_legacy_latein", "0007_auto_20200822_1500"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hueb20", "0040_auto_20210207_1654"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalContribution",
            fields=[
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("NOT_REVIEWED", "Not reviewed"),
                            ("CHANGES_NECESSARY", "Changes necessary"),
                            ("REREVIEW_NECESSESARY", "Rereview necessary"),
                            ("OK", "Successfully reviewed"),
                        ],
                        default="NOT_REVIEWED",
                        max_length=20,
                    ),
                ),
                ("reviewed", models.BooleanField(default=False)),
                (
                    "timestamp",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                (
                    "contribution_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("PUBLISHER", "Publisher"),
                            ("WRITER", "Writer"),
                            ("OTHER", "Other"),
                        ],
                        max_length=20,
                        null=True,
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
                    "document",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.document",
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
                    "originalAuthor_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.originalnewauthornew",
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
                        to="hueb20.person",
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
                        to="hueb_legacy_latein.translationnewtranslatornew",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical contribution",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Contribution",
            fields=[
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("NOT_REVIEWED", "Not reviewed"),
                            ("CHANGES_NECESSARY", "Changes necessary"),
                            ("REREVIEW_NECESSESARY", "Rereview necessary"),
                            ("OK", "Successfully reviewed"),
                        ],
                        default="NOT_REVIEWED",
                        max_length=20,
                    ),
                ),
                ("reviewed", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True, null=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "contribution_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("PUBLISHER", "Publisher"),
                            ("WRITER", "Writer"),
                            ("OTHER", "Other"),
                        ],
                        max_length=20,
                        null=True,
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
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.document",
                    ),
                ),
                (
                    "originalAuthor_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.originalnewauthornew",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.person",
                    ),
                ),
                (
                    "translationTranslator_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.translationnewtranslatornew",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="document",
            name="contributions",
            field=models.ManyToManyField(
                through="hueb20.Contribution", to="hueb20.Person"
            ),
        ),
    ]
