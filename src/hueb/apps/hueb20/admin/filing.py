from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.review import ReviewAdmin, TabularInlineReviewAdmin
from hueb.apps.hueb20.models import Document, Filing


@admin.register(Filing)
class FilingAdmin(ReviewAdmin):
    readonly_fields = ("app", "locAssign_link", "id")
    list_display = ("id", "signatur", "link")
    search_fields = ("signatur", "id")
    autocomplete_fields = ("archive",)

    fieldsets = (
        (
            "Filing Information",
            {
                "description": ("Stores the filing locations of documents"),
                "fields": ("id", "signatur", "link"),
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
                "fields": ("app", "locAssign_link"),
                "classes": ("collapse",),
            },
        ),
    )

    def locAssign_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_locassign_change",
            args=[obj.locAssign_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.locAssign_ref)
        return mark_safe(link)

    locAssign_link.short_description = "Filing Location"


class FilingInline(TabularInlineReviewAdmin):
    readonly_fields = ("app", "id")
    model = Document.located_in.through
    extra = 0
    verbose_name = "Filing Location"
    verbose_name_plural = verbose_name + "s"
    autocomplete_fields = ("archive",)
    fields = (
        "id",
        "archive",
        "signatur",
        "link",
        "state",
    )
    exclude = ("locAssign_ref", "reviewed")
