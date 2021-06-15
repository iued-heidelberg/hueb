\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;

-- dropping keyword-tables because they are empty
drop table if exists manual_keys;
drop table if exists official_keys;
drop table if exists additional_keys;
drop table if exists sim_term;
drop table if exists swd_main;
drop table if exists swd_term;

-- dropping person-name-database-tables because they are empty
drop table if exists pnd_alias;
drop table if exists pnd_main;
drop table if exists pnd_title;

-- dropping old information
drop table if exists old_table;

-- dropping project specifica
drop table if exists projektbeschreibung;

-- dropping pseudonym table which is empty
drop table if exists pseudo;

-- dropping empty collection table
drop table if exists collection;

-- renaming ddc_deutsch to ddc_german
ALTER TABLE IF EXISTS ddc_deutsch
RENAME TO ddc_german;


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

-- renaming primary_keys
SELECT rename_column_if_exists('sueb_latein_author', 'auth_id', 'id');
SELECT rename_column_if_exists('sueb_latein_author_new', 'auth_id', 'id');
SELECT rename_column_if_exists('sueb_latein_country', 'c_id', 'id');
SELECT rename_column_if_exists('sueb_latein_ddc_german', 'ddc_id', 'id');
SELECT rename_column_if_exists('sueb_latein_language', 'lang_id', 'id');
SELECT rename_column_if_exists('sueb_latein_loc_assign', 'loc_assign_id', 'id');
SELECT rename_column_if_exists('sueb_latein_location', 'loc_id', 'id');
SELECT rename_column_if_exists('sueb_latein_location_new', 'loc_id', 'id');
SELECT rename_column_if_exists('sueb_latein_orig_assign', 'orig_assign_id', 'id');
SELECT rename_column_if_exists('sueb_latein_original', 'orig_id', 'id');
SELECT rename_column_if_exists('sueb_latein_original_new', 'orig_id', 'id');
SELECT rename_column_if_exists('sueb_latein_translation', 'trans_id', 'id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'trans_id', 'id');
SELECT rename_column_if_exists('sueb_latein_translator', 'translator_id', 'id');
SELECT rename_column_if_exists('sueb_latein_translator_new', 'translator_id', 'id');
SELECT rename_column_if_exists('sueb_latein_user', 'user_id', 'id');

-- adding sequences
SELECT(add_sequence('sueb_latein_author'));
SELECT(add_sequence('sueb_latein_author_new'));
SELECT(add_sequence('sueb_latein_country'));
SELECT(add_sequence('sueb_latein_ddc_german'));
SELECT(add_sequence('sueb_latein_language'));
SELECT(add_sequence('sueb_latein_loc_assign'));
SELECT(add_sequence('sueb_latein_location'));
SELECT(add_sequence('sueb_latein_location_new'));
SELECT(add_sequence('sueb_latein_orig_assign'));
SELECT(add_sequence('sueb_latein_original'));
SELECT(add_sequence('sueb_latein_original_new'));
SELECT(add_sequence('sueb_latein_translation'));
SELECT(add_sequence('sueb_latein_translation_new'));
SELECT(add_sequence('sueb_latein_translator'));
SELECT(add_sequence('sueb_latein_translator_new'));

ALTER SEQUENCE user_user_id_seq RENAME TO sueb_latein_user_user_id_seq;




-- dropping empty columns from original
ALTER TABLE sueb_latein_original
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming original columns
SELECT rename_column_if_exists('sueb_latein_original', 'land', 'country_id');
SELECT rename_column_if_exists('sueb_latein_original', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_latein_original', 'auth_id', 'author0_id');
SELECT rename_column_if_exists('sueb_latein_original', 'auth_id1', 'author1_id');
SELECT rename_column_if_exists('sueb_latein_original', 'auth_id2', 'author2_id');
SELECT rename_column_if_exists('sueb_latein_original', 'auth_id3', 'author3_id');

-- renaming author columns
SELECT rename_column_if_exists('sueb_latein_author', 'auth_id', 'author_id');

-- renaming author_new columns
SELECT rename_column_if_exists('sueb_latein_author_new', 'auth_id', 'author_id');

-- renaming language columns
SELECT rename_column_if_exists('sueb_latein_language', 'lang_id', 'language_id');

-- cleaning up country table
--country_fk

alter table sueb_latein_original drop constraint if exists country_fk;
alter table sueb_latein_original_new drop constraint if exists country_fk;
alter table sueb_latein_translation drop constraint if exists country_fk;
alter table sueb_latein_translation_new drop constraint if exists country_fk;


ALTER TABLE sueb_latein_country
DROP CONSTRAINT IF EXISTS country_pkey;

ALTER TABLE sueb_latein_country
ADD PRIMARY KEY (id);


-- dropping empty columns from original_new
ALTER TABLE sueb_latein_original_new
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming original columns
SELECT rename_column_if_exists('sueb_latein_original_new', 'land', 'country_id');
SELECT rename_column_if_exists('sueb_latein_original_new', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_latein_original_new', 'auth_id', 'author0_id');
SELECT rename_column_if_exists('sueb_latein_original_new', 'auth_id1', 'author1_id');
SELECT rename_column_if_exists('sueb_latein_original_new', 'auth_id2', 'author2_id');
SELECT rename_column_if_exists('sueb_latein_original_new', 'auth_id3', 'author3_id');

-- dropping empty columns from translation
ALTER TABLE sueb_latein_translation
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming translation columns
SELECT rename_column_if_exists('sueb_latein_translation', 'land', 'country_id');
SELECT rename_column_if_exists('sueb_latein_translation', 'via_language', 'via_language_id');
SELECT rename_column_if_exists('sueb_latein_translation', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_latein_translation', 'translator_id1', 'translator1_id');
SELECT rename_column_if_exists('sueb_latein_translation', 'translator_id',  'translator0_id');
SELECT rename_column_if_exists('sueb_latein_translation', 'translator_id2', 'translator2_id');
SELECT rename_column_if_exists('sueb_latein_translation', 'translator_id3', 'translator3_id');
SELECT rename_column_if_exists('sueb_latein_translation', 'auth_id', 'author_id');

-- dropping empty columns from translation
ALTER TABLE sueb_latein_translation_new
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming translation columns
SELECT rename_column_if_exists('sueb_latein_translation_new', 'land', 'country_id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'via_language', 'via_language_id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'translator_id1', 'translator1_id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'translator_id',  'translator0_id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'translator_id2', 'translator2_id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'translator_id3', 'translator3_id');
SELECT rename_column_if_exists('sueb_latein_translation_new', 'auth_id', 'author_id');

-- changing user_id type of translator
alter table sueb_latein_translator
alter column user_id drop default;

alter table sueb_latein_translator
alter column user_id type bigint using user_id::bigint;

-- changing user_id type of translator_new
alter table sueb_latein_translator_new
alter column user_id drop default;

alter table sueb_latein_translator_new
alter column user_id type bigint using user_id::bigint;