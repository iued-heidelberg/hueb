from django.contrib import admin

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


class ReadonlyAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OriginalNewAuthorNewInline(admin.TabularInline):
    model = OriginalNewAuthorNew
    extra = 0
    autocomplete_fields = ("author", "original_new")


class TranslationNewTranslatorNewInline(admin.TabularInline):
    model = TranslationNewTranslatorNew
    extra = 0
    autocomplete_fields = ("translation_new", "translator")


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

    inlines = [TranslationNewTranslatorNewInline, LocAssignInline, OrigNewAssignInline]
