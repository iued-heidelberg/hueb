CREATE OR REPLACE FUNCTION column_exists(ptable TEXT, pcolumn TEXT)
  RETURNS BOOLEAN AS $BODY$
DECLARE result bool;
BEGIN
    -- Does the requested column exist?
    SELECT COUNT(*) INTO result
    FROM information_schema.columns
    WHERE
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