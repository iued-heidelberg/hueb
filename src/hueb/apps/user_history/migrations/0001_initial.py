# Generated by Django 3.2.5 on 2022-01-31 21:50
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserHistory",
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
                (
                    "user",
                    models.OneToOneField(
                        to="auth.User",
                        on_delete=models.CASCADE,
                        null=False,
                        blank=False,
                    ),
                ),
            ],
            options={
                "db_table": "user_history_userhistory",
            },
        ),
    ]
