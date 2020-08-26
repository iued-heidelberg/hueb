from django.conf import settings
from django.core.management import call_command
from django.db import migrations


def forwards_func(apps, schema_editor):
    call_command("populate_history", "--auto")


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("hueb_legacy_latein", "0007_auto_20200822_1500"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "hueb20",
            "0030_historicalarchive_historicalcomment_historicalcountry_historicalculturalcircle_historicalddcgerman_h",
        ),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
