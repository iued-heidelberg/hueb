from django.contrib import admin
from import_export.admin import ExportMixin

from .models import (
    AuthorNew,
    Country,
    DdcGerman,
    Language,
    LocAssign,
    LocationNew,
    OrigAssign,
    OriginalNew,
    OriginalNewAuthorNew,
    TranslationNew,
    TranslationNewTranslatorNew,
    TranslatorNew,
    User,
)


class ReadonlyAdmin(ExportMixin, admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OriginalNewAuthorNewInline(admin.TabularInline):
    model = OriginalNewAuthorNew
    extra = 0
    autocomplete_fields = ("author", "original")


class TranslationNewTranslatorNewInline(admin.TabularInline):
    model = TranslationNewTranslatorNew
    extra = 0
    autocomplete_fields = ("translation", "translator")


class LocAssignInline(admin.TabularInline):
    model = LocAssign
    fields = ("loc_new", "signatur")
    autocomplete_fields = ("loc_new",)
    extra = 0


class OrigAssignInline(admin.TabularInline):
    model = OrigAssign
    fk_name = "trans"
    fields = ("id", "orig")
    autocomplete_fields = ("orig",)
    extra = 0


class TransAssignInline(admin.TabularInline):
    model = OrigAssign
    fk_name = "orig"
    fields = ("id", "trans")
    autocomplete_fields = ("trans",)
    extra = 0


class OrigNewAssignInline(admin.TabularInline):
    model = OrigAssign
    fk_name = "trans_new"
    fields = ("id", "orig_new")
    autocomplete_fields = ("orig_new",)
    extra = 0


class TransNewAssignInline(admin.TabularInline):
    model = OrigAssign
    fk_name = "orig_new"
    fields = ("id", "trans_new")
    autocomplete_fields = ("trans_new",)
    extra = 0


@admin.register(OrigAssign)
class OrigAssignAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "orig",
        "trans",
        "orig_new",
        "trans_new",
        "migration_notes",
        "migration_generated",
        "orig_diff",
        "trans_diff",
        "orig_diff_new",
        "trans_diff_new",
    )
    list_filter = ("migration_generated",)
    autocomplete_fields = (
        "orig_new",
        "trans_new",
        "orig_diff_new",
        "trans_diff_new",
    )

    def get_queryset(self, request):
        qs = (
            super(OrigAssignAdmin, self)
            .get_queryset(request)
            .select_related("orig")
            .select_related("trans")
            .select_related("orig_new")
            .select_related("trans_new")
            .select_related("orig_diff")
            .select_related("trans_diff")
            .select_related("orig_diff_new")
            .select_related("trans_diff_new")
        )
        return qs

    fieldsets = (
        ("Old relationships", {"description": (" "), "fields": ("orig", "trans")}),
        (
            "New relationships",
            {"description": (" "), "fields": ("orig_new", "trans_new")},
        ),
        (
            "Old diff relationships",
            {"description": (" "), "fields": ("orig_diff", "trans_diff")},
        ),
        (
            "New diff relationships",
            {"description": (" "), "fields": ("orig_diff_new", "trans_diff_new")},
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
        "loc",
        "orig",
        "trans",
        "signatur",
        "loc_new",
        "orig_new",
        "trans_new",
        "migration_notes",
        "migration_generated",
    )
    list_filter = ("migration_generated",)
    autocomplete_fields = (
        "loc_new",
        "orig_new",
        "trans_new",
    )

    fieldsets = (
        (
            "Old relationships",
            {"description": (" "), "fields": ("loc", "orig", "trans")},
        ),
        (
            "New relationships",
            {"description": (" "), "fields": ("loc_new", "orig_new", "trans_new")},
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
            .select_related("orig")
            .select_related("trans")
            .select_related("loc")
            .select_related("orig_new")
            .select_related("trans_new")
            .select_related("loc_new")
        )
        return qs


@admin.register(User)
class UserAdmin(ReadonlyAdmin):
    list_display = ("id", "name", "loginname", "anmerkungen")
    search_fields = ("name", "id")

    fieldsets = (
        (
            (
                "User Information",
                {
                    "description": ("Information stored about the user"),
                    "fields": ("name", "loginname", "passwort", "anmerkungen"),
                },
            )
        ),
    )


@admin.register(TranslatorNew)
class TranslatorNewAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "name",
        "comment",
        "user",
        "datum",
        "migration_notes",
        "migration_generated",
    )
    search_fields = ("name", "id")
    list_filter = ("datum", "migration_generated")

    fieldsets = (
        (
            "Translator Information",
            {
                "description": ("Information stored about the translator"),
                "fields": ("name", "comment"),
            },
        ),
        (
            "Metadata",
            {
                "description": ("Information about the original creator of this entry"),
                "fields": ("user", "datum"),
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
    inlines = [
        TranslationNewTranslatorNewInline,
    ]

    def get_queryset(self, request):
        qs = (
            super(TranslatorNewAdmin, self).get_queryset(request).select_related("user")
        )
        return qs


@admin.register(AuthorNew)
class AuthorNewAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "name",
        "comment",
        "user",
        "datum",
        "migration_notes",
        "migration_generated",
    )
    search_fields = ("name", "id")
    list_filter = ("datum", "migration_generated")

    fieldsets = (
        (
            "Author Information",
            {
                "description": ("Information stored about the author"),
                "fields": ("name", "comment"),
            },
        ),
        (
            "Metadata",
            {
                "description": ("Information about the original creator of this entry"),
                "fields": ("user", "datum"),
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

    inlines = [
        OriginalNewAuthorNewInline,
    ]

    def get_queryset(self, request):
        qs = super(AuthorNewAdmin, self).get_queryset(request).select_related("user")
        return qs


@admin.register(Country)
class CountryAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "country",
        "migration_notes",
        "migration_generated",
    )
    search_fields = ("country", "id")
    fieldsets = (
        (
            "Country Information",
            {
                "description": ("Information stored about the country"),
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
    search_fields = ("ddc_number", "ddc_name")

    fieldsets = (
        (
            "DDC Information",
            {"description": (" "), "fields": ("ddc_number", "ddc_name")},
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
    search_fields = ("language", "id")

    fieldsets = (
        ("Language Information", {"description": (" "), "fields": ("language",)}),
        (
            "Migration",
            {
                "description": ("Migration metadata"),
                "classes": ("collapse",),
                "fields": ("migration_notes", "migration_generated"),
            },
        ),
    )


@admin.register(LocationNew)
class LocationNewAdmin(ReadonlyAdmin):
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
    list_filter = ("migration_generated",)
    search_fields = ("name", "adress", "country")

    fieldsets = (
        (
            "Location Information",
            {
                "description": (" "),
                "fields": (
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


@admin.register(OriginalNew)
class OriginalNewAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "subtitle1",
        "year",
        "publisher",
        "published_location",
        "edition",
        "language",
        "comment",
        "ddc",
        "real_year",
        "link",
        "user",
        "datum",
        "country",
        "migration_notes",
        "migration_generated",
    )
    list_filter = ("migration_generated",)
    search_fields = (
        "title",
        "subtitle",
        "subtitle1",
        "year",
        "publisher",
        "published_location",
    )
    autocomplete_fields = ("ddc",)

    def get_queryset(self, request):
        qs = (
            super(OriginalNewAdmin, self)
            .get_queryset(request)
            .select_related("language")
            .select_related("ddc")
            .select_related("user")
            .select_related("country")
            # .select_related("person")
            .select_related("document")
            .select_related("documentrelationship")
            # .select_related("author_new")
        )
        return qs

    fieldsets = (
        (
            "Original Information",
            {
                "description": (" "),
                "fields": (
                    "title",
                    "subtitle",
                    "subtitle1",
                    "year",
                    "publisher",
                    "published_location",
                    "edition",
                    "language",
                    "real_year",
                    "country",
                ),
            },
        ),
        (
            "Original Metadata",
            {
                "description": (" "),
                "fields": ("ddc", "comment", "link", "user", "datum"),
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

    inlines = [OriginalNewAuthorNewInline, LocAssignInline, TransNewAssignInline]


@admin.register(TranslationNew)
class TranslationNewAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "subtitle1",
        "author",
        "year",
        "publisher",
        "published_location",
        "edition",
        "language",
        "via_language",
        "ddc",
        "comment",
        "real_year",
        "link",
        "user",
        "datum",
        "country",
        "migration_notes",
        "migration_generated",
        "author_new",
    )
    list_filter = ("migration_generated",)
    search_fields = (
        "title",
        "subtitle",
        "subtitle1",
        "year",
        "publisher",
        "published_location",
    )
    autocomplete_fields = ("author_new", "ddc")

    fieldsets = (
        (
            "Original Information",
            {
                "description": (" "),
                "fields": (
                    "title",
                    "subtitle",
                    "subtitle1",
                    "author",
                    "year",
                    "publisher",
                    "published_location",
                    "edition",
                    "language",
                    "via_language",
                    "real_year",
                    "country",
                ),
            },
        ),
        (
            "Original Metadata",
            {
                "description": (" "),
                "fields": ("ddc", "comment", "link", "user", "datum"),
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
            super(TranslationNewAdmin, self)
            .get_queryset(request)
            .select_related("language")
            .select_related("via_language")
            .select_related("author")
            .select_related("author_new")
            .select_related("ddc")
            .select_related("user")
            .select_related("country")
            # .select_related("person")
            .select_related("document")
            .select_related("documentrelationship")
        )
        return qs

    inlines = [TranslationNewTranslatorNewInline, LocAssignInline, OrigNewAssignInline]


@admin.register(TranslationNewTranslatorNew)
class TranslationNewTranslatorNewAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "translation",
        "translator",
    )
    autocomplete_fields = (
        "translation",
        "translator",
    )

    def get_queryset(self, request):
        qs = (
            super(TranslationNewTranslatorNewAdmin, self)
            .get_queryset(request)
            .select_related("translation")
            .select_related("translator")
        )
        return qs

    fieldsets = (
        (
            "Relationship",
            {"description": (" "), "fields": ("translation", "translator")},
        ),
    )


@admin.register(OriginalNewAuthorNew)
class OriginalNewAuthorNewAdmin(ReadonlyAdmin):
    list_display = (
        "id",
        "original",
        "author",
    )
    autocomplete_fields = (
        "original",
        "author",
    )

    def get_queryset(self, request):
        qs = (
            super(OriginalNewAuthorNewAdmin, self)
            .get_queryset(request)
            .select_related("original")
            .select_related("author")
        )
        return qs

    fieldsets = (
        (
            "Relationship",
            {"description": (" "), "fields": ("original", "author")},
        ),
    )
