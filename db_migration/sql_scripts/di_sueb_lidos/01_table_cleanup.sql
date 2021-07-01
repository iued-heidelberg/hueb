\set ON_ERROR_STOP true
SET search_path to di_sueb_lidos;

-- dropping keyword-tables because they are empty
drop table if exists additional_keys;
drop table if exists collection;
drop table if exists country;
drop table if exists loc_assign;
drop table if exists location;
drop table if exists official_keys;
drop table if exists pnd_alias;
drop table if exists pnd_main;
drop table if exists pnd_title;
drop table if exists pseudo;
drop table if exists sim_term;
drop table if exists swd_main;
drop table if exists swd_term;

drop table if exists lidos_ex_alt;
drop table if exists manual_keys_alt;
drop table if exists orig_assign_alt;


drop table if exists translation;
drop table if exists translation_alt;
ALTER TABLE translation_iso RENAME to sueb_lidos_translation;

drop table if exists translator;
drop table if exists translator_alt;
ALTER TABLE translator_iso RENAME to sueb_lidos_translator;

drop table if exists original;
drop table if exists original_alt;
ALTER TABLE original_iso RENAME to sueb_lidos_original;

drop table if exists author;
drop table if exists author_alt;
ALTER TABLE author_iso RENAME to sueb_lidos_author;

ALTER TABLE ddc_deutsch RENAME to sueb_lidos_ddc_german;
ALTER TABLE filter RENAME to sueb_lidos_filter;
ALTER TABLE language RENAME TO sueb_lidos_language;
ALTER TABLE lidos_ex RENAME TO sueb_lidos_lidos_ex;
ALTER TABLE manual_keys RENAME TO sueb_lidos_manual_keys;
ALTER TABLE orig_assign RENAME TO sueb_lidos_orig_assign;


SELECT rename_column_if_exists('sueb_lidos_author', 'auth_id', 'id');
SELECT rename_column_if_exists('sueb_lidos_ddc_german', 'ddc_id', 'id');
SELECT rename_column_if_exists('sueb_lidos_language', 'lang_id', 'id');
SELECT rename_column_if_exists('sueb_lidos_manual_keys', 'mankey_id', 'id');
SELECT rename_column_if_exists('sueb_lidos_orig_assign', 'orig_assign_id', 'id');
SELECT rename_column_if_exists('sueb_lidos_original', 'orig_id', 'id');
SELECT rename_column_if_exists('sueb_lidos_translation', 'trans_id', 'id');
SELECT rename_column_if_exists('sueb_lidos_translator', 'translator_id', 'id');



-- adding sequences
SELECT(add_sequence('sueb_lidos_author'));
SELECT(add_sequence('sueb_lidos_ddc_german'));
SELECT(add_sequence('sueb_lidos_filter'));
SELECT(add_sequence('sueb_lidos_language'));
SELECT(add_sequence('sueb_lidos_lidos_ex'));
SELECT(add_sequence('sueb_lidos_manual_keys'));
SELECT(add_sequence('sueb_lidos_orig_assign'));
SELECT(add_sequence('sueb_lidos_original'));
SELECT(add_sequence('sueb_lidos_translation'));
SELECT(add_sequence('sueb_lidos_translator'));


ALTER TABLE sueb_lidos_manual_keys
DROP COLUMN IF EXISTS off_id;

SELECT rename_column_if_exists('sueb_lidos_manual_keys', 'orig_id', 'original_id');
SELECT rename_column_if_exists('sueb_lidos_manual_keys', 'trans_id', 'translation_id');



ALTER TABLE sueb_lidos_orig_assign
DROP COLUMN IF EXISTS orig_diff_id,
DROP COLUMN IF EXISTS trans_diff_id;

SELECT rename_column_if_exists('sueb_lidos_orig_assign', 'orig_id', 'original_id');
SELECT rename_column_if_exists('sueb_lidos_orig_assign', 'trans_id', 'translation_id');

ALTER TABLE sueb_lidos_original
DROP COLUMN IF EXISTS col_id,
DROP COLUMN IF EXISTS additional_keys;

SELECT rename_column_if_exists('sueb_lidos_original', 'auth_id', 'author_id');
SELECT rename_column_if_exists('sueb_lidos_original', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_lidos_original', 'manual_keys', 'manual_keys_id');


ALTER TABLE sueb_lidos_translation
DROP COLUMN IF EXISTS col_id,
DROP COLUMN IF EXISTS additional_keys;

SELECT rename_column_if_exists('sueb_lidos_translation', 'auth_id', 'author_id');
SELECT rename_column_if_exists('sueb_lidos_translation', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_lidos_translation', 'manual_keys', 'manual_keys_id');

SELECT rename_column_if_exists('sueb_lidos_translation', 'via_language', 'via_language_id');
