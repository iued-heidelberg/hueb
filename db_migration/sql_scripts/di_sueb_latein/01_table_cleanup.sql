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

-- renaming primary_keys
SELECT rename_column_if_exists('author', 'auth_id', 'id');
SELECT rename_column_if_exists('author_new', 'auth_id', 'id');
SELECT rename_column_if_exists('country', 'c_id', 'id');
SELECT rename_column_if_exists('ddc_german', 'ddc_id', 'id');
SELECT rename_column_if_exists('language', 'lang_id', 'id');
SELECT rename_column_if_exists('loc_assign', 'loc_assign_id', 'id');
SELECT rename_column_if_exists('location', 'loc_id', 'id');
SELECT rename_column_if_exists('location_new', 'loc_id', 'id');
SELECT rename_column_if_exists('orig_assign', 'orig_assign_id', 'id');
SELECT rename_column_if_exists('original', 'orig_id', 'id');
SELECT rename_column_if_exists('original_new', 'orig_id', 'id');
SELECT rename_column_if_exists('translation', 'trans_id', 'id');
SELECT rename_column_if_exists('translation_new', 'trans_id', 'id');
SELECT rename_column_if_exists('translator', 'translator_id', 'id');
SELECT rename_column_if_exists('translator_new', 'translator_id', 'id');
SELECT rename_column_if_exists('user', 'user_id', 'id');

-- adding sequences
SELECT(add_sequence('author'));
SELECT(add_sequence('author_new'));
SELECT(add_sequence('country'));
SELECT(add_sequence('ddc_german'));
SELECT(add_sequence('language'));
SELECT(add_sequence('loc_assign'));
SELECT(add_sequence('location'));
SELECT(add_sequence('location_new'));
SELECT(add_sequence('orig_assign'));
SELECT(add_sequence('original'));
SELECT(add_sequence('original_new'));
SELECT(add_sequence('translation'));
SELECT(add_sequence('translation_new'));
SELECT(add_sequence('translator'));
SELECT(add_sequence('translator_new'));
  -- user has a sequence already



-- dropping empty columns from original
ALTER TABLE original
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming original columns
SELECT rename_column_if_exists('original', 'land', 'country_id');
SELECT rename_column_if_exists('original', 'language', 'language_id');
SELECT rename_column_if_exists('original', 'auth_id', 'author0_id');
SELECT rename_column_if_exists('original', 'auth_id1', 'author1_id');
SELECT rename_column_if_exists('original', 'auth_id2', 'author2_id');
SELECT rename_column_if_exists('original', 'auth_id3', 'author3_id');

-- renaming author columns
SELECT rename_column_if_exists('author', 'auth_id', 'author_id');

-- renaming author_new columns
SELECT rename_column_if_exists('author_new', 'auth_id', 'author_id');

-- renaming language columns
SELECT rename_column_if_exists('language', 'lang_id', 'language_id');

-- cleaning up country table
--country_fk

alter table original drop constraint if exists country_fk;
alter table original_new drop constraint if exists country_fk;
alter table translation drop constraint if exists country_fk;
alter table translation_new drop constraint if exists country_fk;


ALTER TABLE country
DROP CONSTRAINT IF EXISTS country_pkey;

ALTER TABLE country
ADD PRIMARY KEY (id);


-- dropping empty columns from original_new
ALTER TABLE original_new
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming original columns
SELECT rename_column_if_exists('original_new', 'land', 'country_id');
SELECT rename_column_if_exists('original_new', 'language', 'language_id');
SELECT rename_column_if_exists('original_new', 'auth_id', 'author0_id');
SELECT rename_column_if_exists('original_new', 'auth_id1', 'author1_id');
SELECT rename_column_if_exists('original_new', 'auth_id2', 'author2_id');
SELECT rename_column_if_exists('original_new', 'auth_id3', 'author3_id');

-- dropping empty columns from translation
ALTER TABLE translation
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming translation columns
SELECT rename_column_if_exists('translation', 'land', 'country_id');
SELECT rename_column_if_exists('translation', 'via_language', 'via_language_id');
SELECT rename_column_if_exists('translation', 'language', 'language_id');
SELECT rename_column_if_exists('translation', 'translator_id1', 'translator1_id');
SELECT rename_column_if_exists('translation', 'translator_id',  'translator0_id');
SELECT rename_column_if_exists('translation', 'translator_id2', 'translator2_id');
SELECT rename_column_if_exists('translation', 'translator_id3', 'translator3_id');
SELECT rename_column_if_exists('translation', 'auth_id', 'author_id');

-- dropping empty columns from translation
ALTER TABLE translation_new
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming translation columns
SELECT rename_column_if_exists('translation_new', 'land', 'country_id');
SELECT rename_column_if_exists('translation_new', 'via_language', 'via_language_id');
SELECT rename_column_if_exists('translation_new', 'language', 'language_id');
SELECT rename_column_if_exists('translation_new', 'translator_id1', 'translator1_id');
SELECT rename_column_if_exists('translation_new', 'translator_id',  'translator0_id');
SELECT rename_column_if_exists('translation_new', 'translator_id2', 'translator2_id');
SELECT rename_column_if_exists('translation_new', 'translator_id3', 'translator3_id');
SELECT rename_column_if_exists('translation_new', 'auth_id', 'author_id');

-- changing user_id type of translator
alter table translator
alter column user_id drop default;

alter table translator
alter column user_id type bigint using user_id::bigint;

-- changing user_id type of translator_new
alter table translator_new
alter column user_id drop default;

alter table translator_new
alter column user_id type bigint using user_id::bigint;