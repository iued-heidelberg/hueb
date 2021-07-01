\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;

-- dropping superfluous sequences
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

