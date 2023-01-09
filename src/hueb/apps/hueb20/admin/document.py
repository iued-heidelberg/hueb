from copy import deepcopy

import requests
from django.contrib import admin, messages
from django.contrib.postgres.fields import IntegerRangeField
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.contribution import ContributionInline
from hueb.apps.hueb20.admin.review import ReviewAdmin, TabularInlineReviewAdmin
from hueb.apps.hueb20.models import Contribution, Document, Filing
from hueb.apps.hueb20.models.document import DocumentRelationship
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

    change_form_template = "admin/document_change_form.html"

    actions = ["duplicate", "validate_links"]

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
        "serialize_written_in",
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
        "link_status",
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
    search_fields = ("id", "title", "contributions__name", "written_in")
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

    def is_not_linked(self, request, obj):
        return (
            "_save_without_link" not in request.POST
            and not DocumentRelationship.objects.filter(document_from=obj).exists()
            and not DocumentRelationship.objects.filter(document_to=obj).exists()
        )

    def response_add(self, request, obj):
        if self.is_not_linked(request, obj) and "_popup" not in request.get_full_path():
            self.message_user(
                request,
                format_html("Document saved. You forgot to add a linked document!"),
                level=messages.WARNING,
            )
            return HttpResponseRedirect("../{id}/change/".format(id=obj.id))
        return super().response_add(request, obj)

    def response_change(self, request, obj):
        if self.is_not_linked(request, obj) and "_mark_reviewed" not in request.POST:
            self.message_user(
                request,
                format_html("Document saved. You forgot to add a linked document!"),
                level=messages.WARNING,
            )
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    def get_queryset(self, request):
        qs = (
            super(DocumentAdmin, self)
            .get_queryset(request)
            .annotate(archives_count=Count("located_in"))
            .prefetch_related("contribution_set__person")
            .prefetch_related("translations")
            .prefetch_related("filing_set__archive")
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
        return "\n".join([str(filing.archive) for filing in obj.filing_set.all()])

    get_archives.short_description = "Archive"

    def get_publishers(self, obj):
        return "\n".join(
            [
                str(contribution.person)
                if contribution.contribution_type == Contribution.PUBLISHER
                else ""
                for contribution in obj.contribution_set.all()
            ]
        )

    get_publishers.short_description = "Publisher"

    def get_written_by(self, obj):
        return "\n".join(
            [
                str(contribution.person)
                if contribution.contribution_type == Contribution.WRITER
                else ""
                for contribution in obj.contribution_set.all()
            ]
        )

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

    def link_status(self, obj):
        try:
            if (
                not obj.filing_set.filter(archive__name="Online-Version")
                .filter(link_status=False)
                .exists()
            ):
                if (
                    obj.filing_set.filter(archive__name="Online-Version")
                    .filter(link_status=True)
                    .exists()
                ):
                    return True
                return None
            return False
        except Filing.DoesNotExist:
            return None

    """
    def save_related(self, request, form, formsets, change):
        for formset in formsets:
            if formset.model == Filing:
                for filing_form in formset:
                    filing_instance = filing_form.save(commit=False)
                    if not filing_instance.archive:
                        continue
                    if filing_instance.archive.name == "Online-Version":
                        if not change:
                            filing_instance.link_status = True
                        else:
                            try:
                                filing = Filing.objects.get(id=filing_instance.id)
                                if filing.link != filing_instance.link:
                                    filing_instance.link_status = True
                            except Filing.DoesNotExist:
                                filing_instance.link_status = True
                        print(filing_instance.link_status)

                        filing_instance.save()
        super().save_related(request, form, formsets, change)
    """

    def duplicate(self, request, queryset):
        documents = queryset.all()
        for document in documents:
            new_document = deepcopy(document)
            new_document.id = None
            new_document.save()
            for contribution in document.contribution_set.all():
                c = Contribution(
                    person=contribution.person,
                    document=new_document,
                    contribution_type=contribution.contribution_type,
                    originalAuthor_ref=new_document.originalAuthor_ref,
                    translationTranslator_ref=new_document.translationTranslator_ref,
                )
                c.save()
                new_document.contribution_set.add(c)
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

    def validate_links(self, request, queryset):
        documents = queryset.all()
        if len(documents) > 100:
            messages.error(
                request, "Please select 100 or less documents to validate links"
            )
            return
        for document in documents:
            try:
                filings = document.filing_set.filter(
                    archive__name="Online-Version"
                ).all()
                for filing in filings:
                    if not filing.link:
                        filing.link_status = False
                        filing.save()
                    else:
                        try:
                            rq = requests.get(filing.link)
                            if rq.status_code == 200:  # OK success status
                                filing.link_status = True
                                filing.save()
                            else:
                                filing.link_status = False
                                filing.save()
                        except Exception:
                            filing.link_status = False
                            filing.save()
            except Exception:
                continue
