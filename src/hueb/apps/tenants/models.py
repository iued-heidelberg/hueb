from django.contrib.auth.models import User
from django.db import models

TENANT_APPS = [
    ("GUEBFR", "GÜB-FR"),
    ("HUES", "HUES"),
]


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    app = models.CharField(max_length=6, choices=TENANT_APPS)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class TenantUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="tenantuser"
    )
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        if self.tenant.name is None:
            return " "
        return self.tenant.name
