\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;


-- Adds foreign_key constraints for author
  alter table sueb_latein_author drop constraint if exists user_fk;
  alter table sueb_latein_author
    add constraint user_fk
      foreign key (user_id) references "sueb_latein_user"
        on update cascade on delete restrict;

-- Adds foreign_key constraints for author_new
  alter table sueb_latein_author_new drop constraint if exists user_fk;
  alter table sueb_latein_author_new
    add constraint user_fk
      foreign key (user_id) references "sueb_latein_user"
        on update cascade on delete restrict;

-- Adds foreign_key constraints for country
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for ddc_deutsch
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for language
  -- no foreign_key constraints necessary

-- Adds foreign_key constraints for loc_assign
  -- add new columns
    alter table sueb_latein_loc_assign drop column if exists loc_new_id;
    alter table sueb_latein_loc_assign drop column if exists orig_new_id;
    alter table sueb_latein_loc_assign drop column if EXISTS trans_new_id;

    alter table sueb_latein_loc_assign add column loc_new_id bigint;
    alter table sueb_latein_loc_assign add column orig_new_id bigint;
    alter table sueb_latein_loc_assign add column trans_new_id bigint;

    update sueb_latein_loc_assign
    set orig_new_id = orig_id,
        loc_new_id = loc_id,
        trans_new_id = trans_id;

  -- location_fk
    SELECT(clean_up_relation('sueb_latein_loc_assign', 'loc_id', 'sueb_latein_location'));

  -- location_new_fk
    SELECT(clean_up_relation('sueb_latein_loc_assign', 'loc_new_id', 'sueb_latein_location_new'));

  -- original_fk
    SELECT(clean_up_relation('sueb_latein_loc_assign', 'orig_id', 'sueb_latein_original'));

  -- original_new_fk
    SELECT(clean_up_relation('sueb_latein_loc_assign', 'orig_new_id', 'sueb_latein_original_new'));

  -- translation_fk
    SELECT(clean_up_relation('sueb_latein_loc_assign', 'trans_id', 'sueb_latein_translation'));

  -- translation_new_fk
    SELECT(clean_up_relation('sueb_latein_loc_assign', 'trans_new_id', 'sueb_latein_translation_new'));

-- Adds foreign_key constraints for orig_assign
  -- add new columns
    alter table sueb_latein_orig_assign drop column if exists orig_new_id;
    alter table sueb_latein_orig_assign drop column if EXISTS trans_new_id;
    alter table sueb_latein_orig_assign drop column if exists orig_diff_new_id;
    alter table sueb_latein_orig_assign drop column if EXISTS trans_diff_new_id;

    alter table sueb_latein_orig_assign add column orig_new_id bigint;
    alter table sueb_latein_orig_assign add column trans_new_id bigint;
    alter table sueb_latein_orig_assign add column orig_diff_new_id bigint;
    alter table sueb_latein_orig_assign add column trans_diff_new_id bigint;

    update sueb_latein_orig_assign
    set orig_new_id = orig_id,
        trans_new_id = trans_id,
        orig_diff_new_id = orig_diff_id,
        trans_diff_new_id = trans_diff_id;

  -- orig_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'orig_id', 'sueb_latein_original'));
  -- orig_new_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'orig_new_id', 'sueb_latein_original_new'));

  -- trans_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'trans_id', 'sueb_latein_translation'));
  -- trans_new_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'trans_new_id', 'sueb_latein_translation_new'));

  -- orig_diff_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'orig_diff_id', 'sueb_latein_original', '', '_diff'));
  -- orig_diff_new_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'orig_diff_new_id', 'sueb_latein_original_new', '', '_diff'));

  -- trans_diff_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'trans_diff_id', 'sueb_latein_translation', '', '_diff'));
  -- trans_diff_new_fk
    SELECT(clean_up_relation('sueb_latein_orig_assign', 'trans_diff_new_id', 'sueb_latein_translation_new', '', '_diff'));


-- Adds foreign_key constraints for original


  -- ddc_fk
    SELECT(clean_up_relation('sueb_latein_original', 'ddc_id', 'sueb_latein_ddc_german'));

  --language_fk
    SELECT(clean_up_relation('sueb_latein_original', 'language_id', 'sueb_latein_language'));

  --user_fk
    SELECT(clean_up_relation('sueb_latein_original', 'user_id', 'sueb_latein_user'));

  --country_fk
    SELECT(clean_up_relation('sueb_latein_original', 'country_id', 'sueb_latein_country'));

-- Adds foreign_key constraints for original_new

  -- ddc_fk
    SELECT(clean_up_relation('sueb_latein_original_new', 'ddc_id', 'sueb_latein_ddc_german'));

  --language_fk
    SELECT(clean_up_relation('sueb_latein_original_new', 'language_id', 'sueb_latein_language'));

  --user_fk
    SELECT(clean_up_relation('sueb_latein_original_new', 'user_id', 'sueb_latein_user'));

  --country_fk
    SELECT(clean_up_relation('sueb_latein_original_new', 'country_id', 'sueb_latein_country'));

-- Adds foreign_key constraints for translation
  -- ddc_fk
    SELECT(clean_up_relation('sueb_latein_translation', 'ddc_id', 'sueb_latein_ddc_german'));

  --author_fk
    SELECT(clean_up_relation('sueb_latein_translation', 'author_id', 'sueb_latein_author'));

  --author_new_fk
    alter table sueb_latein_translation drop column if exists author_new_id;
    alter table sueb_latein_translation add column author_new_id bigint;
    update sueb_latein_translation
    set author_new_id = author_id;
    SELECT(clean_up_relation('sueb_latein_translation', 'author_new_id', 'sueb_latein_author_new'));

  --language_fk
    SELECT(clean_up_relation('sueb_latein_translation', 'language_id', 'sueb_latein_language'));

  --via_language_fk
    SELECT(clean_up_relation('sueb_latein_translation', 'via_language_id', 'sueb_latein_language', 'via_'));

   --user_fk
    SELECT(clean_up_relation('sueb_latein_translation', 'user_id', 'sueb_latein_user'));

  --country_fk
    SELECT(clean_up_relation('sueb_latein_translation', 'country_id', 'sueb_latein_country'));

-- Adds foreign_key constraints for translation_new
-- ddc_fk
    SELECT(clean_up_relation('sueb_latein_translation_new', 'ddc_id', 'sueb_latein_ddc_german'));

  --author_fk
    SELECT(clean_up_relation('sueb_latein_translation_new', 'author_id', 'sueb_latein_author'));

  --author_new_fk
    alter table sueb_latein_translation_new drop column if exists author_new_id;
    alter table sueb_latein_translation_new add column author_new_id bigint;
    update sueb_latein_translation_new
    set author_new_id = author_id;

    SELECT(clean_up_relation('sueb_latein_translation_new', 'author_new_id', 'sueb_latein_author_new'));

  --language_fk
    SELECT(clean_up_relation('sueb_latein_translation_new', 'language_id', 'sueb_latein_language'));

  --via_language_fk
    SELECT(clean_up_relation('sueb_latein_translation_new', 'via_language_id', 'sueb_latein_language', 'via_'));

   --user_fk
    SELECT(clean_up_relation('sueb_latein_translation_new', 'user_id', 'sueb_latein_user'));

  --country_fk
    SELECT(clean_up_relation('sueb_latein_translation_new', 'country_id', 'sueb_latein_country'));

-- Adds foreign_key constraints for translator
  -- user_id
    SELECT(clean_up_relation('sueb_latein_translator', 'user_id', 'sueb_latein_user'));


-- Adds foreign_key constraints for translator_new
  -- user_id
    SELECT(clean_up_relation('sueb_latein_translator_new', 'user_id', 'sueb_latein_user'));





DROP SEQUENCE IF EXISTS  author_auth_id_seq;
DROP SEQUENCE IF EXISTS  author_new_auth_id_seq;
DROP SEQUENCE IF EXISTS  loc_assign_loc_assign_id_seq;
DROP SEQUENCE IF EXISTS  location_loc_id_seq;
DROP SEQUENCE IF EXISTS  location_new_loc_id_seq;
DROP SEQUENCE IF EXISTS  orig_assign_orig_assign_id_seq;
DROP SEQUENCE IF EXISTS  translator_translator_id_seq;
DROP SEQUENCE IF EXISTS  translator_new_translator_id_seq;
