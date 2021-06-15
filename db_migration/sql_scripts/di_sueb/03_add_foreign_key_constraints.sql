\set ON_ERROR_STOP true
SET search_path to di_sueb;


-- Adds foreign_key constraints for author
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for collection
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for country
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for ddc_german
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for language
  -- no foreign_key constraints necessary
-- Adds foreign_key constraints for loc_assign
  -- location_fk
    SELECT(clean_up_relation('sueb_loc_assign', 'location_id', 'sueb_location'));

  -- original_fk
    SELECT(clean_up_relation('sueb_loc_assign', 'original_id', 'sueb_original'));

  -- translation_fk
    SELECT(clean_up_relation('sueb_loc_assign', 'translation_id', 'sueb_translation'));

-- Adds foreign_key constraints for location
  -- country
    SELECT(clean_up_relation('sueb_location', 'country_id', 'sueb_country'));

-- Adds foreign_key constraints for manual_keys
  -- original_fk
    SELECT(clean_up_relation('sueb_manual_keys', 'original_id', 'sueb_original'));
  -- original_fk
    SELECT(clean_up_relation('sueb_manual_keys', 'translation_id', 'sueb_translation'));


-- Adds foreign_key constraints for orig_assign
  -- orig_fk
    SELECT(clean_up_relation('sueb_orig_assign', 'original_id', 'sueb_original'));
  -- trans_fk
    SELECT(clean_up_relation('sueb_orig_assign', 'translation_id', 'sueb_translation'));



-- Adds foreign_key constraints for original

  -- ddc_fk
    SELECT(clean_up_relation('sueb_original', 'ddc_id', 'sueb_ddc_german'));

  -- author_fk
    SELECT(clean_up_relation('sueb_original', 'author_id', 'sueb_author'));

  -- collection_fk
    SELECT(clean_up_relation('sueb_original', 'collection_id', 'sueb_collection'));

  --language_fk
    SELECT(clean_up_relation('sueb_original', 'language_id', 'sueb_language'));


-- Adds foreign_key constraints for pnd_alias
  --pnd_main_fk
    --SELECT(clean_up_relation('pnd_alias', 'pnd_id', 'pnd_main'));
    ALTER TABLE sueb_pnd_alias
    ADD CONSTRAINT sueb_pnd_main_fk
      FOREIGN KEY(pnd_id)
        REFERENCES sueb_pnd_main(id);

-- Adds foreign_key constraints for pnd_main

-- Adds foreign_key constraints for pnd_term
  --pnd_main_fk
    --SELECT(clean_up_relation('pnd_term', 'pnd_id', 'pnd_main'));
    ALTER TABLE sueb_pnd_title
    ADD CONSTRAINT sueb_pnd_main_fk
      FOREIGN KEY(pnd_id)
        REFERENCES sueb_pnd_main(id);


-- Adds foreign_key constraints for swd_main
-- Adds foreign_key constraints for swd_term
  --swd_main_fk
    --SELECT(clean_up_relation('swd_term', 'swd_id', 'swd_main'));
    ALTER TABLE sueb_swd_term
    ADD CONSTRAINT sueb_swd_main_fk
      FOREIGN KEY(swd_id)
        REFERENCES sueb_swd_main(id);


-- Adds foreign_key constraints for translation
  -- ddc_fk
    SELECT(clean_up_relation('sueb_translation', 'ddc_id', 'sueb_ddc_german'));

  -- ddc_fk
    SELECT(clean_up_relation('sueb_translation', 'translator_id', 'sueb_translator'));

  --author_fk
    SELECT(clean_up_relation('sueb_translation', 'author_id', 'sueb_author'));

  --collection_fk
    SELECT(clean_up_relation('sueb_translation', 'collection_id', 'sueb_collection'));

  --language_fk
    SELECT(clean_up_relation('sueb_translation', 'language_id', 'sueb_language'));

  --via_language_fk
    SELECT(clean_up_relation('sueb_translation', 'via_language_id', 'sueb_language'));

DROP SEQUENCE IF EXISTS  author_auth_id_seq;
DROP SEQUENCE IF EXISTS  loc_assign_loc_assign_id_seq;
DROP SEQUENCE IF EXISTS  location_loc_id_seq;
DROP SEQUENCE IF EXISTS  manual_keys_mankey_id_seq;
DROP SEQUENCE IF EXISTS  orig_assign_orig_assign_id_seq;
DROP SEQUENCE IF EXISTS  translator_translator_id_seq;
