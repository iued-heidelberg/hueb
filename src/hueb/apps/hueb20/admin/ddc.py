from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.models import DdcGerman
from simple_history.admin import SimpleHistoryAdmin


@admin.register(DdcGerman)
class DdcGermanAdmin(SimpleHistoryAdmin):
    readonly_fields = ("app", "ddc_link")
    list_display = (
        "id",
        "ddc_number",
        "ddc_name",
    )
    search_fields = ("ddc_number", "ddc_name")

    fieldsets = (
        (
            "DDC Information",
            {"description": (" "), "fields": ("ddc_number", "ddc_name")},
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "ddc_link"),
                "classes": ("collapse",),
            },
        ),
    )

    def ddc_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_ddcgerman_change", args=[obj.ddc_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.ddc_ref)
        return mark_safe(link)

    ddc_link.short_description = "DDC"
