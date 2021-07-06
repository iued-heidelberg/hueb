\set ON_ERROR_STOP true
SET search_path to public;

DROP TABLE IF EXISTS sueb_author CASCADE;
DROP TABLE IF EXISTS sueb_collection CASCADE;
DROP TABLE IF EXISTS sueb_country CASCADE;
DROP TABLE IF EXISTS sueb_ddc_german CASCADE;
DROP TABLE IF EXISTS sueb_language CASCADE;
DROP TABLE IF EXISTS sueb_loc_assign CASCADE;
DROP TABLE IF EXISTS sueb_location CASCADE;
DROP TABLE IF EXISTS sueb_manual_keys CASCADE;
DROP TABLE IF EXISTS sueb_orig_assign CASCADE;
DROP TABLE IF EXISTS sueb_original CASCADE;
DROP TABLE IF EXISTS sueb_pnd_alias CASCADE;
DROP TABLE IF EXISTS sueb_pnd_main CASCADE;
DROP TABLE IF EXISTS sueb_pnd_title CASCADE;
DROP TABLE IF EXISTS sueb_swd_main CASCADE;
DROP TABLE IF EXISTS sueb_swd_term CASCADE;
DROP TABLE IF EXISTS sueb_translation CASCADE;
DROP TABLE IF EXISTS sueb_translator CASCADE;

SET search_path to di_sueb;
ALTER TABLE IF EXISTS sueb_author
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_collection
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_country
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_ddc_german
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_language
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_loc_assign
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_location
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_manual_keys
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_orig_assign
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_original
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_pnd_alias
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_pnd_main
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_pnd_title
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_swd_main
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_swd_term
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_translation
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_translator
SET SCHEMA public;
