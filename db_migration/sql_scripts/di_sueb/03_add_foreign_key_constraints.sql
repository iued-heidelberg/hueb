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
    SELECT(clean_up_relation('loc_assign', 'location_id', 'location'));

  -- original_fk
    SELECT(clean_up_relation('loc_assign', 'original_id', 'original'));

  -- translation_fk
    SELECT(clean_up_relation('loc_assign', 'translation_id', 'translation'));

-- Adds foreign_key constraints for location
  -- country
    SELECT(clean_up_relation('location', 'country_id', 'country'));

-- Adds foreign_key constraints for manual_keys
  -- original_fk
    SELECT(clean_up_relation('manual_keys', 'original_id', 'original'));
  -- original_fk
    SELECT(clean_up_relation('manual_keys', 'translation_id', 'translation'));


-- Adds foreign_key constraints for orig_assign
  -- orig_fk
    SELECT(clean_up_relation('orig_assign', 'original_id', 'original'));
  -- trans_fk
    SELECT(clean_up_relation('orig_assign', 'translation_id', 'translation'));



-- Adds foreign_key constraints for original

  -- ddc_fk
    SELECT(clean_up_relation('original', 'ddc_id', 'ddc_german'));

  -- author_fk
    SELECT(clean_up_relation('original', 'author_id', 'author'));

  -- collection_fk
    SELECT(clean_up_relation('original', 'collection_id', 'collection'));

  --language_fk
    SELECT(clean_up_relation('original', 'language_id', 'language'));


-- Adds foreign_key constraints for pnd_alias
  --pnd_main_fk
    --SELECT(clean_up_relation('pnd_alias', 'pnd_id', 'pnd_main'));
    ALTER TABLE pnd_alias
    ADD CONSTRAINT pnd_main_fk
      FOREIGN KEY(pnd_id)
        REFERENCES pnd_main(id);

-- Adds foreign_key constraints for pnd_main

-- Adds foreign_key constraints for pnd_term
  --pnd_main_fk
    --SELECT(clean_up_relation('pnd_term', 'pnd_id', 'pnd_main'));
    ALTER TABLE pnd_title
    ADD CONSTRAINT pnd_main_fk
      FOREIGN KEY(pnd_id)
        REFERENCES pnd_main(id);


-- Adds foreign_key constraints for swd_main
-- Adds foreign_key constraints for swd_term
  --swd_main_fk
    --SELECT(clean_up_relation('swd_term', 'swd_id', 'swd_main'));
    ALTER TABLE swd_term
    ADD CONSTRAINT swd_main_fk
      FOREIGN KEY(swd_id)
        REFERENCES swd_main(id);


-- Adds foreign_key constraints for translation
  -- ddc_fk
    SELECT(clean_up_relation('translation', 'ddc_id', 'ddc_german'));

  -- ddc_fk
    SELECT(clean_up_relation('translation', 'translator_id', 'translator'));

  --author_fk
    SELECT(clean_up_relation('translation', 'author_id', 'author'));

  --collection_fk
    SELECT(clean_up_relation('translation', 'collection_id', 'collection'));

  --language_fk
    SELECT(clean_up_relation('translation', 'language_id', 'language'));

  --via_language_fk
    SELECT(clean_up_relation('translation', 'via_language_id', 'language'));