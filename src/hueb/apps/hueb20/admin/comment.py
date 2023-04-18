from django.contrib import admin
from hueb.apps.hueb20.admin.tenant import TenantAdmin
from hueb.apps.hueb20.models import Comment
from import_export.admin import ExportMixin
from simple_history.admin import SimpleHistoryAdmin


class CommentInline(admin.TabularInline):
    model = Comment
    fields = (
        "external",
        "text",
    )
    readonly_fields = (
        "app",
        "id",
    )
    extra = 0
    verbose_name = "Comment"
    verbose_name_plural = verbose_name + "s"


@admin.register(Comment)
class CommentAdmin(ExportMixin, SimpleHistoryAdmin, TenantAdmin):
    model = Comment
    fields = (
        "id",
        "text",
        "person",
        "document",
        "external",
    )
    readonly_fields = (
        "id",
        "app",
        "text",
        "person",
        "document",
    )
    extra = 0
    verbose_name = "Comment"
    verbose_name_plural = verbose_name + "s"
