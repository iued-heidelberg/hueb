# Generated by Django 3.1.3 on 2021-02-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0037_auto_20210204_1836"),
    ]

    operations = [
        migrations.AddField(
            model_name="archive",
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
            model_name="archive",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="country",
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
            model_name="country",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="culturalcircle",
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
            model_name="culturalcircle",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="ddcgerman",
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
            model_name="ddcgerman",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="document",
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
            model_name="document",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="filing",
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
            model_name="filing",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="historicalarchive",
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
            model_name="historicalarchive",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalcountry",
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
            model_name="historicalcountry",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalculturalcircle",
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
            model_name="historicalculturalcircle",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalddcgerman",
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
            model_name="historicalddcgerman",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicaldocument",
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
            model_name="historicaldocument",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalfiling",
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
            model_name="historicalfiling",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicallanguage",
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
            model_name="historicallanguage",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalperson",
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
            model_name="historicalperson",
            name="timestamp",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="language",
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
            model_name="language",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="person",
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
            model_name="person",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
