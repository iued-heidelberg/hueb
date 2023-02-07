# Generated by Django 3.2.5 on 2021-07-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb_legacy_lidos", "0005_auto_20210707_1109"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="ddcgerman",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="filter",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="language",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="lidosex",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="manualkeys",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="origassign",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="original",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="translation",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="translator",
            name="migration_generated",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
