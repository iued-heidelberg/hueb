# Generated by Django 3.1.3 on 2021-02-04 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hueb20", "0036_create_reviewstates"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalreview",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalreview",
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
        migrations.AlterField(
            model_name="review",
            name="archive",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.archive",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.country",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="cultural_circle",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.culturalcircle",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="ddc_german",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.ddcgerman",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="document",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.document",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="filing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.filing",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="note",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="hueb20.comment",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hueb20.person",
            ),
        ),
        migrations.AlterField(
            model_name="review",
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
        migrations.AlterField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]