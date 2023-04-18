from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _
from hueb.apps.tenants.models import TenantUser
from hueb.apps.tenants.utils import tenant_from_request


class TenantUserInline(admin.StackedInline):
    model = TenantUser
    can_delete = False
    verbose_name_plural = "tenant"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ("tenantuser",)
    # inlines = [TenantUserInline]

    staff_fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Permissions"), {"fields": ("is_staff", "is_active")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Groups"), {"fields": ("groups",)}),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(UserAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        user = kwargs["request"].user

        if not user.is_superuser:
            if db_field.name == "groups":
                field.queryset = field.queryset.filter(
                    id__in=[
                        i.id
                        for i in Group.objects.filter(name__icontains="Tenant").all()
                    ]
                )
        return field

    def get_inlines(self, request, obj):
        if not request.user.is_superuser:
            return []
        else:
            return [TenantUserInline]

    def get_fieldsets(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return self.staff_fieldsets
        else:
            return super().get_fieldsets(request, obj)

    def has_delete_permission(self, request, obj=None):
        tenant = tenant_from_request(request)
        if tenant and obj and (tenant != obj.tenantuser.tenant):
            return False
        return super().has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        tenant = tenant_from_request(request)
        if tenant and obj and (tenant != obj.tenantuser.tenant):
            return False
        return super().has_change_permission(request, obj)

    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        if tenant:
            queryset = queryset.filter(tenantuser__tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        super().save_model(request, obj, form, change)
        if tenant and not change:
            tenantuser = TenantUser(tenant=tenant, user=obj)
            tenantuser.save()


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
