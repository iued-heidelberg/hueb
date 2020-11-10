from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.models import Country
from simple_history.admin import SimpleHistoryAdmin


@admin.register(Country)
class CountryAdmin(SimpleHistoryAdmin):
    readonly_fields = ("app", "country_link")
    list_display = (
        "id",
        "country",
    )
    search_fields = ("country", "id")
    fieldsets = (
        (
            "Country Information",
            {
                "description": ("Information stored about the country"),
                "fields": ("country",),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "country_link"),
                "classes": ("collapse",),
            },
        ),
    )

    def country_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_country_change", args=[obj.country_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.country_ref)
        return mark_safe(link)

    country_link.short_description = "Country"
