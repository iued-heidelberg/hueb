from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.review import ReviewAdmin
from hueb.apps.hueb20.models import Language
from translated_fields import TranslatedFieldAdmin, to_attribute


# @admin.register(Language)
class LanguageAdmin(TranslatedFieldAdmin, ReviewAdmin):
    readonly_fields = ("app", "language_link", "id")
    list_display = (
        "id",
        "language",
        "state",
    )
    # inlines = [TranslationInline,]
    list_filter = ("state", "app")
    search_fields = (*Language.language.fields, "id")

    fieldsets = (
        (
            "Language Information",
            {
                "description": (" "),
                "fields": ("id", *Language.language.fields),
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
                "fields": ("app", "language_link"),
                "classes": ("collapse",),
            },
        ),
    )

    def language_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_language_change",
            args=[obj.language_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.language_ref)
        return mark_safe(link)

    language_link.short_description = "Language"
    pass


admin.site.register(Language, LanguageAdmin)
