from django.db import migrations


def rename_eip(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")

    duies = Tenant.objects.get(name="duies")
    duies.name = "eip"
    duies.subdomain_prefix = "eip"
    duies.app = "EIP"
    duies.save()


def rename_eip_back(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")
    eip = Tenant.objects.get(name="eip")
    eip.name = "duies"
    eip.subdomain_prefix = "duies"
    eip.app = "DUIES"
    eip.save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [("tenants", "0006_create_tenants_duies")]

    operations = [migrations.RunPython(rename_eip, rename_eip_back)]
