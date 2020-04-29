class LegacyRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = {"hueb_legacy_latein"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read hueb_legacy_latein models go to legacy_latein.
        """
        if model._meta.app_label in self.route_app_labels:
            return "legacy_latein"
        return "default"

    def db_for_write(self, model, **hints):
        """
        Attempts to write hueb_legacy_latein models go to legacy_latein.
        """
        if model._meta.app_label in self.route_app_labels:
            return "legacy_latein"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the hueb_legacy_latein app is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the hueb_legacy_latein app only appear in the
        'legacy_latein' database.
        """
        if app_label in self.route_app_labels:
            return db == "legacy_latein"
        return db == "default"
