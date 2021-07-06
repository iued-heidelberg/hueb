\set ON_ERROR_STOP true


-- dropping superfluous sequences
SET search_path to public;
DROP TABLE IF EXISTS sueb_lidos_author CASCADE;
DROP TABLE IF EXISTS sueb_lidos_ddc_german CASCADE;
DROP TABLE IF EXISTS sueb_lidos_filter CASCADE;
DROP TABLE IF EXISTS sueb_lidos_language CASCADE;
DROP TABLE IF EXISTS sueb_lidos_lidos_ex CASCADE;
DROP TABLE IF EXISTS sueb_lidos_manual_keys CASCADE;
DROP TABLE IF EXISTS sueb_lidos_orig_assign CASCADE;
DROP TABLE IF EXISTS sueb_lidos_original CASCADE;
DROP TABLE IF EXISTS sueb_lidos_translation CASCADE;
DROP TABLE IF EXISTS sueb_lidos_translator CASCADE;


SET search_path to di_sueb_lidos ;
ALTER TABLE IF EXISTS sueb_lidos_author
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_ddc_german
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_filter
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_language
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_lidos_ex
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_manual_keys
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_orig_assign
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_original
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_translation
SET SCHEMA public;

ALTER TABLE IF EXISTS sueb_lidos_translator
SET SCHEMA public;
