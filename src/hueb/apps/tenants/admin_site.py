from django.apps import apps
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.urls import NoReverseMatch, reverse
from django.utils.text import capfirst
from hueb.apps.hueb20.__init__ import Hueb20Config
from hueb.apps.tenants.utils import tenantname_from_request


class TenantAdminSite(AdminSite):
    def has_permission(self, request):
        has_base_permission = super().has_permission(request)
        if not has_base_permission:
            return False
        else:
            try:
                tenantuser = request.user.tenantuser
                has_permission = tenantuser.tenant.name == tenantname_from_request(
                    request
                )
            except User.tenantuser.RelatedObjectDoesNotExist:
                has_permission = tenantname_from_request(request) is None
            return has_permission

    def _build_app_dict(self, request, label=None):
        app_dict = {}

        if label:
            models = {
                m: m_a
                for m, m_a in self._registry.items()
                if m._meta.app_label == label
            }
        else:
            models = self._registry

        for model, model_admin in models.items():
            app_label = model._meta.app_label

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            model_dict = {
                "name": capfirst(model._meta.verbose_name_plural),
                "object_name": model._meta.object_name,
                "perms": perms,
                "admin_url": None,
                "add_url": None,
            }
            if perms.get("change") or perms.get("view"):
                model_dict["view_only"] = not perms.get("change")
                try:
                    model_dict["admin_url"] = reverse(
                        "admin:%s_%s_changelist" % info, current_app=self.name
                    )
                except NoReverseMatch:
                    pass
            if perms.get("add"):
                try:
                    model_dict["add_url"] = reverse(
                        "admin:%s_%s_add" % info, current_app=self.name
                    )
                except NoReverseMatch:
                    pass

            if app_label in app_dict:
                app_dict[app_label]["models"].append(model_dict)
            else:
                app_dict[app_label] = {
                    "name": apps.get_app_config(app_label).verbose_name
                    if not (
                        app_label == Hueb20Config.name.split(".")[-1]
                        and tenantname_from_request(request)
                    )
                    else tenantname_from_request(request),
                    "app_label": app_label,
                    "app_url": reverse(
                        "admin:app_list",
                        kwargs={"app_label": app_label},
                        current_app=self.name,
                    ),
                    "has_module_perms": has_module_perms,
                    "models": [model_dict],
                }

        if label:
            return app_dict.get(label)
        return app_dict


admin_site = TenantAdminSite(name="TenantAdminSite")
