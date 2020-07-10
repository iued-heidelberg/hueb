\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;

ALTER TABLE IF EXISTS author
RENAME TO sueb_latein_author;

ALTER TABLE IF EXISTS author_new
RENAME TO sueb_latein_author_new;

ALTER TABLE IF EXISTS country
RENAME TO sueb_latein_country;

ALTER TABLE IF EXISTS ddc_german
RENAME TO sueb_latein_ddc_german;

ALTER TABLE IF EXISTS "language"
RENAME TO sueb_latein_language;

ALTER TABLE IF EXISTS loc_assign
RENAME TO sueb_latein_loc_assign;

ALTER TABLE IF EXISTS "location"
RENAME TO sueb_latein_location;

ALTER TABLE IF EXISTS location_new
RENAME TO sueb_latein_location_new;

ALTER TABLE IF EXISTS orig_assign
RENAME TO sueb_latein_orig_assign;

ALTER TABLE IF EXISTS original
RENAME TO sueb_latein_original;

ALTER TABLE IF EXISTS original_new
RENAME TO sueb_latein_original_new;

ALTER TABLE IF EXISTS original_author
RENAME TO sueb_latein_original_author;

ALTER TABLE IF EXISTS original_author_new
RENAME TO sueb_latein_original_author_new;

ALTER TABLE IF EXISTS original_new_author
RENAME TO sueb_latein_original_new_author;

ALTER TABLE IF EXISTS original_new_author_new
RENAME TO sueb_latein_original_new_author_new;

ALTER TABLE IF EXISTS translation
RENAME TO sueb_latein_translation;

ALTER TABLE IF EXISTS translation_new
RENAME TO sueb_latein_translation_new;

ALTER TABLE IF EXISTS translation_translator
RENAME TO sueb_latein_translation_translator;

ALTER TABLE IF EXISTS translation_translator_new
RENAME TO sueb_latein_translation_translator_new;

ALTER TABLE IF EXISTS translation_new_translator
RENAME TO sueb_latein_translation_new_translator;

ALTER TABLE IF EXISTS translation_new_translator_new
RENAME TO sueb_latein_translation_new_translator_new;

ALTER TABLE IF EXISTS translator
RENAME TO sueb_latein_translator;

ALTER TABLE IF EXISTS translator_new
RENAME TO sueb_latein_translator_new;

ALTER TABLE IF EXISTS "user"
RENAME TO sueb_latein_user;

ALTER TABLE IF EXISTS sueb_latein_author
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_author_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_country
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_ddc_german
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_language
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_loc_assign
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_location
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_location_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_orig_assign
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_original
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_original_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_original_author
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_original_author_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_original_new_author
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_original_new_author_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translation
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translation_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translation_translator
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translation_translator_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translation_new_translator
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translation_new_translator_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translator
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_translator_new
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_latein_user
SET SCHEMA public;