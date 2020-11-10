from django.contrib import admin
from django.contrib.postgres.fields import IntegerRangeField
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.models import Person
from hueb.apps.hueb20.widgets.timerange import TimeRangeWidget
from simple_history.admin import SimpleHistoryAdmin

from .comment import CommentInline


@admin.register(Person)
class PersonAdmin(SimpleHistoryAdmin):

    readonly_fields = ("app", "author_link", "translator_link")
    list_display = (
        "id",
        "name",
        "alias",
        "is_alias",
        "adapt_person_lifetime_start_list_view",
        "adapt_person_lifetime_end_list_view",
    )
    search_fields = ("name", "id", "lifetime_start", "lifetime_end")
    autocomplete_fields = ("alias",)
    formfield_overrides = {IntegerRangeField: {"widget": TimeRangeWidget}}
    fieldsets = (
        (
            "Person Information",
            {
                "description": ("All known data about a person"),
                "fields": ("name", "alias", "lifetime_start", "lifetime_end"),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "translator_link", "author_link"),
                "classes": ("collapse",),
            },
        ),
    )
    inlines = [CommentInline]

    def author_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_authornew_change", args=[obj.author_ref.id]
        )
        link = '<a href="%s">%s</a>' % (url, obj.author_ref)
        return mark_safe(link)

    author_link.short_description = "Author"

    def translator_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translatornew_change",
            args=[obj.translator_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translator_ref)
        return mark_safe(link)

    translator_link.short_description = "Translator"
