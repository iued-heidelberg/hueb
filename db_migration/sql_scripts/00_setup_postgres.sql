\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;

CREATE OR REPLACE FUNCTION column_exists(ptable TEXT, pcolumn TEXT)
  RETURNS BOOLEAN AS $BODY$
DECLARE result bool;
DECLARE sp TEXT;
BEGIN
    -- GET search_path
    SHOW search_path INTO sp;

    -- Does the requested column exist?
    SELECT COUNT(*) INTO result
    FROM information_schema.columns
    WHERE
      table_schema = sp and
      table_name = ptable and
      column_name = pcolumn;
    RETURN result;
END$BODY$
  LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION rename_column_if_exists(ptable TEXT, pcolumn TEXT, new_name TEXT)
  RETURNS VOID AS $BODY$
BEGIN
    -- Rename the column if it exists.
    IF column_exists(ptable, pcolumn) THEN
        EXECUTE FORMAT('ALTER TABLE %I RENAME COLUMN %I TO %I;',
            ptable, pcolumn, new_name);
    END IF;
END$BODY$
  LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION dangling_references_exists(primary_table TEXT, primary_column TEXT, secondary_table TEXT)
  RETURNS BOOLEAN AS $BODY$
DECLARE result bool;

BEGIN
    EXECUTE FORMAT('
      SELECT EXISTS(
        SELECT %I
        FROM %I
        WHERE %I NOT IN (
          SELECT id
          FROM %I
        )
      );',
    primary_column, primary_table, primary_column, secondary_table)
    INTO result;
    RETURN result;
  END$BODY$
  LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION clean_up_relation(primary_table TEXT, primary_column TEXT, secondary_table TEXT)
  RETURNS void AS $BODY$
DECLARE placeholder BIGINT;
BEGIN

  -- drop primary key
    EXECUTE FORMAT('
      ALTER TABLE %s
      DROP CONSTRAINT IF EXISTS %I;',
      primary_table, secondary_table||'_fk');


  -- check if a placeholder is necessary
    IF dangling_references_exists(primary_table, primary_column, secondary_table)
    THEN
      -- insert placeholder
        EXECUTE FORMAT('
          INSERT INTO %I(migration_notes, migration_generated)
          VALUES ($$Automatisch als Platzhalter angelegt$$, true)
          RETURNING id;',
          secondary_table)
        INTO placeholder;

        -- move dangling references to placeholder
        EXECUTE FORMAT('
        UPDATE %I
        SET %s = %s
        WHERE id IN(
          SELECT %s
          FROM %s
          WHERE %s NOT IN (
            SELECT id
            FROM %s
          )
        )
        RETURNING *;',
        primary_table, primary_column, placeholder, primary_table||'.id', primary_table, primary_table || '.' || primary_column, secondary_table);


    END IF;

  -- create primary key
    EXECUTE FORMAT('
       alter table %s
        add constraint %I
          foreign key (%s) references "%s"
            on update cascade on delete restrict;',
            primary_table, secondary_table||'_fk', primary_column, secondary_table);


    RETURN;
  END$BODY$
  LANGUAGE plpgsql VOLATILE;

  CREATE OR REPLACE FUNCTION add_sequence(ptable TEXT)
  RETURNS VOID AS $BODY$
BEGIN

  EXECUTE FORMAT('
    DROP SEQUENCE IF EXISTS %I_id_seq CASCADE;
    CREATE SEQUENCE %I_id_seq;
    ALTER TABLE %s ALTER COLUMN id SET DEFAULT nextval($$%I_id_seq$$);

    ALTER TABLE %s ALTER COLUMN id SET NOT NULL;


    SELECT setval($$%I_id_seq$$,
      (SELECT MAX(id)
        FROM %I)
    );', ptable, ptable, ptable, ptable, ptable, ptable, ptable, ptable, ptable);

END$BODY$
  LANGUAGE plpgsql VOLATILE;
