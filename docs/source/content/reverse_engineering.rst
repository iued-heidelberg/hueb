Reverse Engineering the database structure
==========================================

Move the database schema from mariadb to postgresql and django models.

Thoughts after first inspection:
--------------------------------
1. the relations original and translation are mostly identical
   -> they could be unified into one text-relation containing both
   originals and translations
2. the via-attribute of the language-translation relationship doesn't capture
   the texts which were used to translate the intermediate steps
3. the additional_key and manual_key relations aren't used anymore
4. the pnd_* relations aren't relevant. The information could be used in the
   migration to use the gnd-archive for author identification
5. the swd_* relations aren't used
6. sim_term, test_author, test_book and official_keys aren't used


Steps to clean up database:
---------------------------

1. Archive original dump
2. Move data to postgresql, archive postgresql database
3. Drop unused relations and rename the rest to signal that they are intended
   for readonly use, archive script to drop relationspostgresql database
4. Add foreign-key relationships, archive script to add foreign-key
   relationships and postgresql database
5. Create models by using djangos default tools, graph models




