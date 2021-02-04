# Generated by Django 3.1.3 on 2021-02-04 14:57

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hueb20", "0034_change_range_usage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("NOT_REVIEWED", "Not reviewed"),
                            ("CHANGES_NECESSARY", "Changes necessary"),
                            ("OK", "Successfully Reviewed"),
                        ],
                        default="NOT_REVIEWED",
                        max_length=20,
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
                    "ddc_german",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_ddc",
                        to="hueb20.ddcgerman",
                    ),
                ),
                (
                    "archive",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_archive",
                        to="hueb20.archive",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_country",
                        to="hueb20.country",
                    ),
                ),
                (
                    "cultural_circle",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_culturalcircle",
                        to="hueb20.culturalcircle",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_document",
                        to="hueb20.document",
                    ),
                ),
                (
                    "filing",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_filing",
                        to="hueb20.filing",
                    ),
                ),
                (
                    "note",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="review_comment",
                        to="hueb20.comment",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_person",
                        to="hueb20.person",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="review_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalReview",
            fields=[
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("NOT_REVIEWED", "Not reviewed"),
                            ("CHANGES_NECESSARY", "Changes necessary"),
                            ("OK", "Successfully Reviewed"),
                        ],
                        default="NOT_REVIEWED",
                        max_length=20,
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
                    "DdcGerman",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.ddcgerman",
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
                        to="hueb20.archive",
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
                        to="hueb20.country",
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
                        to="hueb20.culturalcircle",
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
                    "filing",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.filing",
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
                    "note",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb20.comment",
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
                    "user",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical review",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
