#!/bin/bash
psql -d hueb_db -c "DROP SCHEMA IF EXISTS public;"
psql -d hueb_db -c "DROP SCHEMA IF EXISTS di_sueb_latein CASCADE;"

pg_dump --clean -O hueb_db > cleaned_data.sql

psql hueb < cleaned_data.sql