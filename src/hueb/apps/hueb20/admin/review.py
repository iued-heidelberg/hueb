from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from import_export.admin import ExportMixin
from simple_history.admin import SimpleHistoryAdmin
from hueb.apps.hueb20.models.document import DocumentRelationship


class ReviewAdmin(ExportMixin, SimpleHistoryAdmin):
    change_form_template = "admin/review_change_form.html"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        disabled_fields = ("state", "reviewed")

        if not request.user.has_perm("hueb20.can_review"):
            for f in disabled_fields:
                if f in form.base_fields:
                    form.base_fields[f].disabled = True

        return form

    def is_not_linked(self, request, obj):
        return (
            "_save_without_link" not in request.POST
            and not DocumentRelationship.objects.filter(document_from=obj).exists()
            and not DocumentRelationship.objects.filter(document_to=obj).exists()
        )

    def response_change(self, request, obj):
        if "_mark_reviewed" in request.POST:
            if request.user.has_perm("hueb20.can_review"):
                updated = []
                obj.mark_reviewed(updated=updated)
                self.message_user(
                    request,
                    format_html(
                        "Marked as reviewed: \n{}".format(self._list_of_urls(updated))
                    ),
                )
                return HttpResponseRedirect(".")
            else:
                self.message_user(
                    request,
                    format_html(
                        "Not enough permissions to add review. But entry is saved."
                    ),
                    messages.ERROR,
                )
                return HttpResponseRedirect(".")

        return super().response_change(request, obj)

    def _list_of_urls(self, objects):
        links = [inst.linked_name() for inst in objects]
        link_list = "\n ".join(links)
        return link_list


class TabularInlineReviewAdmin(admin.TabularInline):
    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm("hueb20.can_review"):
            return self.readonly_fields + (
                "state",
                "reviewed",
            )
        else:
            return self.readonly_fields
