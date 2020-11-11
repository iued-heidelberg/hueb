from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.models import CulturalCircle
from simple_history.admin import SimpleHistoryAdmin

from .comment import CommentInline


@admin.register(CulturalCircle)
class CulturalCircleAdmin(SimpleHistoryAdmin):
    readonly_fields = ("app", "cultural_circle_link")
    list_display = ("id", "name", "description", "start", "end")
    search_fields = ("name", "id", "start", "end")
    inlines = [CommentInline]
    fieldsets = (
        (
            "Country Information",
            {
                "description": ("Information stored about the cultural circle"),
                "fields": ("name", "description", "start", "end"),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "cultural_circle_link"),
                "classes": ("collapse",),
            },
        ),
    )

    def cultural_circle_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_country_change",
            args=[obj.country_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.country_ref)
        return mark_safe(link)

    cultural_circle_link.short_description = "Country"
