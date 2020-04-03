\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;


-- Adds foreign_key constraints for author
  alter table author drop constraint if exists user_fk;
  alter table author
    add constraint user_fk
      foreign key (user_id) references "user"
        on update cascade on delete restrict;

-- Adds foreign_key constraints for author_new
  alter table author_new drop constraint if exists user_fk;
  alter table author_new
    add constraint user_fk
      foreign key (user_id) references "user"
        on update cascade on delete restrict;

-- Adds foreign_key constraints for country
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for ddc_deutsch
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for language
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for loc_assign
-- Adds foreign_key constraints for loc_assign
  -- add new columns
    alter table loc_assign drop column if exists loc_new_id;
    alter table loc_assign drop column if exists orig_new_id;
    alter table loc_assign drop column if EXISTS trans_new_id;

    alter table loc_assign add column loc_new_id bigint;
    alter table loc_assign add column orig_new_id bigint;
    alter table loc_assign add column trans_new_id bigint;

    update loc_assign
    set orig_new_id = orig_id,
        loc_new_id = loc_id,
        trans_new_id = trans_id;

  -- location_fk

    alter table loc_assign drop constraint if exists location_fk;

    INSERT INTO location (loc_id, migration_notes, migration_generated)
      SELECT
        loc_assign.loc_id,
        'Angelegt weil loc_assign einen FK auf location hatte aber keine Werte eingetragen waren',
        true
      FROM loc_assign
      WHERE loc_assign.loc_id NOT IN (
        SELECT location.loc_id
        FROM location
      )
      GROUP BY loc_id;

    alter table loc_assign
    add constraint location_fk
      foreign key (loc_id) references "location"
        on update cascade on delete restrict;

  -- location_new_fk
    alter table loc_assign drop constraint if exists location_new_fk;

    alter table loc_assign
    add constraint location_new_fk
      foreign key (loc_new_id) references "location_new"
        on update cascade on delete restrict;

  -- original_fk

    alter table loc_assign drop constraint if exists original_fk;

    INSERT INTO original (orig_id, migration_notes, migration_generated)
      SELECT
        loc_assign.orig_id,
        'Angelegt weil loc_assign einen FK auf original hatte aber keine Werte eingetragen waren',
        true
      FROM loc_assign
      WHERE loc_assign.orig_id NOT IN (
        SELECT original.orig_id
        FROM original
      )
      GROUP BY orig_id;

    alter table loc_assign
    add constraint original_fk
      foreign key (orig_id) references "original"
        on update cascade on delete restrict;

  -- original_new_fk
    alter table loc_assign drop constraint if exists original_new_fk;

    alter table loc_assign
    add constraint original_new_fk
      foreign key (orig_new_id) references "original_new"
        on update cascade on delete restrict;

  -- translation_fk
    alter table loc_assign drop constraint if exists translation_fk;

    INSERT INTO translation (trans_id, migration_notes, migration_generated)
      SELECT
        loc_assign.trans_id,
        'Angelegt weil loc_assign einen FK auf translation hatte aber keine Werte eingetragen waren',
        true
      FROM loc_assign
      WHERE loc_assign.trans_id NOT IN (
        SELECT translation.trans_id
        FROM translation
      )
      GROUP BY trans_id;

    alter table loc_assign
    add constraint translation_fk
      foreign key (trans_id) references "translation"
        on update cascade on delete restrict;

  -- translation_new_fk
    alter table loc_assign drop constraint if exists translation_new_fk;

    alter table loc_assign
      add constraint translation_new_fk
        foreign key (trans_new_id) references "translation_new"
          on update cascade on delete restrict;


-- Adds foreign_key constraints for orig_assign
  -- add new columns
    alter table orig_assign drop column if exists orig_new_id;
    alter table orig_assign drop column if EXISTS trans_new_id;
    alter table orig_assign drop column if exists orig_diff_new_id;
    alter table orig_assign drop column if EXISTS trans_diff_new_id;

    alter table orig_assign add column orig_new_id bigint;
    alter table orig_assign add column trans_new_id bigint;
    alter table orig_assign add column orig_diff_new_id bigint;
    alter table orig_assign add column trans_diff_new_id bigint;

    update orig_assign
    set orig_new_id = orig_id,
        trans_new_id = trans_id,
        orig_diff_new_id = orig_diff_id,
        trans_diff_new_id = trans_diff_id;

  -- orig_fk
    alter table orig_assign drop constraint if exists orig_fk;

    INSERT INTO original (orig_id, migration_notes, migration_generated)
    SELECT
          orig_assign.orig_id,
          'Angelegt weil orig_assign einen FK auf original hatte aber keine Werte eingetragen waren',
          true
        FROM orig_assign
        WHERE orig_assign.orig_id NOT IN (
          SELECT original.orig_id
          FROM original
        )
        GROUP BY orig_id;

    alter table orig_assign
      add constraint orig_fk
        foreign key (orig_id) references "original"
          on update cascade on delete restrict;

  -- orig_new_fk
    alter table orig_assign drop constraint if exists orig_new_fk;

    alter table orig_assign
    add constraint orig_new_fk
      foreign key (orig_new_id) references "original_new"
        on update cascade on delete restrict;

  -- trans_fk

    alter table orig_assign drop constraint if exists trans_fk;

    INSERT INTO translation(trans_id, migration_notes, migration_generated)
    SELECT
          orig_assign.trans_id,
          'Angelegt weil orig_assign einen FK auf translation hatte aber keine Werte eingetragen waren',
          true
        FROM orig_assign
        WHERE orig_assign.trans_id NOT IN (
          SELECT translation.trans_id
          FROM translation
        )
        GROUP BY trans_id;


    alter table orig_assign
      add constraint trans_fk
        foreign key (trans_id) references "translation"
          on update cascade on delete restrict;

  -- trans_new_fk
    alter table orig_assign drop constraint if exists trans_new_fk;

    alter table orig_assign
      add constraint trans_new_fk
        foreign key (trans_new_id) references "translation_new"
          on update cascade on delete restrict;

  -- orig_diff_fk
    alter table orig_assign drop constraint if exists orig_diff_fk;

    alter table orig_assign
      add constraint orig_diff_fk
        foreign key (orig_diff_id) references "original"
          on update cascade on delete restrict;

  -- orig_diff_new_fk
    alter table orig_assign drop constraint if exists orig_diff_new_fk;

    alter table orig_assign
    add constraint orig_diff_new_fk
      foreign key (orig_diff_new_id) references "original_new"
        on update cascade on delete restrict;

  -- trans_diff_fk
    alter table orig_assign drop constraint if exists trans_diff_fk;

    alter table orig_assign
      add constraint trans_diff_fk
        foreign key (trans_diff_id) references "translation"
          on update cascade on delete restrict;

  -- trans_diff_new_fk
    alter table orig_assign drop constraint if exists trans_diff_new_fk;

    alter table orig_assign
    add constraint trans_diff_new_fk
      foreign key (trans_diff_new_id) references "translation_new"
        on update cascade on delete restrict;

-- Adds foreign_key constraints for original
  -- add new columns

    alter table original drop column if exists author0_new_id;
    alter table original drop column if exists author1_new_id;
    alter table original drop column if exists author2_new_id;
    alter table original drop column if exists author3_new_id;

    alter table original add column author0_new_id bigint;
    alter table original add column author1_new_id bigint;
    alter table original add column author2_new_id bigint;
    alter table original add column author3_new_id bigint;


    update original
    set author0_new_id = author0_id,
        author1_new_id = author1_id,
        author2_new_id = author2_id,
        author3_new_id = author3_id;


  -- ddc_fk
    alter table original drop constraint if exists ddc_fk;

    alter table original
      add constraint ddc_fk
        foreign key (ddc_id) references "ddc_german"
          on update cascade on delete restrict;

  --author0_fk

    alter table original drop constraint if exists author0_fk;

    INSERT INTO author (author_id, migration_notes, migration_generated)
      SELECT
        original.author0_id,
        'Angelegt weil original einen FK auf author hatte aber keine Werte eingetragen waren',
        true
      FROM original
      WHERE original.author0_id NOT IN (
        SELECT author.author_id
        FROM author
      )
      GROUP BY author0_id;

    alter table original
      add constraint author0_fk
        foreign key (author0_id) references "author"
          on update cascade on delete restrict;

  --author1_fk

    alter table original drop constraint if exists author1_fk;

    alter table original
      add constraint author1_fk
        foreign key (author1_id) references "author"
          on update cascade on delete restrict;

  --author2_fk

    alter table original drop constraint if exists author2_fk;

    alter table original
      add constraint author2_fk
        foreign key (author2_id) references "author"
          on update cascade on delete restrict;

  --author3_fk

    alter table original drop constraint if exists author3_fk;

    alter table original
      add constraint author3_fk
        foreign key (author3_id) references "author"
          on update cascade on delete restrict;

  --author0_new_fk

    alter table original drop constraint if exists author0_new_fk;

    alter table original
      add constraint author0_new_fk
        foreign key (author0_new_id) references "author_new"
          on update cascade on delete restrict;

  --author1_new_fk

    alter table original drop constraint if exists author1_new_fk;

    alter table original
      add constraint author1_new_fk
        foreign key (author1_new_id) references "author_new"
          on update cascade on delete restrict;

  --author2_new_fk

    alter table original drop constraint if exists author2_new_fk;

    alter table original
      add constraint author2_new_fk
        foreign key (author2_new_id) references "author_new"
          on update cascade on delete restrict;

  --author3_new_fk

    alter table original drop constraint if exists author3_new_fk;

    alter table original
      add constraint author3_new_fk
        foreign key (author3_new_id) references "author_new"
          on update cascade on delete restrict;

  --language_fk

    alter table original drop constraint if exists language_fk;

    INSERT INTO language (language_id, migration_notes, migration_generated)
        SELECT
          original.language_id,
          'Angelegt weil original einen FK auf language hatte aber keine Werte eingetragen waren',
          true
        FROM original
        WHERE original.language_id NOT IN (
          SELECT language.language_id
          FROM language
        )
        GROUP BY language_id;

    alter table original
      add constraint language_fk
        foreign key (language_id) references "language"
          on update cascade on delete restrict;

  --user_fk
    alter table original drop constraint if exists user_fk;

    alter table original
          add constraint user_fk
            foreign key (user_id) references "user"
              on update cascade on delete restrict;

  --country_fk

    alter table original drop constraint if exists country_fk;

    INSERT INTO country (country_id, migration_notes, migration_generated)
      SELECT
        original.country_id,
        'Angelegt weil original einen FK auf country hatte aber keine Werte eingetragen waren',
        true
      FROM original
      WHERE original.country_id NOT IN (
        SELECT country.country_id
        FROM country
      )
      GROUP BY country_id;

    alter table original
          add constraint country_fk
            foreign key (country_id) references "country"
              on update cascade on delete restrict;

-- Adds foreign_key constraints for original_new
  -- add new columns
    alter table original_new drop column if exists author0_new_id;
    alter table original_new drop column if exists author1_new_id;
    alter table original_new drop column if exists author2_new_id;
    alter table original_new drop column if exists author3_new_id;

    alter table original_new add column author0_new_id bigint;
    alter table original_new add column author1_new_id bigint;
    alter table original_new add column author2_new_id bigint;
    alter table original_new add column author3_new_id bigint;


    update original_new
    set author0_new_id = author0_id,
        author1_new_id = author1_id,
        author2_new_id = author2_id,
        author3_new_id = author3_id;

  -- ddc_fk
    alter table original_new drop constraint if exists ddc_fk;

    alter table original_new
      add constraint ddc_fk
        foreign key (ddc_id) references "ddc_german"
          on update cascade on delete restrict;

  --author0_fk
    alter table original_new drop constraint if exists author0_fk;

    INSERT INTO author (author_id, migration_notes, migration_generated)
      SELECT
        original_new.author0_id,
        'Angelegt weil original_new einen FK auf author hatte aber keine Werte eingetragen waren',
        true
      FROM original_new
      WHERE original_new.author0_id NOT IN (
        SELECT author.author_id
        FROM author
      )
      GROUP BY author0_id;

    alter table original_new
      add constraint author0_fk
        foreign key (author0_id) references "author"
          on update cascade on delete restrict;

  --author1_fk

    alter table original_new drop constraint if exists author1_fk;

      INSERT INTO author (author_id, migration_notes, migration_generated)
      SELECT
        original_new.author1_id,
        'Angelegt weil original_new einen FK auf author hatte aber keine Werte eingetragen waren',
        true
      FROM original_new
      WHERE original_new.author1_id NOT IN (
        SELECT author.author_id
        FROM author
      )
      GROUP BY author1_id;

    alter table original_new
      add constraint author1_fk
        foreign key (author1_id) references "author"
          on update cascade on delete restrict;

  --author2_fk

    alter table original_new drop constraint if exists author2_fk;

      INSERT INTO author (author_id, migration_notes, migration_generated)
      SELECT
        original_new.author2_id,
        'Angelegt weil original_new einen FK auf author hatte aber keine Werte eingetragen waren',
        true
      FROM original_new
      WHERE original_new.author2_id NOT IN (
        SELECT author.author_id
        FROM author
      )
      GROUP BY author2_id;

    alter table original_new
      add constraint author2_fk
        foreign key (author2_id) references "author"
          on update cascade on delete restrict;

  --author3_fk
      alter table original_new drop constraint if exists author3_fk;

      INSERT INTO author (author_id, migration_notes, migration_generated)
      SELECT
        original_new.author3_id,
        'Angelegt weil original_new einen FK auf author hatte aber keine Werte eingetragen waren',
        true
      FROM original_new
      WHERE original_new.author3_id NOT IN (
        SELECT author.author_id
        FROM author
      )
      GROUP BY author3_id;

    alter table original_new
      add constraint author3_fk
        foreign key (author3_id) references "author"
          on update cascade on delete restrict;

  --author0_new_fk

      alter table original_new drop constraint if exists author0_new_fk;

      alter table original_new
        add constraint author0_new_fk
          foreign key (author0_new_id) references "author_new"
            on update cascade on delete restrict;

  --author1_new_fk

      alter table original_new drop constraint if exists author1_new_fk;

      alter table original_new
        add constraint author1_new_fk
          foreign key (author1_new_id) references "author_new"
            on update cascade on delete restrict;


  --author2_new_fk

      alter table original_new drop constraint if exists author2_new_fk;

      alter table original_new
        add constraint author2_new_fk
          foreign key (author2_new_id) references "author_new"
            on update cascade on delete restrict;


  --author3_new_fk

      alter table original_new drop constraint if exists author3_new_fk;

      alter table original_new
        add constraint author3_new_fk
          foreign key (author3_new_id) references "author_new"
            on update cascade on delete restrict;

  --language_fk

    alter table original_new drop constraint if exists language_fk;

    alter table original_new
      add constraint language_fk
        foreign key (language_id) references "language"
          on update cascade on delete restrict;

  --user_fk
    alter table original_new drop constraint if exists user_fk;

    alter table original_new
          add constraint user_fk
            foreign key (user_id) references "user"
              on update cascade on delete restrict;

  --country_fk


    alter table original_new drop constraint if exists country_fk;

    alter table original_new
          add constraint country_fk
            foreign key (country_id) references "country"
              on update cascade on delete restrict;

-- Adds foreign_key constraints for translation
  -- add new columns
    alter table translation drop column if exists translator0_new_id;
    alter table translation drop column if exists translator1_new_id;
    alter table translation drop column if exists translator2_new_id;
    alter table translation drop column if exists translator3_new_id;
    alter table translation drop column if exists author_new_id;

    alter table translation add column translator0_new_id bigint;
    alter table translation add column translator1_new_id bigint;
    alter table translation add column translator2_new_id bigint;
    alter table translation add column translator3_new_id bigint;
    alter table translation add column author_new_id bigint;


    update translation
    set translator0_new_id = translator0_id,
        translator1_new_id = translator1_id,
        translator2_new_id = translator2_id,
        translator3_new_id = translator3_id,
        author_new_id = author_id;
  -- ddc_fk
    alter table translation drop constraint if exists ddc_fk;

    alter table translation
      add constraint ddc_fk
        foreign key (ddc_id) references "ddc_german"
          on update cascade on delete restrict;

  --translator0_fk
    alter table translation drop constraint if exists translator0_fk;

    INSERT INTO translator (translator_id, migration_notes, migration_generated)
      SELECT
        translation.translator0_id,
        'Angelegt weil translation einen FK auf translator hatte aber keine Werte eingetragen waren',
        true
      FROM translation
      WHERE translation.translator0_id NOT IN (
        SELECT translator.translator_id
        FROM translator
      )
      GROUP BY translator0_id;

    alter table translation
      add constraint translator0_fk
        foreign key (translator0_id) references "translator"
          on update cascade on delete restrict;

  --translator1_fk
    alter table translation drop constraint if exists translator1_fk;

    alter table translation
      add constraint translator1_fk
        foreign key (translator1_id) references "translator"
          on update cascade on delete restrict;

  --translator2_fk
    alter table translation drop constraint if exists translator2_fk;

    alter table translation
      add constraint translator2_fk
        foreign key (translator2_id) references "translator"
          on update cascade on delete restrict;

  --translator3_fk
    alter table translation drop constraint if exists translator3_fk;

    alter table translation
      add constraint translator3_fk
        foreign key (translator3_id) references "translator"
          on update cascade on delete restrict;

  --translator0_new_fk
    alter table translation drop constraint if exists translator0_new_fk;

    alter table translation
      add constraint translator0_new_fk
        foreign key (translator0_new_id) references "translator_new"
          on update cascade on delete restrict;

  --translator1_new_fk
    alter table translation drop constraint if exists translator1_new_fk;

    alter table translation
      add constraint translator1_new_fk
        foreign key (translator1_new_id) references "translator_new"
          on update cascade on delete restrict;

  --translator2_new_fk
    alter table translation drop constraint if exists translator2_new_fk;

    alter table translation
      add constraint translator2_new_fk
        foreign key (translator2_new_id) references "translator_new"
          on update cascade on delete restrict;

  --translator3_new_fk
      alter table translation drop constraint if exists translator3_new_fk;

      alter table translation
        add constraint translator3_new_fk
          foreign key (translator3_new_id) references "translator_new"
            on update cascade on delete restrict;

  --author_fk
    alter table translation drop constraint if exists author_fk;

    alter table translation
      add constraint author_fk
        foreign key (author_id) references "author"
          on update cascade on delete restrict;

  --author_new_fk
    alter table translation drop constraint if exists author_new_fk;

    alter table translation
      add constraint author_new_fk
        foreign key (author_new_id) references "author_new"
          on update cascade on delete restrict;

  --language_fk
    alter table translation drop constraint if exists language_fk;

    alter table translation
      add constraint language_fk
        foreign key (language_id) references "language"
          on update cascade on delete restrict;

  --via_language_fk
    alter table translation drop constraint if exists via_language_fk;

    alter table translation
      add constraint via_language_fk
        foreign key (language_id) references "language"
          on update cascade on delete restrict;

   --user_fk
    alter table translation drop constraint if exists user_fk;

    alter table translation
      add constraint user_fk
        foreign key (user_id) references "user"
          on update cascade on delete restrict;

  --country_fk

    alter table translation drop constraint if exists country_fk;

    alter table translation
      add constraint country_fk
        foreign key (country_id) references "country"
          on update cascade on delete restrict;

-- Adds foreign_key constraints for translation_new
  -- add new columns
    alter table translation_new drop column if exists translator0_new_id;
    alter table translation_new drop column if exists translator1_new_id;
    alter table translation_new drop column if exists translator2_new_id;
    alter table translation_new drop column if exists translator3_new_id;
    alter table translation_new drop column if exists author_new_id;

    alter table translation_new add column translator0_new_id bigint;
    alter table translation_new add column translator1_new_id bigint;
    alter table translation_new add column translator2_new_id bigint;
    alter table translation_new add column translator3_new_id bigint;
    alter table translation_new add column author_new_id bigint;


    update translation_new
    set translator0_new_id = translator0_id,
        translator1_new_id = translator1_id,
        translator2_new_id = translator2_id,
        translator3_new_id = translator3_id,
        author_new_id = author_id;

  -- ddc_fk
    alter table translation_new drop constraint if exists ddc_fk;

    alter table translation_new
      add constraint ddc_fk
        foreign key (ddc_id) references "ddc_german"
          on update cascade on delete restrict;

  --translator0_fk
    alter table translation_new drop constraint if exists translator0_fk;

    INSERT INTO translator (translator_id, migration_notes, migration_generated)
      SELECT
        translation_new.translator0_id,
        'Angelegt weil translation_new einen FK auf translator hatte aber keine Werte eingetragen waren',
        true
      FROM translation_new
      WHERE translation_new.translator0_id NOT IN (
        SELECT translator.translator_id
        FROM translator
      )
      GROUP BY translator0_id;

    alter table translation_new
      add constraint translator0_fk
        foreign key (translator0_id) references "translator"
          on update cascade on delete restrict;

  --translator1_fk
    alter table translation_new drop constraint if exists translator1_fk;

    INSERT INTO translator (translator_id, migration_notes, migration_generated)
      SELECT
        translation_new.translator1_id,
        'Angelegt weil translation_new einen FK auf translator hatte aber keine Werte eingetragen waren',
        true
      FROM translation_new
      WHERE translation_new.translator1_id NOT IN (
        SELECT translator.translator_id
        FROM translator
      )
      GROUP BY translator1_id;

    alter table translation_new
      add constraint translator1_fk
        foreign key (translator1_id) references "translator"
          on update cascade on delete restrict;

  --translator2_fk
    alter table translation_new drop constraint if exists translator2_fk;

    INSERT INTO translator (translator_id, migration_notes, migration_generated)
      SELECT
        translation_new.translator2_id,
        'Angelegt weil translation_new einen FK auf translator hatte aber keine Werte eingetragen waren',
        true
      FROM translation_new
      WHERE translation_new.translator2_id NOT IN (
        SELECT translator.translator_id
        FROM translator
      )
      GROUP BY translator2_id;

    alter table translation_new
      add constraint translator2_fk
        foreign key (translator2_id) references "translator"
          on update cascade on delete restrict;

  --translator3_fk
    alter table translation_new drop constraint if exists translator3_fk;

    INSERT INTO translator (translator_id, migration_notes, migration_generated)
      SELECT
        translation_new.translator3_id,
        'Angelegt weil translation_new einen FK auf translator hatte aber keine Werte eingetragen waren',
        true
      FROM translation_new
      WHERE translation_new.translator3_id NOT IN (
        SELECT translator.translator_id
        FROM translator
      )
      GROUP BY translator3_id;

    alter table translation_new
      add constraint translator3_fk
        foreign key (translator3_id) references "translator"
          on update cascade on delete restrict;

  --translator0_new_fk
    alter table translation_new drop constraint if exists translator0_new_fk;

    alter table translation_new
      add constraint translator0_new_fk
        foreign key (translator0_new_id) references "translator_new"
          on update cascade on delete restrict;

  --translator1_new_fk
    alter table translation_new drop constraint if exists translator1_new_fk;

    alter table translation_new
      add constraint translator1_new_fk
        foreign key (translator1_new_id) references "translator_new"
          on update cascade on delete restrict;

  --translator2_new_fk
    alter table translation_new drop constraint if exists translator2_new_fk;

    alter table translation_new
      add constraint translator2_new_fk
        foreign key (translator2_new_id) references "translator_new"
          on update cascade on delete restrict;

  --translator3_new_fk
    alter table translation_new drop constraint if exists translator3_new_fk;

    alter table translation_new
      add constraint translator3_new_fk
        foreign key (translator3_new_id) references "translator_new"
          on update cascade on delete restrict;

  --author_fk
    alter table translation_new drop constraint if exists author_fk;

    INSERT INTO author (author_id, migration_notes, migration_generated)
      SELECT
        translation_new.author_id,
        'Angelegt weil translation_new einen FK auf author hatte aber keine Werte eingetragen waren',
        true
      FROM translation_new
      WHERE translation_new.author_id NOT IN (
        SELECT author.author_id
        FROM author
      )
      GROUP BY author_id;

    alter table translation_new
      add constraint author_fk
        foreign key (author_id) references "author"
          on update cascade on delete restrict;

  --author_new_fk
    alter table translation_new drop constraint if exists author_new_fk;

    alter table translation_new
      add constraint author_new_fk
        foreign key (author_new_id) references "author_new"
          on update cascade on delete restrict;

  --language_fk
    alter table translation_new drop constraint if exists language_fk;

    alter table translation_new
      add constraint language_fk
        foreign key (language_id) references "language"
          on update cascade on delete restrict;

  --via_language_fk
    alter table translation_new drop constraint if exists via_language_fk;

    alter table translation_new
      add constraint via_language_fk
        foreign key (language_id) references "language"
          on update cascade on delete restrict;

  --user_fk
    alter table translation_new drop constraint if exists user_fk;

    alter table translation_new
      add constraint user_fk
        foreign key (user_id) references "user"
          on update cascade on delete restrict;

  --country_fk

    alter table translation_new drop constraint if exists country_fk;

    alter table translation_new
      add constraint country_fk
        foreign key (country_id) references "country"
          on update cascade on delete restrict;

-- Adds foreign_key constraints for translator
  -- user_id
    alter table translator drop constraint if exists user_fk;

    alter table translator
      add constraint user_fk
        foreign key (user_id) references "user"
          on update cascade on delete restrict;


-- Adds foreign_key constraints for translator_new
  -- user_id
    alter table translator_new drop constraint if exists user_fk;

    alter table translator_new
      add constraint user_fk
        foreign key (user_id) references "user"
          on update cascade on delete restrict;