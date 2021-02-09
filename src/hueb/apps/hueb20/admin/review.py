from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin


class ReviewAdmin(SimpleHistoryAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        disabled_fields = ("state", "reviewed")

        if not request.user.has_perm("hueb20.can_review"):
            for f in disabled_fields:
                if f in form.base_fields:
                    form.base_fields[f].disabled = True

        return form


class TabularInlineReviewAdmin(admin.TabularInline):
    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm("hueb20.can_review"):
            return ("state", "reviewed")
        else:

            return ()
