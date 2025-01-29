from django.db import migrations


def create_duies(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")

    hues = Tenant.objects.create(name="duies", subdomain_prefix="duies", app="DUIES")
    hues.save()


def remove_duies(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")
    Tenant.objects.get(name="duies").delete()


class Migration(migrations.Migration):
    initial = True

    dependencies = [("tenants", "0005_alter_tenantuser_user")]

    operations = [migrations.RunPython(create_duies, remove_duies)]
