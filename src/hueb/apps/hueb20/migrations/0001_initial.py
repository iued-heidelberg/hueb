# Generated by Django 3.0.5 on 2020-07-10 11:56

import django.contrib.postgres.fields.ranges
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archive",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("signatur", models.CharField(max_length=255)),
                ("link", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("country", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="DdcGerman",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("ddc_number", models.CharField(max_length=3)),
                ("ddc_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="SourceReference",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("model", models.CharField(max_length=255)),
                ("reference_id", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="YearRange",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "timerange",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True, null=True
                    ),
                ),
                ("start_uncertainty", models.IntegerField(blank=True, null=True)),
                ("end_uncertainty", models.IntegerField(blank=True, null=True)),
                ("parsed_string", models.TextField(blank=True, null=True)),
                (
                    "source",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.SourceReference",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("is_alias", models.BooleanField(blank=True, null=True)),
                (
                    "alias",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.Person",
                    ),
                ),
                (
                    "lifetime",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.YearRange",
                    ),
                ),
                (
                    "source",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.SourceReference",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, null=True)),
                ("adress", models.TextField(blank=True, null=True)),
                ("hostname", models.CharField(blank=True, max_length=255, null=True)),
                ("ip", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "z3950_gateway",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "country",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb20.Country",
                    ),
                ),
                (
                    "source",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.SourceReference",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("language", models.CharField(max_length=255)),
                (
                    "source",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.SourceReference",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.TextField()),
                ("subtitle", models.TextField(blank=True, null=True)),
                (
                    "published_location",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("edition", models.TextField(blank=True, null=True)),
                ("year_published", models.DateTimeField(blank=True, null=True)),
                ("archive", models.ManyToManyField(to="hueb20.Archive")),
                (
                    "author",
                    models.ManyToManyField(
                        related_name="DocumentAuthor", to="hueb20.Person"
                    ),
                ),
                ("country", models.ManyToManyField(to="hueb20.Country")),
                (
                    "ddc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb20.DdcGerman",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb20.Language",
                    ),
                ),
                (
                    "published",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.YearRange",
                    ),
                ),
                (
                    "publisher",
                    models.ManyToManyField(
                        related_name="DocumentPublisher", to="hueb20.Person"
                    ),
                ),
                (
                    "source",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.SourceReference",
                    ),
                ),
                (
                    "translated_from",
                    models.ManyToManyField(
                        related_name="_document_translated_from_+", to="hueb20.Document"
                    ),
                ),
                (
                    "translated_to",
                    models.ManyToManyField(
                        related_name="_document_translated_to_+", to="hueb20.Document"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ddcgerman",
            name="source",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.SourceReference",
            ),
        ),
        migrations.AddField(
            model_name="country",
            name="source",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.SourceReference",
            ),
        ),
        migrations.AddField(
            model_name="archive",
            name="source",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.SourceReference",
            ),
        ),
    ]
