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

-- dropping empty columns from original
ALTER TABLE original
DROP COLUMN IF EXISTS manual_keys,
DROP COLUMN IF EXISTS additional_keys,
DROP COLUMN IF EXISTS col_id;

-- renaming columns from original
SELECT rename_column_if_exists('original', 'land', 'country_id');
SELECT rename_column_if_exists('original', 'language', 'language_id');