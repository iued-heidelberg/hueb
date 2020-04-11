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
    SELECT(clean_up_relation('loc_assign', 'loc_id', 'location'));

  -- location_new_fk
    SELECT(clean_up_relation('loc_assign', 'loc_new_id', 'location_new'));

  -- original_fk
    SELECT(clean_up_relation('loc_assign', 'orig_id', 'original'));

  -- original_new_fk
    SELECT(clean_up_relation('loc_assign', 'orig_new_id', 'original_new'));

  -- translation_fk
    SELECT(clean_up_relation('loc_assign', 'trans_id', 'translation'));

  -- translation_new_fk
    SELECT(clean_up_relation('loc_assign', 'trans_new_id', 'translation_new'));

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
    SELECT(clean_up_relation('orig_assign', 'orig_id', 'original'));
  -- orig_new_fk
    SELECT(clean_up_relation('orig_assign', 'orig_new_id', 'original_new'));

  -- trans_fk
    SELECT(clean_up_relation('orig_assign', 'trans_id', 'translation'));
  -- trans_new_fk
    SELECT(clean_up_relation('orig_assign', 'trans_new_id', 'translation_new'));

  -- orig_diff_fk
    SELECT(clean_up_relation('orig_assign', 'orig_diff_id', 'original'));
  -- orig_diff_new_fk
    SELECT(clean_up_relation('orig_assign', 'orig_diff_new_id', 'original_new'));

  -- trans_diff_fk
    SELECT(clean_up_relation('orig_assign', 'trans_diff_id', 'translation'));
  -- trans_diff_new_fk
    SELECT(clean_up_relation('orig_assign', 'trans_diff_new_id', 'translation_new'));


-- Adds foreign_key constraints for original


  -- ddc_fk
    SELECT(clean_up_relation('original', 'ddc_id', 'ddc_german'));

  --language_fk
    SELECT(clean_up_relation('original', 'language_id', 'language'));

  --user_fk
    SELECT(clean_up_relation('original', 'user_id', 'user'));

  --country_fk
    SELECT(clean_up_relation('original', 'country_id', 'country'));

-- Adds foreign_key constraints for original_new

  -- ddc_fk
    SELECT(clean_up_relation('original_new', 'ddc_id', 'ddc_german'));

  --language_fk
    SELECT(clean_up_relation('original_new', 'language_id', 'language'));

  --user_fk
    SELECT(clean_up_relation('original_new', 'user_id', 'user'));

  --country_fk
    SELECT(clean_up_relation('original', 'country_id', 'country'));

-- Adds foreign_key constraints for translation
  -- ddc_fk
    SELECT(clean_up_relation('translation', 'ddc_id', 'ddc_german'));

  --author_fk
    SELECT(clean_up_relation('translation', 'author_id', 'author'));

  --author_new_fk
    alter table translation drop column if exists author_new_id;
    alter table translation add column author_new_id bigint;
    update translation
    set author_new_id = author_id;
    SELECT(clean_up_relation('translation', 'author_new_id', 'author'));

  --language_fk
    SELECT(clean_up_relation('translation', 'language_id', 'language'));

  --via_language_fk
    SELECT(clean_up_relation('translation', 'via_language_id', 'language'));

   --user_fk
    SELECT(clean_up_relation('translation', 'user_id', 'user'));

  --country_fk
    SELECT(clean_up_relation('translation', 'country_id', 'country'));

-- Adds foreign_key constraints for translation_new
-- ddc_fk
    SELECT(clean_up_relation('translation_new', 'ddc_id', 'ddc_german'));

  --author_fk
    SELECT(clean_up_relation('translation_new', 'author_id', 'author'));

  --author_new_fk
    alter table translation_new drop column if exists author_new_id;
    alter table translation_new add column author_new_id bigint;
    update translation_new
    set author_new_id = author_id;
    SELECT(clean_up_relation('translation_new', 'author_new_id', 'author'));

  --language_fk
    SELECT(clean_up_relation('translation_new', 'language_id', 'language'));

  --via_language_fk
    SELECT(clean_up_relation('translation_new', 'via_language_id', 'language'));

   --user_fk
    SELECT(clean_up_relation('translation_new', 'user_id', 'user'));

  --country_fk
    SELECT(clean_up_relation('translation_new', 'country_id', 'country'));

-- Adds foreign_key constraints for translator
  -- user_id
    SELECT(clean_up_relation('translator', 'user_id', 'user'));


-- Adds foreign_key constraints for translator_new
  -- user_id
    SELECT(clean_up_relation('translator_new', 'user_id', 'user'));
