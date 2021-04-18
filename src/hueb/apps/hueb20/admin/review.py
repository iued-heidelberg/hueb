from django.contrib import admin
from django.http import HttpResponseRedirect
from simple_history.admin import SimpleHistoryAdmin


class ReviewAdmin(SimpleHistoryAdmin):
    change_form_template = "admin/review_change_form.html"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        disabled_fields = ("state", "reviewed")

        if not request.user.has_perm("hueb20.can_review"):
            for f in disabled_fields:
                if f in form.base_fields:
                    form.base_fields[f].disabled = True

        return form

    def response_change(self, request, obj):
        if "_mark_reviewed" in request.POST:
            if request.user.has_perm("hueb20.can_review"):
                updated = []
                obj.mark_reviewed(updated=updated)
                self.message_user(
                    request,
                    "Marked as reviewed: \n{}".format(self._list_of_urls(updated)),
                )
                return HttpResponseRedirect(".")

        return super().response_change(request, obj)

    def _list_of_urls(self, objects):
        links = [inst.linked_name() for inst in objects]
        link_list = "\n - ".join(links)
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
