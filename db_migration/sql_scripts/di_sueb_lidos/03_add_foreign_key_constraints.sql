\set ON_ERROR_STOP true
SET search_path to di_sueb_lidos;



SELECT(clean_up_relation('sueb_lidos_manual_keys', 'original_id', 'sueb_lidos_original'));

SELECT(clean_up_relation('sueb_lidos_manual_keys', 'translation_id', 'sueb_lidos_translation'));



SELECT(clean_up_relation('sueb_lidos_orig_assign', 'original_id', 'sueb_lidos_original'));

SELECT(clean_up_relation('sueb_lidos_orig_assign', 'translation_id', 'sueb_lidos_translation'));


SELECT(clean_up_relation('sueb_lidos_original', 'ddc_id', 'sueb_lidos_ddc_german'));

SELECT(clean_up_relation('sueb_lidos_original', 'author_id', 'sueb_lidos_author'));

SELECT(clean_up_relation('sueb_lidos_original', 'language_id', 'sueb_lidos_language'));

SELECT(clean_up_relation('sueb_lidos_original', 'manual_keys_id', 'sueb_lidos_manual_keys'));



SELECT(clean_up_relation('sueb_lidos_translation', 'ddc_id', 'sueb_lidos_ddc_german'));

SELECT(clean_up_relation('sueb_lidos_translation', 'author_id', 'sueb_lidos_author'));

SELECT(clean_up_relation('sueb_lidos_translation', 'translator_id', 'sueb_lidos_translator'));

SELECT(clean_up_relation('sueb_lidos_translation', 'language_id', 'sueb_lidos_language'));

SELECT(clean_up_relation('sueb_lidos_translation', 'via_language_id', 'sueb_lidos_language'));


