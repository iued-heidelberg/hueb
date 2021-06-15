\set ON_ERROR_STOP true
SET search_path to di_sueb;

-- dropping keyword-tables because they are empty
drop table if exists additional_keys;
drop table if exists official_keys;
drop table if exists old_table;

drop table if exists sim_term;

-- dropping project specifica
drop table if exists projektbeschreibung;

-- dropping pseudonym table which is empty
drop table if exists pseudo;

-- renaming ddc_deutsch to ddc_german
ALTER TABLE IF EXISTS ddc_deutsch
RENAME TO ddc_german;


-- dropping original_new
-- this query shows that most data is contained in original
/*\
  SELECT
    a.orig_id as original_new_missing,
    b.orig_id as original_missing
  FROM di_sueb.original a
  FULL OUTER JOIN di_sueb.original_new b
    ON a.orig_id = b.orig_id
  WHERE a.orig_id IS NULL OR b.orig_id IS NULL
*/
drop table if exists original_new;

-- dropping translation_new
-- this query shows that most data is contained in translation
/*
  SELECT
    a.trans_id as translation_new_missing,
    b.trans_id as translation_missing
  FROM di_sueb.translation a
  FULL OUTER JOIN di_sueb.translation_new b
    ON a.trans_id = b.trans_id
  WHERE a.trans_id IS NULL OR b.trans_id IS NULL
*/
drop table if exists translation_new;

ALTER TABLE IF EXISTS author
RENAME TO sueb_author;

ALTER TABLE IF EXISTS "collection"
RENAME TO sueb_collection;

ALTER TABLE IF EXISTS country
RENAME TO sueb_country;

ALTER TABLE IF EXISTS ddc_german
RENAME TO sueb_ddc_german;

ALTER TABLE IF EXISTS "language"
RENAME TO sueb_language;

ALTER TABLE IF EXISTS loc_assign
RENAME TO sueb_loc_assign;

ALTER TABLE IF EXISTS "location"
RENAME TO sueb_location;

ALTER TABLE IF EXISTS manual_keys
RENAME TO sueb_manual_keys;

ALTER TABLE IF EXISTS orig_assign
RENAME TO sueb_orig_assign;

ALTER TABLE IF EXISTS original
RENAME TO sueb_original;

ALTER TABLE IF EXISTS pnd_alias
RENAME TO sueb_pnd_alias;

ALTER TABLE IF EXISTS pnd_main
RENAME TO sueb_pnd_main;

ALTER TABLE IF EXISTS pnd_title
RENAME TO sueb_pnd_title;

ALTER TABLE IF EXISTS swd_main
RENAME TO sueb_swd_main;

ALTER TABLE IF EXISTS swd_term
RENAME TO sueb_swd_term;

ALTER TABLE IF EXISTS translation
RENAME TO sueb_translation;

ALTER TABLE IF EXISTS translator
RENAME TO sueb_translator;


-- renaming primary_keys
SELECT rename_column_if_exists('sueb_author', 'auth_id', 'id');
SELECT rename_column_if_exists('sueb_collection', 'col_id', 'id');
SELECT rename_column_if_exists('sueb_country', 'c_id', 'id');
SELECT rename_column_if_exists('sueb_ddc_german', 'ddc_id', 'id');
SELECT rename_column_if_exists('sueb_language', 'lang_id', 'id');
SELECT rename_column_if_exists('sueb_loc_assign', 'loc_assign_id', 'id');
SELECT rename_column_if_exists('sueb_location', 'loc_id', 'id');
SELECT rename_column_if_exists('sueb_manual_keys', 'mankey_id', 'id');
SELECT rename_column_if_exists('sueb_orig_assign', 'orig_assign_id', 'id');
SELECT rename_column_if_exists('sueb_original', 'orig_id', 'id');

SELECT rename_column_if_exists('sueb_pnd_alias', 'pnd_alias_id', 'id');
SELECT rename_column_if_exists('sueb_pnd_main', 'pnd_id', 'id');

SELECT rename_column_if_exists('sueb_pnd_title', 'pnd_title_id', 'id');

SELECT rename_column_if_exists('sueb_swd_main', 'swd_id', 'id');
SELECT rename_column_if_exists('sueb_swd_term', 'swd_term_id', 'id');

SELECT rename_column_if_exists('sueb_translation', 'trans_id', 'id');
SELECT rename_column_if_exists('sueb_translator', 'translator_id', 'id');




-- adding sequences
SELECT(add_sequence('sueb_author'));
SELECT(add_sequence('sueb_collection'));
SELECT(add_sequence('sueb_country'));
SELECT(add_sequence('sueb_ddc_german'));
SELECT(add_sequence('sueb_language'));
SELECT(add_sequence('sueb_loc_assign'));
SELECT(add_sequence('sueb_location'));
SELECT(add_sequence('sueb_manual_keys'));
SELECT(add_sequence('sueb_orig_assign'));
SELECT(add_sequence('sueb_original'));
SELECT(add_sequence('sueb_pnd_alias'));
SELECT(add_sequence('sueb_pnd_main'));
SELECT(add_sequence('sueb_pnd_title'));
SELECT(add_sequence('sueb_swd_main'));
SELECT(add_sequence('sueb_swd_term'));
SELECT(add_sequence('sueb_translation'));
SELECT(add_sequence('sueb_translator'));


ALTER TABLE sueb_country ADD PRIMARY KEY (id);

SELECT rename_column_if_exists('sueb_loc_assign', 'loc_id', 'location_id');
SELECT rename_column_if_exists('sueb_loc_assign', 'orig_id', 'original_id');
SELECT rename_column_if_exists('sueb_loc_assign', 'trans_id', 'translation_id');


SELECT rename_column_if_exists('sueb_location', 'country', 'country_id');


SELECT rename_column_if_exists('sueb_manual_keys', 'orig_id', 'original_id');
SELECT rename_column_if_exists('sueb_manual_keys', 'trans_id', 'translation_id');


ALTER TABLE sueb_manual_keys
DROP COLUMN IF EXISTS off_id;


ALTER TABLE sueb_orig_assign
DROP COLUMN IF EXISTS orig_diff_id,
DROP COLUMN IF EXISTS trans_diff_id;

SELECT rename_column_if_exists('sueb_orig_assign', 'orig_id', 'original_id');
SELECT rename_column_if_exists('sueb_orig_assign', 'trans_id', 'translation_id');


-- dropping empty columns from original
ALTER TABLE sueb_original
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys; --empty

-- renaming original columns
SELECT rename_column_if_exists('sueb_original', 'auth_id', 'author_id');
SELECT rename_column_if_exists('sueb_original', 'col_id', 'collection_id');
SELECT rename_column_if_exists('sueb_original', 'language', 'language_id');


ALTER TABLE sueb_translation
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys; --empty

-- renaming original columns
SELECT rename_column_if_exists('sueb_original', 'col_id', 'collection_id');
SELECT rename_column_if_exists('sueb_original', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_original', 'via_language', 'via_language_id');

-- renaming translation columns
SELECT rename_column_if_exists('sueb_translation', 'auth_id', 'author_id');
SELECT rename_column_if_exists('sueb_translation', 'col_id', 'collection_id');
SELECT rename_column_if_exists('sueb_translation', 'language', 'language_id');
SELECT rename_column_if_exists('sueb_translation', 'via_language', 'via_language_id');

