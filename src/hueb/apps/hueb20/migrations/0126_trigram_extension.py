from django.contrib.postgres import operations
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0125_remove_blank_spaces"),
    ]

    operations = [
        operations.TrigramExtension(),
    ]
