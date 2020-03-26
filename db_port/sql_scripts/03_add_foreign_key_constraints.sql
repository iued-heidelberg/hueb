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
