from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from hueb.apps.tenants.models import TenantUser


class TenantUserInline(admin.StackedInline):
    model = TenantUser
    can_delete = False
    verbose_name_plural = "tenant"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ("tenantuser",)
    inlines = [TenantUserInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
