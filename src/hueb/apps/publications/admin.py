from django.contrib import admin
from .models import Publication

# Register your models here.


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "download_link",
        "description",
    )
    readonly_fields = ("download_link",)
    fieldsets = (
        (
            "Name",
            {
                "fields": (
                    "name",
                    "file",
                    "download_link",
                    "description",
                ),
                # "readonly_fields": ("download_link",),
            },
        ),
    )
