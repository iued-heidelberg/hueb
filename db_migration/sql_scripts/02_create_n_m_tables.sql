\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;


SELECT(split_new_into_separate('original', 'author'));
SELECT(split_new_into_separate('original_new', 'author'));

SELECT(add_m_n_relation('original', 'author', ''));
SELECT(add_m_n_relation('original', 'author', '_new'));
SELECT(add_m_n_relation('original_new', 'author','_new'));

-- original_new_author

  DROP TABLE IF EXISTS original_new_author;

  CREATE TABLE original_new_author(
    id    SERIAL PRIMARY KEY,
    original_id BIGINT NOT NULL,
    author_id BIGINT NOT NULL,
    FOREIGN KEY (original_id) REFERENCES original_new (id),
    FOREIGN KEY (author_id) REFERENCES author (id)
  );

  INSERT INTO author (migration_notes, migration_generated)
    VALUES ('Angelegt weil original einen FK auf author hatte aber keine Werte eingetragen waren', true)
    RETURNING id;

  UPDATE original_new
  SET author0_id=subquery.id
  FROM (SELECT id
      FROM author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE original_new.id IN(
    SELECT id
    FROM original_new
    WHERE author0_id NOT IN(
      SELECT id
      FROM author
    )
  );

  INSERT INTO original_new_author (original_id, author_id)
  SELECT
    id,
    author0_id
  FROM
    original_new
  WHERE
    author0_id != 0;


  UPDATE original_new
  SET author1_id=subquery.id
  FROM (SELECT id
      FROM author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE original_new.id IN(
    SELECT id
    FROM original_new
    WHERE author1_id NOT IN(
      SELECT id
      FROM author
    )
  );

  INSERT INTO original_new_author (original_id, author_id)
  SELECT
    id,
    author1_id
  FROM
    original_new
  WHERE
    author1_id != 0;


  UPDATE original_new
  SET author2_id=subquery.id
  FROM (SELECT id
      FROM author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE original_new.id IN(
    SELECT id
    FROM original_new
    WHERE author2_id NOT IN(
      SELECT id
      FROM author
    )
  );

  INSERT INTO original_new_author (original_id, author_id)
  SELECT
    id,
    author2_id
  FROM
    original_new
  WHERE
    author2_id != 0;

  UPDATE original_new
  SET author3_id=subquery.id
  FROM (SELECT id
      FROM author
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE original_new.id IN(
    SELECT id
    FROM original_new
    WHERE author3_id NOT IN(
      SELECT id
      FROM author
    )
  );

  INSERT INTO original_new_author (original_id, author_id)
  SELECT
    id,
    author3_id
  FROM
    original_new
  WHERE
    author3_id != 0;


SELECT(delete_superfluos_columns('original', 'author', ''));
SELECT(delete_superfluos_columns('original', 'author', '_new'));
SELECT(delete_superfluos_columns('original_new', 'author',''));
SELECT(delete_superfluos_columns('original_new', 'author','_new'));


SELECT(split_new_into_separate('translation', 'translator'));
SELECT(split_new_into_separate('translation_new', 'translator'));

SELECT(add_m_n_relation('translation', 'translator', ''));
SELECT(add_m_n_relation('translation', 'translator', '_new'));
SELECT(add_m_n_relation('translation_new', 'translator', '_new'));

-- translation_new_translator

  DROP TABLE IF EXISTS translation_new_translator;

  CREATE TABLE translation_new_translator(
    id    SERIAL PRIMARY KEY,
    translation_id BIGINT NOT NULL,
    translator_id BIGINT NOT NULL,
    FOREIGN KEY (translation_id) REFERENCES translation_new (id),
    FOREIGN KEY (translator_id) REFERENCES translator (id)
  );

  INSERT INTO translator (migration_notes, migration_generated)
    VALUES ('Angelegt weil original einen FK auf author hatte aber keine Werte eingetragen waren', true)
    RETURNING id;

  UPDATE translation_new
  SET translator0_id=subquery.id
  FROM (SELECT id
      FROM translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE translation_new.id IN(
    SELECT id
    FROM translation_new
    WHERE translator0_id NOT IN(
      SELECT id
      FROM translator
    )
  );

  INSERT INTO translation_new_translator (translation_id, translator_id)
  SELECT
    id,
    translator0_id
  FROM
    translation_new
  WHERE
    translator0_id != 0;

  UPDATE translation_new
  SET translator1_id=subquery.id
  FROM (SELECT id
      FROM translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE translation_new.id IN(
    SELECT id
    FROM translation_new
    WHERE translator1_id NOT IN(
      SELECT id
      FROM translator
    )
  );

  INSERT INTO translation_new_translator (translation_id, translator_id)
  SELECT
    id,
    translator1_id
  FROM
    translation_new
  WHERE
    translator1_id != 0;

  UPDATE translation_new
  SET translator2_id=subquery.id
  FROM (SELECT id
      FROM translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE translation_new.id IN(
    SELECT id
    FROM translation_new
    WHERE translator2_id NOT IN(
      SELECT id
      FROM translator
    )
  );

  INSERT INTO translation_new_translator (translation_id, translator_id)
  SELECT
    id,
    translator2_id
  FROM
    translation_new
  WHERE
    translator2_id != 0;

  UPDATE translation_new
  SET translator3_id=subquery.id
  FROM (SELECT id
      FROM translator
      WHERE migration_generated=true
      LIMIT 1) as subquery
  WHERE translation_new.id IN(
    SELECT id
    FROM translation_new
    WHERE translator3_id NOT IN(
      SELECT id
      FROM translator
    )
  );

  INSERT INTO translation_new_translator (translation_id, translator_id)
  SELECT
    id,
    translator3_id
  FROM
    translation_new
  WHERE
    translator3_id != 0;

SELECT(delete_superfluos_columns('translation', 'translator', ''));
SELECT(delete_superfluos_columns('translation', 'translator', '_new'));
SELECT(delete_superfluos_columns('translation_new', 'translator',''));
SELECT(delete_superfluos_columns('translation_new', 'translator','_new'));



