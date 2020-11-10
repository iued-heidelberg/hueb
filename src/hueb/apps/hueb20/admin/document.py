from django.contrib import admin
from django.contrib.postgres.fields import IntegerRangeField
from django.db.models import Count
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.models import Document
from hueb.apps.hueb20.widgets.timerange import TimeRangeWidget
from hueb.apps.hueb_legacy_latein import models as Legacy
from simple_history.admin import SimpleHistoryAdmin

from .comment import CommentInline
from .filing import FilingInline


class LegacyAuthorNew(admin.TabularInline):
    model = Legacy.AuthorNew
    extra = 0


class DocumentAuthorInline(admin.TabularInline):
    model = Document.written_by.through
    extra = 0
    verbose_name = "Author or Translator"
    verbose_name_plural = verbose_name
    autocomplete_fields = ("person",)


class DocumentPublisherInline(admin.TabularInline):
    model = Document.publishers.through
    extra = 0
    verbose_name = "Publisher"
    verbose_name_plural = verbose_name + "s"
    autocomplete_fields = ("person",)


class TranslationRelationshipInline(admin.TabularInline):
    readonly_fields = ("app",)
    model = Document.translations.through
    fk_name = "document_from"
    extra = 0
    verbose_name = "Translation"
    verbose_name_plural = verbose_name + "s"
    autocomplete_fields = ("document_to",)


class OriginalRelationshipInline(admin.TabularInline):

    readonly_fields = ("app",)
    model = Document.translations.through
    fk_name = "document_to"
    extra = 0
    verbose_name = "Original"
    verbose_name_plural = verbose_name + "s"
    autocomplete_fields = ("document_from",)


@admin.register(Document)
class DocumentAdmin(SimpleHistoryAdmin):

    autocomplete_fields = ("ddc", "cultural_circle", "language")
    readonly_fields = (
        "app",
        "origAssign_link",
        "original_link",
        "translation_link",
        "originalAuthor_link",
        "translationTranslator_link",
    )
    list_display = (
        "id",
        "title",
        "subtitle",
        "get_written_by",
        "adapt_document_written_in_list_view",
        "get_publishers",
        "published_location",
        "edition",
        "language",
        "ddc",
        "cultural_circle",
        "get_archives_count",
        "get_archives",
        "get_translations",
    )
    formfield_overrides = {IntegerRangeField: {"widget": TimeRangeWidget}}
    inlines = [
        DocumentAuthorInline,
        DocumentPublisherInline,
        TranslationRelationshipInline,
        OriginalRelationshipInline,
        FilingInline,
        CommentInline,
    ]
    search_fields = ("id", "title", "written_by__name", "written_in")
    fieldsets = (
        (
            "Document Information",
            {
                "description": ("Stores the information known about documents"),
                "fields": (
                    "title",
                    "subtitle",
                    "edition",
                    "language",
                    "ddc",
                    "written_in",
                    "published_location",
                    "cultural_circle",
                ),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": (
                    "app",
                    "origAssign_link",
                    "original_link",
                    "originalAuthor_link",
                    "translationTranslator_link",
                    "translation_link",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    def get_queryset(self, request):
        qs = (
            super(DocumentAdmin, self)
            .get_queryset(request)
            .annotate(archives_count=Count("located_in"))
            .prefetch_related("written_by")
            .prefetch_related("located_in")
            .prefetch_related("publishers")
            .prefetch_related("translations")
            .select_related("language")
            .select_related("ddc")
            .select_related("cultural_circle")
        )
        return qs

    def get_archives_count(self, obj):
        return int(obj.archives_count)

    get_archives_count.admin_order_field = "archives_count"
    get_archives_count.short_description = "Anzahl Archive"

    def get_archives(self, obj):
        return "\n".join([archive.name for archive in obj.located_in.all()])

    get_archives.short_description = "Archive"

    def get_publishers(self, obj):
        return "\n".join([publisher.name for publisher in obj.publishers.all()])

    get_publishers.short_description = "Publisher"

    def get_written_by(self, obj):
        return "\n".join([writer.name for writer in obj.written_by.all()])

    get_written_by.short_description = "Written by"

    def get_translations(self, obj):
        return "\n".join([translation.title for translation in obj.translations.all()])

    get_translations.short_description = "Translation"

    def origAssign_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_origassign_change", args=[obj.origAssign_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.origAssign_ref)
        return mark_safe(link)

    origAssign_link.short_description = "Original<->Translation Relationship"

    def original_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_originalnew_change", args=[obj.original_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.original_ref)
        return mark_safe(link)

    original_link.short_description = "Original Text"

    def translation_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translationnew_change",
            args=[obj.translation_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translation_ref)
        return mark_safe(link)

    translation_link.short_description = "Translation"

    def originalAuthor_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_originalnewauthornew_change",
            args=[obj.originalAuthor_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.originalAuthor_ref)
        return mark_safe(link)

    originalAuthor_link.short_description = "Author"

    def translationTranslator_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translationnewtranslatornew_change",
            args=[obj.translationTranslator_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translationTranslator_ref)
        return mark_safe(link)

    translationTranslator_link.short_description = "Translator"
