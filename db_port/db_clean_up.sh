
psql -d hueb_db -a -f sql_scripts/00_setup_postgres.sql
psql -d hueb_db -a -f sql_scripts/01_table_cleanup.sql
psql -d hueb_db -a -f sql_scripts/02_add_migration_notes.sql
psql -d hueb_db -a -f sql_scripts/03_add_foreign_key_constraints.sql