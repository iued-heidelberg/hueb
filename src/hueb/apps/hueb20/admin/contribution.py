from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.review import ReviewAdmin, TabularInlineReviewAdmin
from hueb.apps.hueb20.models import Contribution, Document


@admin.register(Contribution)
class ContributionAdmin(ReviewAdmin):
    readonly_fields = (
        "app",
        "id",
        "author_link",
        "translator_link",
    )
    list_display = ("id", "person", "contribution_type", "document")
    list_filter = ("state", "app")
    search_fields = ("person", "document")
    autocomplete_fields = ("person", "document")

    fieldsets = (
        (
            "Contribution Information",
            {
                "description": ("Stores the contribution locations of documents"),
                "fields": ("id", "person", "contribution_type", "document"),
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
                "fields": ("app", "author_link", "translator_link"),
                "classes": ("collapse",),
            },
        ),
    )

    def author_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_originalnewauthornew_change",
            args=[obj.author_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.author_ref)
        return mark_safe(link)

    author_link.short_description = "Author"

    def translator_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translationnewtranslatornew_change",
            args=[obj.translator_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translator_ref)
        return mark_safe(link)

    translator_link.short_description = "Filing Location"

    def get_queryset(self, request):
        qs = (
            super()
            .get_queryset(request)
            .select_related("document")
            .select_related("person")
        )
        return qs


class ContributionInline(TabularInlineReviewAdmin):
    readonly_fields = ("app", "id", "person_id")
    model = Document.contributions.through
    extra = 0
    verbose_name = "Contributions"
    verbose_name_plural = verbose_name
    autocomplete_fields = ("person",)
    fields = ("person_id", "person", "contribution_type", "state")
    exclude = ("originalAuthor_ref", "translationTranslator_ref", "reviewed")
