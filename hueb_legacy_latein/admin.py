from django.contrib import admin

from .models import User, Translator, TranslatorNew, Author, AuthorNew, Country, DdcGerman, Language, LocAssign, Location, LocationNew, OrigAssign, Original, OriginalNew, Translation, TranslationNew, OriginalAuthor, OriginalAuthorNew, OriginalNewAuthor, OriginalNewAuthorNew, TranslationNewTranslator, TranslationNewTranslatorNew, TranslationTranslator, TranslationTranslatorNew


class OriginalAuthorInline(admin.TabularInline):
    model = OriginalAuthor
    extra = 0

class OriginalAuthorNewInline(admin.TabularInline):
    model = OriginalAuthorNew
    extra = 0

class OriginalNewAuthorInline(admin.TabularInline):
    model = OriginalNewAuthor
    extra = 0

class OriginalNewAuthorNewInline(admin.TabularInline):
    model = OriginalNewAuthorNew
    extra = 0

class TranslationTranslatorInline(admin.TabularInline):
    model = TranslationTranslator
    extra = 0

class TranslationTranslatorNewInline(admin.TabularInline):
    model = TranslationTranslatorNew
    extra = 0

class TranslationNewTranslatorInline(admin.TabularInline):
    model = TranslationNewTranslator
    extra = 0

class TranslationNewTranslatorNewInline(admin.TabularInline):
    model = TranslationNewTranslatorNew
    extra = 0

@admin.register(OrigAssign)
class OrigAssignAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'orig_id',
        'trans_id',
        'orig_diff',
        'trans_diff',
        'migration_notes',
        'migration_generated',
        'orig_new_id',
        'trans_new_id',
        'orig_diff_new',
        'trans_diff_new',
    )
    list_filter = ('migration_generated',)
    raw_id_fields = (
        'orig_diff',
        'trans_diff',
        'orig_diff_new',
        'trans_diff_new',
    )

@admin.register(LocAssign)
class LocAssignAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'loc',
        'orig',
        'trans',
        'signatur',
        'migration_notes',
        'migration_generated',
        'loc_new',
        'orig_new',
        'trans_new',
    )
    list_filter = ('migration_generated',)
    raw_id_fields = (
        'loc',
        'orig',
        'trans',
        'loc_new',
        'orig_new',
        'trans_new',
    )

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'loginname', 'anmerkungen')
    search_fields = ('name', 'id')

    fieldsets = (
        ('User Information', {
            'description': ('Information stored about the user'),
            'fields': ('name', 'loginname', 'passwort', 'anmerkungen')
        })),

@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'comment',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',

    )
    search_fields = ('name', 'id')
    list_filter = ('datum', 'migration_generated')

    fieldsets = (
        ('Translator Information', {
            'description': ('Information stored about the translator'),
            'fields': ('name', 'comment')
        }),
        ('Metadata', {
            'description': ('Information about the original creator of this entry'),
            'fields': ('user', 'datum'),
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )

@admin.register(TranslatorNew)
class TranslatorNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'comment',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',

    )
    search_fields = ('name', 'id')
    list_filter = ('datum', 'migration_generated')

    fieldsets = (
        ('Translator Information', {
            'description': ('Information stored about the translator'),
            'fields': ('name', 'comment')
        }),
        ('Metadata', {
            'description': ('Information about the original creator of this entry'),
            'fields': ('user', 'datum'),
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'comment',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',

    )
    search_fields = ('name', 'id')
    list_filter = ('datum', 'migration_generated')

    fieldsets = (
        ('Author Information', {
            'description': ('Information stored about the author'),
            'fields': ('name', 'comment')
        }),
        ('Metadata', {
            'description': ('Information about the original creator of this entry'),
            'fields': ('user', 'datum'),
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )


@admin.register(AuthorNew)
class AuthorNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'comment',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',

    )
    search_fields = ('name', 'id')
    list_filter = ('datum', 'migration_generated')

    fieldsets = (
        ('Author Information', {
            'description': ('Information stored about the author'),
            'fields': ('name', 'comment')
        }),
        ('Metadata', {
            'description': ('Information about the original creator of this entry'),
            'fields': ('user', 'datum'),
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'country',
        'migration_notes',
        'migration_generated',
    )
    search_fields = ('country', 'id')
    fieldsets = (
        ('Country Information', {
            'description': ('Information stored about the country'),
            'fields': ('country',)
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )



@admin.register(DdcGerman)
class DdcGermanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ddc_number',
        'ddc_name',
        'migration_notes',
        'migration_generated',
    )
    search_fields = ('ddc_number', 'ddc_name')

    fieldsets = (
        ('DDC Information', {
            'description': (' '),
            'fields': ('ddc_number', 'ddc_name')
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )



@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'migration_notes',
        'migration_generated',
    )
    search_fields = ('language', 'id')

    fieldsets = (
        ('Language Information', {
            'description': (' '),
            'fields': ('language',)
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )





@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'adress',
        'country',
        'hostname',
        'ip',
        'z3950_gateway',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('migration_generated',)
    search_fields = ('name','address', 'country')

    fieldsets = (
        ('Location Information', {
            'description': (' '),
            'fields': ('name','adress', 'country', 'hostname', 'ip', 'z3950_gateway')
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )


@admin.register(LocationNew)
class LocationNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'adress',
        'country',
        'hostname',
        'ip',
        'z3950_gateway',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('migration_generated',)
    search_fields = ('name','address', 'country')

    fieldsets = (
        ('Location Information', {
            'description': (' '),
            'fields': ('name','adress', 'country', 'hostname', 'ip', 'z3950_gateway')
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )





@admin.register(Original)
class OriginalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'subtitle',
        'subtitle1',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language',
        'comment',
        'ddc',
        'real_year',
        'link',
        'user',
        'datum',
        'country',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('migration_generated',)
    search_fields = ('title','subtitle', 'subtitle1', 'year', 'publisher', 'published_location')

    fieldsets = (
        ('Original Information', {
            'description': (' '),
            'fields': ('title','subtitle', 'subtitle1', 'year', 'publisher', 'published_location', 'edition', 'language', 'real_year', 'country')
        }),
         ('Original Metadata', {
            'description': (' '),
            'fields': ('ddc', 'comment', 'link', 'user', 'datum')
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )

    inlines = [OriginalAuthorInline, ]


@admin.register(OriginalNew)
class OriginalNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'subtitle',
        'subtitle1',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language',
        'comment',
        'ddc',
        'real_year',
        'link',
        'user',
        'datum',
        'country_id',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('migration_generated',)
    search_fields = ('title','subtitle', 'subtitle1', 'year', 'publisher', 'published_location')

    fieldsets = (
        ('Original Information', {
            'description': (' '),
            'fields': ('title','subtitle', 'subtitle1', 'year', 'publisher', 'published_location', 'edition', 'language', 'real_year', 'country_id')
        }),
         ('Original Metadata', {
            'description': (' '),
            'fields': ('ddc', 'comment', 'link', 'user', 'datum')
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )

    inlines = [OriginalNewAuthorNewInline, ]


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'subtitle',
        'subtitle1',
        'author_id',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language_id',
        'via_language',
        'ddc',
        'comment',
        'real_year',
        'link',
        'user',
        'datum',
        'country',
        'migration_notes',
        'migration_generated',
        'author_new',
    )
    list_filter = ('migration_generated',)
    search_fields = ('title','subtitle', 'subtitle1', 'year', 'publisher', 'published_location')

    fieldsets = (
        ('Original Information', {
            'description': (' '),
            'fields': ('title','subtitle', 'subtitle1', 'author_id', 'year', 'publisher', 'published_location', 'edition', 'language_id', 'via_language', 'real_year', 'country')
        }),
         ('Original Metadata', {
            'description': (' '),
            'fields': ('ddc', 'comment', 'link', 'user', 'datum')
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )

    inlines = [TranslationTranslatorInline, ]

@admin.register(TranslationNew)
class TranslationNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'subtitle',
        'subtitle1',
        'author_id',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language_id',
        'via_language',
        'ddc',
        'comment',
        'real_year',
        'link',
        'user',
        'datum',
        'country',
        'migration_notes',
        'migration_generated',
        'author_new',
    )
    list_filter = ('migration_generated',)
    search_fields = ('title','subtitle', 'subtitle1', 'year', 'publisher', 'published_location')

    fieldsets = (
        ('Original Information', {
            'description': (' '),
            'fields': ('title','subtitle', 'subtitle1', 'author_id', 'year', 'publisher', 'published_location', 'edition', 'language_id', 'via_language', 'real_year', 'country')
        }),
         ('Original Metadata', {
            'description': (' '),
            'fields': ('ddc', 'comment', 'link', 'user', 'datum')
        }),
        ('Migration', {
            'description': ('Migration metadata'),
            'classes': ('collapse',),
            'fields': ('migration_notes', 'migration_generated'),
        }),
    )

    inlines = [TranslationNewTranslatorNewInline, ]