from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.review import ReviewAdmin
from hueb.apps.hueb20.models import CulturalCircle

from .comment import CommentInline


@admin.register(CulturalCircle)
class CulturalCircleAdmin(ReviewAdmin):
    readonly_fields = ("app", "id", "cultural_circle_link")
    list_display = ("id", "name", "description", "start", "end")
    search_fields = ("name", "id", "start", "end")
    inlines = [CommentInline]
    fieldsets = (
        (
            "Country Information",
            {
                "description": ("Information stored about the cultural circle"),
                "fields": ("id", "name", "description", "start", "end"),
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
