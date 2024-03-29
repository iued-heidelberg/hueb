from django.contrib import admin
from import_export.admin import ExportMixin

from .models import (
    Author,
    DdcGerman,
    Filter,
    Language,
    LidosEx,
    ManualKeys,
    OrigAssign,
    Original,
    Translation,
    Translator,
)


class ReadonlyAdmin(ExportMixin, admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Author)
class AuthorAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "name",
        "comment",
        "migration_notes",
        "migration_generated",
    )
    search_fields = ("name", "id", "comment")
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Author Information",
            {
                "description": ("Information stored about the author"),
                "fields": ("name", "comment"),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )


@admin.register(DdcGerman)
class DdcGermanAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "ddc_number",
        "ddc_name",
        "migration_notes",
        "migration_generated",
    )
    search_fields = ("ddc_number", "id", "ddc_name")
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "DDC Information",
            {
                "fields": ("ddc_number", "ddc_name"),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )


@admin.register(Filter)
class FilterAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "a",
        "b",
        "c",
        "d",
        "migration_notes",
        "migration_generated",
    )
    search_fields = ("a", "id", "b", "c", "d")
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Filter Information",
            {
                "fields": ("a", "b", "c", "d"),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )


@admin.register(Language)
class LanguageAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "language",
        "migration_notes",
        "migration_generated",
    )
    search_fields = (
        "language",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Language Information",
            {
                "fields": ("language",),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )


@admin.register(LidosEx)
class LidosExAdmin(ReadonlyAdmin):
    list_display = (
        "number_01",
        "number_03",
        "number_04",
        "number_05",
        "number_06",
        "number_11",
        "number_1a",
        "number_12",
        "number_13",
        "number_15",
        "number_20",
        "number_21",
        "number_2a",
        "number_22",
        "number_23",
        "number_51",
        "number_52",
        "number_60",
        "number_61",
        "number_62",
        "number_63",
        "deskriptoren",
        "number_25",
        "migration_notes",
        "migration_generated",
    )
    search_fields = (
        "number_01",
        "number_03",
        "number_04",
        "number_05",
        "number_06",
        "number_11",
        "number_1a",
        "number_12",
        "number_13",
        "number_15",
        "number_20",
        "number_21",
        "number_2a",
        "number_22",
        "number_23",
        "number_51",
        "number_52",
        "number_60",
        "number_61",
        "number_62",
        "number_63",
        "deskriptoren",
        "number_25",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Language Information",
            {
                "fields": (
                    "number_01",
                    "number_03",
                    "number_04",
                    "number_05",
                    "number_06",
                    "number_11",
                    "number_1a",
                    "number_12",
                    "number_13",
                    "number_15",
                    "number_20",
                    "number_21",
                    "number_2a",
                    "number_22",
                    "number_23",
                    "number_25",
                    "number_51",
                    "number_52",
                    "number_60",
                    "number_61",
                    "number_62",
                    "number_63",
                    "deskriptoren",
                ),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )


@admin.register(ManualKeys)
class ManualKeysAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "original",
        "translation",
        "term",
        "migration_generated",
    )
    search_fields = (
        "original__title",
        "translation__title",
        "term",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Language Information",
            {
                "fields": ("original", "translation", "term"),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )

    def get_queryset(self, request):
        qs = (
            super(ManualKeysAdmin, self)
            .get_queryset(request)
            .select_related("original")
            .select_related("translation")
        )
        return qs


@admin.register(OrigAssign)
class OrigAssignAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "original",
        "translation",
        "migration_generated",
    )
    search_fields = (
        "original__title",
        "translation__title",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Language Information",
            {
                "fields": (
                    "original",
                    "translation",
                ),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )

    def get_queryset(self, request):
        qs = (
            super(OrigAssignAdmin, self)
            .get_queryset(request)
            .select_related("original")
            .select_related("translation")
        )
        return qs


@admin.register(Original)
class OriginalAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "author",
        "year",
        "publisher",
        "published_location",
        "edition",
        "language",
        "comment",
        "manual_keys",
        "ddc",
        "real_year",
        "migration_generated",
    )
    search_fields = (
        "id",
        "title",
        "subtitle",
        "author__name",
        "year",
        "publisher",
        "published_location",
        "edition",
        "language__language",
        "comment",
        "manual_keys__term",
        "real_year",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Language Information",
            {
                "fields": (
                    "id",
                    "title",
                    "subtitle",
                    "author",
                    "year",
                    "publisher",
                    "published_location",
                    "edition",
                    "language",
                    "comment",
                    "manual_keys",
                    "ddc",
                    "real_year",
                ),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )

    def get_queryset(self, request):
        qs = (
            super(OriginalAdmin, self)
            .get_queryset(request)
            .select_related("author")
            .select_related("language")
            .select_related("manual_keys")
            .select_related("ddc")
        )
        return qs


@admin.register(Translation)
class TranslationAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "translator",
        "author",
        "year",
        "publisher",
        "published_location",
        "edition",
        "via_language",
        "language",
        "comment",
        "manual_keys",
        "ddc",
        "real_year",
        "invisible",
        "migration_generated",
    )
    search_fields = (
        "id",
        "title",
        "subtitle",
        "year",
        "publisher",
        "published_location",
        "edition",
        "via_language__language",
        "language__language",
        "comment",
        "manual_keys",
        "real_year",
        "invisible",
        "migration_generated",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Language Information",
            {
                "fields": (
                    "id",
                    "title",
                    "subtitle",
                    "translator",
                    "author",
                    "year",
                    "publisher",
                    "published_location",
                    "edition",
                    "via_language",
                    "language",
                    "comment",
                    "manual_keys",
                    "ddc",
                    "real_year",
                    "invisible",
                ),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )

    def get_queryset(self, request):
        qs = (
            super(TranslationAdmin, self)
            .get_queryset(request)
            .select_related("author")
            .select_related("translator")
            .select_related("language")
            .select_related("via_language")
            .select_related("ddc")
        )
        return qs


@admin.register(Translator)
class TranslatorAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "name",
        "comment",
        "migration_generated",
    )
    search_fields = (
        "name",
        "comment",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Language Information",
            {
                "fields": (
                    "name",
                    "comment",
                ),
            },
        ),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )
