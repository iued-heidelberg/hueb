from django.contrib import admin
from hueb.apps.tenants.admin_site import admin_site as admin_site_override
from hueb.apps.tenants.utils import tenant_from_request, tenantname_from_request


class TenantAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list.html"

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site_override)

    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        print("GOT HERE")
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        if tenant:
            obj.app = tenant.app
            print(obj.app)
        super().save_model(request, obj, form, change)

    def get_changelist_instance(self, request):
        """
        Return a `ChangeList` instance based on `request`. May raise
        `IncorrectLookupParameters`.
        """
        list_display = self.get_list_display(request)
        list_display_links = self.get_list_display_links(request, list_display)
        # Add the action checkboxes if any actions are available.
        if self.get_actions(request):
            list_display = ["action_checkbox", *list_display]
        sortable_by = self.get_sortable_by(request)
        ChangeList = self.get_changelist(request)
        cl = ChangeList(
            request,
            self.model,
            list_display,
            list_display_links,
            self.get_list_filter(request),
            self.date_hierarchy,
            self.get_search_fields(request),
            self.get_list_select_related(request),
            self.list_per_page,
            self.list_max_show_all,
            self.list_editable,
            self,
            sortable_by,
        )
        cl.tenantname = tenantname_from_request(request)

        return cl
