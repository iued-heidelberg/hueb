# Generated by Django 3.2.5 on 2022-02-10 10:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_history", "0005_alter_userhistory_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userhistory",
            options={
                "verbose_name": "Entries per User",
                "verbose_name_plural": "Entries per User",
            },
        ),
    ]
