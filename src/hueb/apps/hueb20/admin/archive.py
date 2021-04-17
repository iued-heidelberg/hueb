from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.review import ReviewAdmin
from hueb.apps.hueb20.models import Archive


@admin.register(Archive)
class ArchiveAdmin(ReviewAdmin):
    readonly_fields = ("id", "app", "archive_link")
    list_display = (
        "id",
        "name",
        "adress",
        "country",
        "hostname",
        "ip",
        "z3950_gateway",
        "state",
    )
    list_filter = ("state", "app")
    autocomplete_fields = ("country",)
    search_fields = ("name", "adress", "country__country")

    fieldsets = (
        (
            "Archive Information",
            {
                "description": (" "),
                "fields": (
                    "id",
                    "name",
                    "adress",
                    "country",
                    "hostname",
                    "ip",
                    "z3950_gateway",
                ),
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
                "fields": ("app", "archive_link"),
                "classes": ("collapse",),
            },
        ),
    )

    def archive_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_locationnew_change",
            args=[obj.location_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.location_ref)
        return mark_safe(link)

    archive_link.short_description = "Archive"
