SET search_path to di_sueb_latein;

-- dropping keyword-tables because they are empty
drop table if exists manual_keys;
drop table if exists official_keys;
drop table if exists additional_keys;
drop table if exists sim_term;
drop table if exists swd_main;
drop table if exists swd_term;

-- dropping person-name-database-tables because they are empty
drop table if exists pnd_alias;
drop table if exists pnd_main;
drop table if exists pnd_title;

-- dropping old information
drop table if exists old_table;

-- dropping project specifica
drop table if exists projektbeschreibung;

-- dropping pseudonym table which is empty
drop table if exists pseudo;

-- dropping empty collection table
drop table if exists collection;

