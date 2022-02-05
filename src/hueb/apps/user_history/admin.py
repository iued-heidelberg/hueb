from django.contrib import admin
from .models import UserHistory
from import_export.admin import ExportMixin
from hueb.apps.hueb20.admin.review import TabularInlineReviewAdmin


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
        "total_addition_count",
        "document_addition_count",
        "recent_document_additions",
        "person_addition_count",
        "recent_person_additions",
    )

    search_fields = ("user",)

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
                "fields": (
                    "total_addition_count",
                    "document_addition_count",
                    "recent_document_additions",
                    "person_addition_count",
                    "recent_person_additions",
                ),
            },
        ),
    )
