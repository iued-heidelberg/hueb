from django.contrib import admin

# Register your models here.
from .models import (
    Archive,
    Country,
    DdcGerman,
    Document,
    Language,
    Location,
    Person,
    SourceReference,
    YearRange,
)


class SourceReferenceInline(admin.TabularInline):
    model = SourceReference
    extra = 0
    autocomplete_fields = ("app", "model")


@admin.register(YearRange)
class YearRangeAdmin(admin.ModelAdmin):
    list_display = ("id", "timerange", "start_uncertainty", "end_uncertainty")
    search_fields = ("timerange", "id")
    fieldsets = (
        (
            "Timerange Information",
            {
                "description": ("Daterange information"),
                "fields": (
                    "timerange",
                    "start_uncertainty",
                    "end_uncertainty",
                    "parsed_string",
                ),
            },
        ),
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lifetime", "alias", "is_alias")
    search_fields = ("name", "id")
    fieldsets = (
        (
            "Person Information",
            {
                "description": ("All known data about a person"),
                "fields": ("name", "lifetime", "alias", "is_alias"),
            },
        ),
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "country",
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
    )


@admin.register(DdcGerman)
class DdcGermanAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ddc_number",
        "ddc_name",
    )
    search_fields = ("ddc_number", "ddc_name")

    fieldsets = (
        (
            "DDC Information",
            {"description": (" "), "fields": ("ddc_number", "ddc_name")},
        ),
    )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "language",
    )
    search_fields = ("language", "id")

    fieldsets = (
        ("Language Information", {"description": (" "), "fields": ("language",)}),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "adress",
        "country",
        "hostname",
        "ip",
        "z3950_gateway",
    )

    search_fields = ("name", "address", "country")

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
    )


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ("id", "signatur", "link")
    search_fields = ("signatur", "id")
    fieldsets = (
        (
            "Archive Information",
            {
                "description": ("Stores the archive locations of documents"),
                "fields": ("signatur", "link"),
            },
        ),
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "published",
        "published_location",
        "edition",
        "language",
        "published",
        "ddc",
    )
    search_fields = ("id", "title", "author")
    fieldsets = (
        (
            "Document Information",
            {
                "description": ("Stores the information known about documents"),
                "fields": (
                    "title",
                    "subtitle",
                    "published",
                    "publisher",
                    "author",
                    "translated_from",
                    "translated_to",
                    "published_location",
                    "edition",
                    "language",
                    "year_published",
                    "country",
                    "ddc",
                    "archive",
                ),
            },
        ),
    )
