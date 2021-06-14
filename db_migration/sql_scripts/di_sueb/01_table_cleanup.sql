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

-- renaming primary_keys
SELECT rename_column_if_exists('author', 'auth_id', 'id');
SELECT rename_column_if_exists('collection', 'col_id', 'id');
SELECT rename_column_if_exists('country', 'c_id', 'id');
SELECT rename_column_if_exists('ddc_german', 'ddc_id', 'id');
SELECT rename_column_if_exists('language', 'lang_id', 'id');
SELECT rename_column_if_exists('loc_assign', 'loc_assign_id', 'id');
SELECT rename_column_if_exists('location', 'loc_id', 'id');
SELECT rename_column_if_exists('manual_keys', 'mankey_id', 'id');
SELECT rename_column_if_exists('orig_assign', 'orig_assign_id', 'id');
SELECT rename_column_if_exists('original', 'orig_id', 'id');

SELECT rename_column_if_exists('pnd_alias', 'pnd_alias_id', 'id');
SELECT rename_column_if_exists('pnd_main', 'pnd_id', 'id');

SELECT rename_column_if_exists('pnd_title', 'pnd_title_id', 'id');

SELECT rename_column_if_exists('swd_main', 'swd_id', 'id');
SELECT rename_column_if_exists('swd_term', 'swd_term_id', 'id');

SELECT rename_column_if_exists('translation', 'trans_id', 'id');
SELECT rename_column_if_exists('translator', 'translator_id', 'id');


-- adding sequences
SELECT(add_sequence('author'));
SELECT(add_sequence('collection'));
SELECT(add_sequence('country'));
SELECT(add_sequence('ddc_german'));
SELECT(add_sequence('language'));
SELECT(add_sequence('loc_assign'));
SELECT(add_sequence('location'));
SELECT(add_sequence('manual_keys'));
SELECT(add_sequence('orig_assign'));
SELECT(add_sequence('original'));
SELECT(add_sequence('pnd_alias'));
SELECT(add_sequence('pnd_main'));
SELECT(add_sequence('swd_term'));
SELECT(add_sequence('translation'));
SELECT(add_sequence('translator'));


ALTER TABLE country ADD PRIMARY KEY (id);

SELECT rename_column_if_exists('loc_assign', 'loc_id', 'location_id');
SELECT rename_column_if_exists('loc_assign', 'orig_id', 'original_id');
SELECT rename_column_if_exists('loc_assign', 'trans_id', 'translation_id');


SELECT rename_column_if_exists('location', 'country', 'country_id');


SELECT rename_column_if_exists('manual_keys', 'orig_id', 'original_id');
SELECT rename_column_if_exists('manual_keys', 'trans_id', 'translation_id');


ALTER TABLE manual_keys
DROP COLUMN IF EXISTS off_id;


ALTER TABLE orig_assign
DROP COLUMN IF EXISTS orig_diff_id,
DROP COLUMN IF EXISTS trans_diff_id;

SELECT rename_column_if_exists('orig_assign', 'orig_id', 'original_id');
SELECT rename_column_if_exists('orig_assign', 'trans_id', 'translation_id');


-- dropping empty columns from original
ALTER TABLE original
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys; --empty

-- renaming original columns
SELECT rename_column_if_exists('original', 'auth_id', 'author_id');
SELECT rename_column_if_exists('original', 'col_id', 'collection_id');
SELECT rename_column_if_exists('original', 'language', 'language_id');


ALTER TABLE translation
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys; --empty

-- renaming original columns
SELECT rename_column_if_exists('original', 'col_id', 'collection_id');
SELECT rename_column_if_exists('original', 'language', 'language_id');
SELECT rename_column_if_exists('original', 'via_language', 'via_language_id');

-- renaming translation columns
SELECT rename_column_if_exists('translation', 'auth_id', 'author_id');
SELECT rename_column_if_exists('translation', 'col_id', 'collection_id');
SELECT rename_column_if_exists('translation', 'language', 'language_id');
SELECT rename_column_if_exists('translation', 'via_language', 'via_language_id');

