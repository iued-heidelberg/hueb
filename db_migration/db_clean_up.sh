#!/bin/bash
set -e
echo "Create working copies of databases"
echo "  Creating hueb_db"
psql -c "SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = 'hueb_db'
          AND pid <> pg_backend_pid();"
psql -c "SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = 'hueb_db_archive'
          AND pid <> pg_backend_pid();"
psql -c "DROP DATABASE IF EXISTS hueb_db;"
psql -c "CREATE DATABASE hueb_db with TEMPLATE hueb_db_archive;"

psql -d hueb_db -a -f sql_scripts/di_sueb_latein/00_setup_postgres.sql
psql -d hueb_db -a -f sql_scripts/di_sueb_latein/01_table_cleanup.sql
psql -d hueb_db -a -f sql_scripts/di_sueb_latein/02_add_migration_notes.sql
psql -d hueb_db -a -f sql_scripts/di_sueb_latein/02_create_n_m_tables.sql
psql -d hueb_db -a -f sql_scripts/di_sueb_latein/03_add_foreign_key_constraints.sql

psql -d hueb_db -a -f sql_scripts/di_sueb/00_setup_postgres.sql
psql -d hueb_db -a -f sql_scripts/di_sueb/01_table_cleanup.sql
psql -d hueb_db -a -f sql_scripts/di_sueb/02_add_migration_notes.sql
psql -d hueb_db -a -f sql_scripts/di_sueb/03_add_foreign_key_constraints.sql