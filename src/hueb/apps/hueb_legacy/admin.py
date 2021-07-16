from django.contrib import admin
from import_export.admin import ExportMixin

from .models import (
    Author,
    Collection,
    Country,
    DdcGerman,
    Language,
    LocAssign,
    Location,
    ManualKeys,
    OrigAssign,
    Original,
    PndAlias,
    PndMain,
    PndTitle,
    SwdMain,
    SwdTerm,
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


@admin.register(Collection)
class CollectionAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "title",
        "editor",
        "migration_notes",
        "migration_generated",
    )
    search_fields = ("title", "id", "editor")
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Collection Information",
            {
                "fields": ("title", "editor"),
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


@admin.register(Country)
class CountryAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "country",
        "migration_notes",
        "migration_generated",
    )
    search_fields = (
        "country",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Country Information",
            {
                "fields": ("country",),
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


@admin.register(LocAssign)
class LocAssignAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "location",
        "original",
        "translation",
        "signatur",
        "migration_notes",
        "migration_generated",
    )
    search_fields = (
        "location__name",
        "original__title",
        "translation__title",
        "signatur",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "LocAssign Information",
            {
                "fields": (
                    "id",
                    "location",
                    "original",
                    "translation",
                    "signatur",
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
            super(LocAssignAdmin, self)
            .get_queryset(request)
            .prefetch_related("translation")
            .prefetch_related("original")
            .prefetch_related("location")
        )
        return qs


@admin.register(Location)
class LocationAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "name",
        "adress",
        "country",
        "hostname",
        "ip",
        "z3950_gateway",
        "migration_notes",
        "migration_generated",
    )
    search_fields = (
        "name",
        "adress",
        "country__country",
        "hostname",
        "ip",
        "z3950_gateway",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "Location Information",
            {
                "fields": (
                    "id",
                    "name",
                    "adress",
                    "country",
                    "hostname",
                    "ip",
                    "z3950_gateway",
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
            super(LocationAdmin, self).get_queryset(request).prefetch_related("country")
        )
        return qs


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
            .prefetch_related("original")
            .prefetch_related("translation")
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
            .prefetch_related("original")
            .prefetch_related("translation")
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
            .select_related("collection")
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
        "ddc",
        "real_year",
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
        "real_year",
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
                    "collection",
                    "publisher",
                    "published_location",
                    "edition",
                    "via_language",
                    "language",
                    "comment",
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
            super(TranslationAdmin, self)
            .get_queryset(request)
            .select_related("author")
            .select_related("translator")
            .select_related("collection")
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


@admin.register(PndAlias)
class PndAliasAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "pnd",
        "pnd_alias",
        "migration_generated",
    )
    search_fields = (
        "pnd__person",
        "pnd_alias",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "PndAlias Information",
            {
                "fields": ("id", "pnd", "pnd_alias"),
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
        qs = super(PndAliasAdmin, self).get_queryset(request).select_related("pnd")
        return qs


@admin.register(PndMain)
class PndMainAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "person",
        "migration_generated",
    )
    search_fields = (
        "id",
        "person",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "PndMain Information",
            {
                "fields": ("id", "person"),
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


@admin.register(PndTitle)
class PndTitleAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "pnd",
        "pnd_title",
        "migration_generated",
    )
    search_fields = (
        "pnd__person",
        "pnd_title",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "PndTitle Information",
            {
                "fields": ("id", "pnd_title", "pnd"),
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
        qs = super(PndTitleAdmin, self).get_queryset(request).select_related("pnd")
        return qs


@admin.register(SwdMain)
class SwdMainAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "number_800_hauptschlagwort",
        "number_801_unterschlagwort1",
        "number_802_unterschlagwort2",
        "migration_generated",
    )
    search_fields = (
        "number_800_hauptschlagwort",
        "number_801_unterschlagwort1",
        "number_802_unterschlagwort2",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "SwdMain Information",
            {
                "fields": (
                    "id",
                    "number_800_hauptschlagwort",
                    "number_801_unterschlagwort1",
                    "number_802_unterschlagwort2",
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


@admin.register(SwdTerm)
class SwdTermAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "number_820_alternativform",
        "number_830_aequivalentebezeichnung",
        "number_845_oberbegriff",
        "number_850_uebergeordnetesschlagwort",
        "number_860_verwandtesschlagwort",
        "swd",
        "migration_generated",
    )
    search_fields = (
        "number_820_alternativform",
        "number_830_aequivalentebezeichnung",
        "number_845_oberbegriff",
        "number_850_uebergeordnetesschlagwort",
        "number_860_verwandtesschlagwort",
        "swd__number_800_hauptschlagwort",
        "id",
    )
    list_filter = ("migration_generated",)

    fieldsets = (
        (
            "SwdTerm Information",
            {
                "fields": (
                    "id",
                    "number_820_alternativform",
                    "number_830_aequivalentebezeichnung",
                    "number_845_oberbegriff",
                    "number_850_uebergeordnetesschlagwort",
                    "number_860_verwandtesschlagwort",
                    "swd",
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
        qs = super(SwdTermAdmin, self).get_queryset(request).select_related("swd")
        return qs
