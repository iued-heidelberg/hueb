from django.contrib import admin, messages
from django.contrib.postgres.fields import IntegerRangeField
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb20.admin.review import ReviewAdmin
from hueb.apps.hueb20.admin.tenant import TenantAdminReadOnly
from hueb.apps.hueb20.models import Person
from hueb.apps.hueb20.widgets.timerange import TimeRangeWidget
from hueb.apps.tenants.admin_site import admin_site
from django.utils.html import format_html
from django.http import HttpResponseRedirect


from .comment import CommentInline


@admin.register(Person, site=admin_site)
class PersonAdmin(ReviewAdmin, TenantAdminReadOnly):
    change_form_template = "admin/person_change_form.html"

    readonly_fields = ("app", "author_link", "translator_link", "id")
    list_display = (
        "id",
        "name",
        "cultural_circle",
        "alias",
        "is_alias",
        "adapt_person_lifetime_start_list_view",
        "adapt_person_lifetime_end_list_view",
        "organisation",
        "state",
    )
    list_filter = ("state", "app")
    search_fields = ("name", "id", "lifetime_start", "lifetime_end")
    autocomplete_fields = (
        "alias",
        "cultural_circle",
        "duplicates",
    )
    formfield_overrides = {IntegerRangeField: {"widget": TimeRangeWidget}}
    fieldsets = (
        (
            "Person Information",
            {
                "description": ("All known data about a person"),
                "fields": (
                    "id",
                    "name",
                    "cultural_circle",
                    "alias",
                    "organisation",
                    "lifetime_start",
                    "lifetime_end",
                    "duplicates",
                ),
            },
        ),
        (
            "Review",
            {"fields": ("state",)},
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "translator_link", "author_link"),
                "classes": ("collapse",),
            },
        ),
    )
    inlines = [CommentInline]

    def author_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_authornew_change", args=[obj.author_ref.id]
        )
        link = '<a href="%s">%s</a>' % (url, obj.author_ref)
        return mark_safe(link)

    author_link.short_description = "Author"

    def translator_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translatornew_change",
            args=[obj.translator_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translator_ref)
        return mark_safe(link)

    translator_link.short_description = "Translator"

    def replace_duplicates(self, request, obj):
        duplicates_ids = request.POST.getlist("duplicates")
        print(duplicates_ids)
        duplicates = Person.objects.filter(id__in=duplicates_ids)
        for duplicate in duplicates:
            # get all contribution objects that reference the duplicate
            # and replace the reference with the new object
            for contribution in duplicate.contribution_set.all():
                contribution.person = obj
                contribution.save()
                # trigger save to update main_author
                if contribution.contribution_type == contribution.WRITER:
                    authors = contribution.document.get_authors()
                    authors = [Person.objects.get(id=x.person.id) for x in authors]
                    authors = sorted(authors, key=lambda x: x.name)
                    contribution.document.main_author = authors[0]
                    contribution.document.save()

            for alias in duplicate.person_set.all():
                alias.person = obj
                alias.save()

            # get comments and replace the reference with the new object
            for comment in duplicate.person_comment.all():
                comment.person = obj
                comment.save()

            # remove the duplicate
            duplicate.delete()

            self.message_user(
                request,
                format_html(
                    "Duplicate {} replaced with {}".format(duplicate.name, obj.name)
                ),
                level=messages.INFO,
            )

    def response_change(self, request, obj):
        if "_replace_duplicates" in request.POST:
            self.message_user(
                request,
                format_html("Person saved. Duplicates replaced!"),
                level=messages.INFO,
            )
            self.replace_duplicates(request, obj)
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    def get_queryset(self, request):
        qs = (
            super()
            .get_queryset(request)
            .select_related("alias")
            .select_related("cultural_circle")
        )
        return qs
