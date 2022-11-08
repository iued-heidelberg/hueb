from django.db import migrations


def repair_filings(apps, schema_editor):
    Filing = apps.get_model("hueb20", "Filing")

    for filing in (
        Filing.objects.filter(link__isnull=False).filter(link_status=False).all()
    ):
        name = filing.link
        sep_names = name.split(" ")  # returns the list with many names
        link = [link for link in sep_names if "http" in link]
        if len(link) == 1:
            filing.link = link[0]
            filing.save()


def unrepair_filings(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0111_auto_20221031_1058"),
    ]

    operations = [
        migrations.RunPython(repair_filings, unrepair_filings),
    ]
