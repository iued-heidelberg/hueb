# Generated by Django 3.1.3 on 2021-02-07 17:25

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hueb_legacy_latein", "0007_auto_20200822_1500"),
        ("hueb20", "0041_auto_20210207_1721"),
    ]

    operations = [
        migrations.AddField(
            model_name="documentrelationship",
            name="original_ref",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_latein.originalnew",
            ),
        ),
        migrations.AddField(
            model_name="documentrelationship",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="documentrelationship",
            name="state",
            field=models.CharField(
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
        migrations.AddField(
            model_name="documentrelationship",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="documentrelationship",
            name="translation_ref",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hueb_legacy_latein.translationnew",
            ),
        ),
        migrations.CreateModel(
            name="HistoricalDocumentRelationship",
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
                    "document_from",
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
                    "document_to",
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
                    "original_ref",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="hueb_legacy_latein.originalnew",
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
                        to="hueb_legacy_latein.translationnew",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical document relationship",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]