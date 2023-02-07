# Generated by Django 3.0.5 on 2020-08-16 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0017_remove_person_is_alias"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="comment",
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("text", models.TextField(blank=True, null=True)),
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
                        to="hueb20.Document",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.Person",
                    ),
                ),
            ],
        ),
    ]
