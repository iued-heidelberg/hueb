from django.contrib.auth.models import User
from django.db import models

TENANT_APPS = [
    ("GUEBFR", "GÜB-FR"),
    ("HUES", "HUES"),
]

TENANT_PREFIX_TO_COLOR = {
    "gueb": "rgb(35 55 60 / 10%)",
    "hues": "rgb(181 21 43 / 10%)",
}


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    app = models.CharField(max_length=6, choices=TENANT_APPS)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name

    def get_verbose_name(self):
        for app in TENANT_APPS:
            if app[0] == self.app:
                return app[1]


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
