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

    INSERT INTO location_new (loc_id, migration_notes, migration_generated)
      SELECT
        loc_assign.loc_id,
        'Angelegt weil loc_assign einen FK auf location_new hatte aber keine Werte eingetragen waren',
        true
      FROM loc_assign
      WHERE loc_assign.loc_id NOT IN (
        SELECT location_new.loc_id
        FROM location_new
      )
      GROUP BY loc_id;

    alter table loc_assign
    add constraint location_new_fk
      foreign key (loc_id) references "location_new"
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

    INSERT INTO original_new (orig_id, migration_notes, migration_generated)
      SELECT
        loc_assign.orig_id,
        'Angelegt weil loc_assign einen FK auf origninal_new hatte aber keine Werte eingetragen waren',
        true
      FROM loc_assign
      WHERE loc_assign.orig_id NOT IN (
        SELECT original_new.orig_id
        FROM original_new
      )
      GROUP BY orig_id;

    alter table loc_assign
    add constraint original_new_fk
      foreign key (orig_id) references "original_new"
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

    INSERT INTO translation_new (trans_id, migration_notes, migration_generated)
      SELECT
        loc_assign.trans_id,
        'Angelegt weil loc_assign einen FK auf translation_new hatte aber keine Werte eingetragen waren',
        true
      FROM loc_assign
      WHERE loc_assign.trans_id NOT IN (
        SELECT translation_new.trans_id
        FROM translation_new
      )
      GROUP BY trans_id;
    alter table loc_assign
      add constraint translation_new_fk
        foreign key (trans_id) references "translation_new"
          on update cascade on delete restrict;

-- Adds foreign_key constraints for orig_assign

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
      foreign key (orig_id) references "original_new"
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

    INSERT INTO translation_new(trans_id, migration_notes, migration_generated)
    SELECT
          orig_assign.trans_id,
          'Angelegt weil orig_assign einen FK auf translation_new hatte aber keine Werte eingetragen waren',
          true
        FROM orig_assign
        WHERE orig_assign.trans_id NOT IN (
          SELECT translation_new.trans_id
          FROM translation_new
        )
        GROUP BY trans_id;

    alter table orig_assign
      add constraint trans_new_fk
        foreign key (trans_id) references "translation_new"
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
      foreign key (orig_diff_id) references "original_new"
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
      foreign key (trans_diff_id) references "translation_new"
        on update cascade on delete restrict;