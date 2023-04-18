from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.review import ReviewAdmin
from hueb.apps.hueb20.models import DdcGerman
from translated_fields import TranslatedFieldAdmin


@admin.register(DdcGerman)
class DdcGermanAdmin(TranslatedFieldAdmin, ReviewAdmin):
    readonly_fields = ("app", "ddc_link", "id")
    list_display = ("id", "ddc_number", "ddc_name", "state")
    list_filter = ("state", "app")
    search_fields = ("ddc_number", *DdcGerman.ddc_name.fields)

    fieldsets = (
        (
            "DDC Information",
            {
                "description": (" "),
                "fields": ("id", "ddc_number", *DdcGerman.ddc_name.fields),
            },
        ),
        (
            "Review",
            {"fields": ("state",)},
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
            "admin:hueb_legacy_latein_ddcgerman_change",
            args=[obj.ddc_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.ddc_ref)
        return mark_safe(link)

    ddc_link.short_description = "DDC"
