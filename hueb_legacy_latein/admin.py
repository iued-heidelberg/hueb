from django.contrib import admin
from .models_legacy import *

# Register your models here.
class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'legacy_latein'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


admin.site.register(Author, MultiDBModelAdmin)
admin.site.register(AuthorNew, MultiDBModelAdmin)
admin.site.register(Country, MultiDBModelAdmin)
admin.site.register(DdcGerman, MultiDBModelAdmin)
admin.site.register(Language, MultiDBModelAdmin)
admin.site.register(LocAssign, MultiDBModelAdmin)
admin.site.register(Location, MultiDBModelAdmin)
admin.site.register(LocationNew, MultiDBModelAdmin)
admin.site.register(OrigAssign, MultiDBModelAdmin)
admin.site.register(Original, MultiDBModelAdmin)
admin.site.register(OriginalNew, MultiDBModelAdmin)
admin.site.register(Translation, MultiDBModelAdmin)
admin.site.register(TranslationNew, MultiDBModelAdmin)
admin.site.register(Translator, MultiDBModelAdmin)
admin.site.register(TranslatorNew, MultiDBModelAdmin)
admin.site.register(User, MultiDBModelAdmin)
