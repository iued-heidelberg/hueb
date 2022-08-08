# Generated by Django 3.2.5 on 2022-04-23 15:16

from django.db import migrations, models

#Add comment so i can push again and fix buggy tests
class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="publications/%Y/%m/%d")),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
