\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;


SELECT(split_new_into_separate('sueb_latein_original', 'author'));
SELECT(split_new_into_separate('sueb_latein_original_new', 'author'));

SELECT(add_m_n_relation('sueb_latein_original', 'original', 'sueb_latein_author', 'author',''));
ALTER TABLE sueb_latein_original_sueb_latein_author RENAME TO sueb_latein_original_author;

SELECT(add_m_n_relation('sueb_latein_original', 'original','sueb_latein_author', 'author', '_new'));
ALTER TABLE sueb_latein_original_sueb_latein_author_new RENAME TO sueb_latein_original_author_new;

SELECT(add_m_n_relation('sueb_latein_original_new', 'original_new', 'sueb_latein_author', 'author' ,'_new'));
ALTER TABLE sueb_latein_original_new_sueb_latein_author_new RENAME TO sueb_latein_original_new_author_new;


-- original_new_author

  DROP TABLE IF EXISTS sueb_latein_original_new_author;

  CREATE TABLE sueb_latein_original_new_author(
    id    SERIAL PRIMARY KEY,
    sueb_latein_original_id BIGINT NOT NULL,
    sueb_latein_author_id BIGINT NOT NULL,
    FOREIGN KEY (sueb_latein_original_id) REFERENCES sueb_latein_original_new (id),
    FOREIGN KEY (sueb_latein_author_id) REFERENCES sueb_latein_author (id)
  );

  INSERT INTO sueb_latein_author (migration_notes, migration_generated)
    VALUES ('Angelegt weil original einen FK auf author hatte aber keine Werte eingetragen waren', true)
    RETURNING id;

  UPDATE sueb_latein_original_new
  SET author0_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_original_new.id IN(
    SELECT id
    FROM sueb_latein_original_new
    WHERE author0_id NOT IN(
      SELECT id
      FROM sueb_latein_author
    )
  );

  INSERT INTO sueb_latein_original_new_author (sueb_latein_original_id, sueb_latein_author_id)
  SELECT
    id,
    author0_id
  FROM
    sueb_latein_original_new
  WHERE
    author0_id != 0;


  UPDATE sueb_latein_original_new
  SET author1_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_original_new.id IN(
    SELECT id
    FROM sueb_latein_original_new
    WHERE author1_id NOT IN(
      SELECT id
      FROM sueb_latein_author
    )
  );

  INSERT INTO sueb_latein_original_new_author (sueb_latein_original_id, sueb_latein_author_id)
  SELECT
    id,
    author1_id
  FROM
    sueb_latein_original_new
  WHERE
    author1_id != 0;


  UPDATE sueb_latein_original_new
  SET author2_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_original_new.id IN(
    SELECT id
    FROM sueb_latein_original_new
    WHERE author2_id NOT IN(
      SELECT id
      FROM sueb_latein_author
    )
  );

  INSERT INTO sueb_latein_original_new_author (sueb_latein_original_id, sueb_latein_author_id)
  SELECT
    id,
    author2_id
  FROM
    sueb_latein_original_new
  WHERE
    author2_id != 0;

  UPDATE sueb_latein_original_new
  SET author3_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_original_new.id IN(
    SELECT id
    FROM sueb_latein_original_new
    WHERE author3_id NOT IN(
      SELECT id
      FROM sueb_latein_author
    )
  );

  INSERT INTO sueb_latein_original_new_author (sueb_latein_original_id, sueb_latein_author_id)
  SELECT
    id,
    author3_id
  FROM
    sueb_latein_original_new
  WHERE
    author3_id != 0;


SELECT(delete_superfluos_columns('sueb_latein_original', 'author', ''));
SELECT(delete_superfluos_columns('sueb_latein_original', 'author', '_new'));
SELECT(delete_superfluos_columns('sueb_latein_original_new', 'author',''));
SELECT(delete_superfluos_columns('sueb_latein_original_new', 'author','_new'));


SELECT(split_new_into_separate('sueb_latein_translation', 'translator'));
SELECT(split_new_into_separate('sueb_latein_translation_new', 'translator'));

SELECT(add_m_n_relation('sueb_latein_translation', 'translation' , 'sueb_latein_translator', 'translator',''));
ALTER TABLE sueb_latein_translation_sueb_latein_translator RENAME TO sueb_latein_translation_translator;


SELECT(add_m_n_relation('sueb_latein_translation', 'translation', 'sueb_latein_translator', 'translator','_new'));
ALTER TABLE sueb_latein_translation_sueb_latein_translator_new RENAME TO sueb_latein_translation_translator_new;


SELECT(add_m_n_relation('sueb_latein_translation_new', 'translation', 'sueb_latein_translator', 'translator', '_new'));
ALTER TABLE sueb_latein_translation_new_sueb_latein_translator_new RENAME TO sueb_latein_translation_new_translator_new;

-- translation_new_translator

  DROP TABLE IF EXISTS sueb_latein_translation_new_translator;

  CREATE TABLE sueb_latein_translation_new_translator(
    id    SERIAL PRIMARY KEY,
    sueb_latein_translation_id BIGINT NOT NULL,
    sueb_latein_translator_id BIGINT NOT NULL,
    FOREIGN KEY (sueb_latein_translation_id) REFERENCES sueb_latein_translation_new (id),
    FOREIGN KEY (sueb_latein_translator_id) REFERENCES sueb_latein_translator (id)
  );

  INSERT INTO sueb_latein_translator (migration_notes, migration_generated)
    VALUES ('Angelegt weil original einen FK auf author hatte aber keine Werte eingetragen waren', true)
    RETURNING id;

  UPDATE sueb_latein_translation_new
  SET translator0_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_translation_new.id IN(
    SELECT id
    FROM sueb_latein_translation_new
    WHERE translator0_id NOT IN(
      SELECT id
      FROM sueb_latein_translator
    )
  );

  INSERT INTO sueb_latein_translation_new_translator (sueb_latein_translation_id, sueb_latein_translator_id)
  SELECT
    id,
    translator0_id
  FROM
    sueb_latein_translation_new
  WHERE
    translator0_id != 0;

  UPDATE sueb_latein_translation_new
  SET translator1_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_translation_new.id IN(
    SELECT id
    FROM sueb_latein_translation_new
    WHERE translator1_id NOT IN(
      SELECT id
      FROM sueb_latein_translator
    )
  );

  INSERT INTO sueb_latein_translation_new_translator (sueb_latein_translation_id, sueb_latein_translator_id)
  SELECT
    id,
    translator1_id
  FROM
    sueb_latein_translation_new
  WHERE
    translator1_id != 0;

  UPDATE sueb_latein_translation_new
  SET translator2_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_translation_new.id IN(
    SELECT id
    FROM sueb_latein_translation_new
    WHERE translator2_id NOT IN(
      SELECT id
      FROM sueb_latein_translator
    )
  );

  INSERT INTO sueb_latein_translation_new_translator (sueb_latein_translation_id, sueb_latein_translator_id)
  SELECT
    id,
    translator2_id
  FROM
    sueb_latein_translation_new
  WHERE
    translator2_id != 0;

  UPDATE sueb_latein_translation_new
  SET translator3_id=subquery.id
  FROM (SELECT id
      FROM sueb_latein_translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE sueb_latein_translation_new.id IN(
    SELECT id
    FROM sueb_latein_translation_new
    WHERE translator3_id NOT IN(
      SELECT id
      FROM sueb_latein_translator
    )
  );

  INSERT INTO sueb_latein_translation_new_translator (sueb_latein_translation_id, sueb_latein_translator_id)
  SELECT
    id,
    translator3_id
  FROM
    sueb_latein_translation_new
  WHERE
    translator3_id != 0;

SELECT(delete_superfluos_columns('sueb_latein_translation', 'translator', ''));
SELECT(delete_superfluos_columns('sueb_latein_translation', 'translator', '_new'));
SELECT(delete_superfluos_columns('sueb_latein_translation_new', 'translator',''));
SELECT(delete_superfluos_columns('sueb_latein_translation_new', 'translator','_new'));



