from django.contrib import admin
from .models import UserHistory
from import_export.admin import ExportMixin

class ReadonlyAdmin(ExportMixin, admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(UserHistory)
class UserHistoryAdmin(ReadonlyAdmin):
    list_display = (
        "user",
        "get_addition_count",
    )

    search_fields = ("user", "get_addition_count",)

    fieldsets = (
        (
            "User Information",
            {
                "fields": ("user",),
            },
        ),
        (
            "Activity",
            {
                "fields": ("get_addition_count",),
            },
        ),
    )

