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

CREATE OR REPLACE FUNCTION clean_up_relation(primary_table TEXT, primary_column TEXT, secondary_table TEXT, prefix TEXT default '', suffix TEXT default '')
  RETURNS void AS $BODY$
DECLARE placeholder BIGINT;
BEGIN

  -- drop primary key
    EXECUTE FORMAT('
      ALTER TABLE %s
      DROP CONSTRAINT IF EXISTS %I;',
      primary_table, prefix || secondary_table|| suffix ||'_fk');


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
            primary_table, prefix || secondary_table|| suffix ||'_fk', primary_column, secondary_table);


    RETURN;
  END$BODY$
  LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION add_sequence(ptable TEXT)
  RETURNS VOID AS $BODY$
DECLARE
  schemaname varchar := '';
  seq_name varchar  := '';
BEGIN
  seq_name := CONCAT (schemaname, ptable, '_id_seq');

  EXECUTE FORMAT('

    DROP SEQUENCE IF EXISTS %I CASCADE;
    CREATE SEQUENCE %I;
    ALTER TABLE %s ALTER COLUMN id SET DEFAULT nextval($$%I$$);

    ALTER TABLE %s ALTER COLUMN id SET NOT NULL;


    SELECT setval($$%I$$,
      (SELECT MAX(id)
        FROM %I)
    );', seq_name, seq_name, ptable, seq_name, ptable, seq_name, ptable);

END$BODY$
  LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION split_new_into_separate(ptable TEXT, scolumn TEXT)
   RETURNS VOID AS $BODY$
DECLARE
   counter INTEGER := 0 ;
BEGIN
   LOOP
 	EXECUTE FORMAT('
		ALTER TABLE %s DROP COLUMN IF EXISTS %I%s_new_id;
	   	ALTER TABLE %s ADD COLUMN %I%s_new_id bigint;

	   UPDATE %s
		SET %I%s_new_id = %I%s_id;
	', ptable, scolumn, counter, ptable, scolumn, counter, ptable, scolumn, counter, scolumn, counter);

	counter := counter + 1 ;
	EXIT WHEN counter > 3 ;

   END LOOP ;

   RETURN;
END ;
$BODY$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_m_n_relation(first_table TEXT, first_column TEXT, second_table Text, second_column TEXT, suffix TEXT)
RETURNS VOID AS $BODY$
DECLARE
 counter INTEGER := 0 ;
BEGIN

  EXECUTE FORMAT('
	DROP TABLE IF EXISTS %I_%I%s;

    CREATE TABLE %I_%I%s(
	  id    SERIAL PRIMARY KEY,
	  %I_id BIGINT NOT NULL,
	  %I_id BIGINT NOT NULL,
	  FOREIGN KEY (%I_id) REFERENCES %s (id),
	  FOREIGN KEY (%I_id) REFERENCES %s%s (id)
    );', first_table, second_table, suffix ,first_table, second_table, suffix, first_table, second_table, first_table, first_table, second_table, second_table, suffix);

 	LOOP
		EXECUTE FORMAT('
		INSERT INTO %I_%I%s (%I_id, %I_id)
		SELECT
		  id,
		  %I%s%s_id
		FROM
		  %s
		WHERE
		  %I%s%s_id != 0;
		', first_table, second_table, suffix, first_table, second_table, second_column, counter ,suffix, first_table, second_column, counter,suffix);

		counter := counter + 1 ;
		EXIT WHEN counter > 3 ;

   END LOOP ;

END$BODY$
  LANGUAGE plpgsql VOLATILE;


CREATE OR REPLACE FUNCTION delete_superfluos_columns(first_table TEXT, second_table Text, suffix TEXT)
RETURNS VOID AS $BODY$
DECLARE
 counter INTEGER := 0 ;
BEGIN

 	LOOP
		EXECUTE FORMAT('
		ALTER TABLE %I
		DROP COLUMN IF EXISTS %I%s%s_id;
		', first_table, second_table, counter, suffix);

		counter := counter + 1 ;
		EXIT WHEN counter > 3 ;

   END LOOP ;

END$BODY$
  LANGUAGE plpgsql VOLATILE;