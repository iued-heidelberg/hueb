from django.db import migrations
from hueb.apps.hueb20.models import LATEIN


def load_filings(apps, schema_editor):
    Legacy_LocAssign = apps.get_model("hueb_legacy_latein", "LocAssign")

    Filing = apps.get_model("hueb20", "Filing")
    Document = apps.get_model("hueb20", "Document")
    Archive = apps.get_model("hueb20", "Archive")

    for legacy_loc_assign in Legacy_LocAssign.objects.all():
        if Filing.objects.filter(locAssign_ref = legacy_loc_assign).exists():
            new_filing = Filing.objects.get(locAssign_ref = legacy_loc_assign)
        else:
            new_filing = Filing()
        # Set reference to old entries
        new_filing.locAssign_ref = legacy_loc_assign
        new_filing.app = LATEIN

        # transfer information
        if Archive.objects.filter(location_ref=legacy_loc_assign.loc_new).exists():
            new_filing.archive = Archive.objects.get(location_ref=legacy_loc_assign.loc_new)
        elif legacy_loc_assign.loc_new is not None:
            raise Exception("There is no archive assigned to " + legacy_loc_assign.loc_new.id)

        new_filing.signatur = legacy_loc_assign.signatur

        assert ((legacy_loc_assign.orig_new is not None) or (legacy_loc_assign.trans_new is not None))

        if legacy_loc_assign.orig_new is not None and legacy_loc_assign.orig_new.title != "" and legacy_loc_assign.orig_new.title is not None:
            d = Document.objects.get(original_ref=legacy_loc_assign.orig_new)
            new_filing.document = d
            new_filing.link = legacy_loc_assign.orig_new.link
            # save new model
            new_filing.save()
            d.filing_set.add(new_filing)
            d.save()
        elif legacy_loc_assign.trans_new is not None and legacy_loc_assign.trans_new.title != "" and legacy_loc_assign.trans_new.title is not None:
            d = Document.objects.get(translation_ref=legacy_loc_assign.trans_new)
            new_filing.document = d
            new_filing.link = legacy_loc_assign.trans_new.link
            # save new model
            new_filing.save()
            d.filing_set.add(new_filing)
            d.save()


def unload_filings(apps, schema_editor):
    Filing = apps.get_model("hueb20", "Filing")
    Filing.objects.filter(app=LATEIN).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0058_load_latein_translations"),
        #("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_filings, unload_filings)]
