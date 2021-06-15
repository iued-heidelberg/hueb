\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;

-- These calls adds a migration_note attribute to each table.
-- This attribute can be used to explain necessary changes to TABLE sueb_latein_entries to allow the foreign key constraint creation.

ALTER TABLE sueb_latein_author
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_author_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_country
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_ddc_german
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_language
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_loc_assign
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_location
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_location_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_orig_assign
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_original
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_original_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_translation
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_translation_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_translator
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_latein_translator_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;
