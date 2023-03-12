from django.db import migrations


def create_hueb_and_gueb(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")

    gueb = Tenant.objects.create(name="gueb", subdomain_prefix="gueb", app="GUEBFR")
    gueb.save()


def remove_hueb_and_gueb(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")
    Tenant.objects.get(name="gueb").delete()


class Migration(migrations.Migration):
    initial = True

    dependencies = [("tenants", "0001_initial")]

    operations = [migrations.RunPython(create_hueb_and_gueb, remove_hueb_and_gueb)]
