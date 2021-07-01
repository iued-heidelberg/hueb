\set ON_ERROR_STOP true
SET search_path to di_sueb_lidos;

-- These calls adds a migration_note attribute to each table.
-- This attribute can be used to explain necessary changes to table entries to allow the foreign key constraint creation.

ALTER TABLE sueb_lidos_author
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_ddc_german
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_filter
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_language
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_lidos_ex
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_manual_keys
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_orig_assign
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_original
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_translation
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE sueb_lidos_translator
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;
