from django.db import migrations


def create_hues(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")

    hues = Tenant.objects.create(name="hues", subdomain_prefix="hues", app="HUES")
    hues.save()


def remove_hues(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")
    Tenant.objects.get(name="hues").delete()


class Migration(migrations.Migration):
    initial = True

    dependencies = [("tenants", "0003_tenantuser")]

    operations = [migrations.RunPython(create_hues, remove_hues)]
