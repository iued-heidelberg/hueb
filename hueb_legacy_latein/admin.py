# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, Translator, TranslatorNew, Author, AuthorNew, Country, DdcGerman, Language, LocAssign, Location, LocationNew, OrigAssign, Original, OriginalNew, Translation, TranslationNew, OriginalAuthor, OriginalAuthorNew, OriginalNewAuthor, OriginalNewAuthorNew, TranslationNewTranslator, TranslationNewTranslatorNew, TranslationTranslator, TranslationTranslatorNew


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'loginname', 'passwort', 'anmerkungen')
    search_fields = ('name',)


@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'comment',
        'name',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('user',)
    search_fields = ('name',)


@admin.register(TranslatorNew)
class TranslatorNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'comment',
        'name',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('user',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'comment',
        'name',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('user',)
    search_fields = ('name',)


@admin.register(AuthorNew)
class AuthorNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'comment',
        'name',
        'user',
        'datum',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('user',)
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'country',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('migration_generated',)


@admin.register(DdcGerman)
class DdcGermanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ddc_number',
        'ddc_name',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('migration_generated',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('migration_generated',)


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
    search_fields = ('name',)


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
    search_fields = ('name',)


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


@admin.register(Original)
class OriginalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ddc',
        'title',
        'subtitle',
        'subtitle1',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language',
        'comment',
        'real_year',
        'link',
        'user',
        'datum',
        'country',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('ddc', 'language', 'user', 'country', 'author',
        'author_new')


@admin.register(OriginalNew)
class OriginalNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ddc',
        'title',
        'subtitle',
        'subtitle1',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language',
        'comment',
        'real_year',
        'link',
        'user',
        'datum',
        'country_id',
        'migration_notes',
        'migration_generated',
    )
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('ddc', 'language', 'user')


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ddc',
        'author_id',
        'title',
        'subtitle',
        'subtitle1',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language_id',
        'via_language',
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
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('ddc', 'via_language', 'user', 'country', 'author_new')


@admin.register(TranslationNew)
class TranslationNewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ddc',
        'author_id',
        'title',
        'subtitle',
        'subtitle1',
        'year',
        'publisher',
        'published_location',
        'edition',
        'language_id',
        'via_language',
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
    list_filter = ('datum', 'migration_generated')
    raw_id_fields = ('ddc', 'via_language', 'user', 'country', 'author_new')


@admin.register(OriginalAuthor)
class OriginalAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'original', 'author')
    raw_id_fields = ('original', 'author')


@admin.register(OriginalAuthorNew)
class OriginalAuthorNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'original', 'author')
    raw_id_fields = ('original', 'author')


@admin.register(OriginalNewAuthor)
class OriginalNewAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'original', 'author')
    raw_id_fields = ('original', 'author')


@admin.register(OriginalNewAuthorNew)
class OriginalNewAuthorNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_new', 'author')
    raw_id_fields = ('original_new', 'author')


@admin.register(TranslationNewTranslator)
class TranslationNewTranslatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'translation', 'translator')
    raw_id_fields = ('translation', 'translator')


@admin.register(TranslationNewTranslatorNew)
class TranslationNewTranslatorNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'translation_new', 'translator')
    raw_id_fields = ('translation_new', 'translator')


@admin.register(TranslationTranslator)
class TranslationTranslatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'translation', 'translator')
    raw_id_fields = ('translation', 'translator')


@admin.register(TranslationTranslatorNew)
class TranslationTranslatorNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'translation', 'translator')
    raw_id_fields = ('translation', 'translator')
