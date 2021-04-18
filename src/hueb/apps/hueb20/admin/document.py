from copy import deepcopy

from django.contrib import admin
from django.contrib.postgres.fields import IntegerRangeField
from django.db.models import Count
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.contribution import ContributionInline
from hueb.apps.hueb20.admin.review import ReviewAdmin, TabularInlineReviewAdmin
from hueb.apps.hueb20.models import Document
from hueb.apps.hueb20.widgets.timerange import TimeRangeWidget

from .comment import CommentInline
from .filing import FilingInline


class TranslationRelationshipInline(TabularInlineReviewAdmin):
    readonly_fields = ("app", "document_to_id")
    model = Document.translations.through
    fk_name = "document_from"
    extra = 0
    verbose_name = "Translation"
    verbose_name_plural = verbose_name + "s"
    autocomplete_fields = ("document_to",)
    fields = (
        "document_to_id",
        "document_to",
        "state",
    )
    exclude = ["reviewed", "original_ref", "translation_ref"]


class OriginalRelationshipInline(TabularInlineReviewAdmin):

    readonly_fields = ("app", "document_from_id")
    model = Document.translations.through
    fk_name = "document_to"
    extra = 0
    verbose_name = "Original"
    verbose_name_plural = verbose_name + "s"
    autocomplete_fields = ("document_from",)
    fields = ("document_from_id", "document_from", "state")
    exclude = ["reviewed", "original_ref", "translation_ref"]


@admin.register(Document)
class DocumentAdmin(ReviewAdmin):

    actions = ["duplicate"]

    autocomplete_fields = ("ddc", "cultural_circle", "language")
    readonly_fields = (
        "id",
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
        "state",
    )
    list_filter = ("state", "app")
    formfield_overrides = {IntegerRangeField: {"widget": TimeRangeWidget}}
    inlines = [
        ContributionInline,
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
                    "id",
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
            "Review",
            {"fields": ("state",)},
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
            "admin:hueb_legacy_latein_origassign_change",
            args=[obj.origAssign_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.origAssign_ref)
        return mark_safe(link)

    origAssign_link.short_description = "Original<->Translation Relationship"

    def original_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_originalnew_change",
            args=[obj.original_ref.id],
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

    def duplicate(self, request, queryset):
        documents = queryset.all()
        for document in documents:
            new_document = deepcopy(document)
            new_document.id = None
            new_document.save()
            for written_by in document.written_by.all():
                new_document.written_by.add(written_by)
            for publisher in document.publishers.all():
                new_document.publishers.add(publisher)
            for translations in document.translations.all():
                new_document.translations.add(translations)
            for filing in document.filing_set.all():
                new_filing = deepcopy(filing)
                new_filing.id = None
                new_filing.save()
                new_filing.document = new_document
                new_filing.archive = filing.archive
                new_filing.save()
            new_document.save()
