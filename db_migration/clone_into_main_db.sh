#!/bin/bash
set -e
#psql -c "DROP DATABASE IF EXISTS hueb;"
#psql -c "CREATE DATABASE hueb with TEMPLATE hueb_db;"

psql -d hueb_db -a -f sql_scripts/di_sueb_latein/10_rename_and_move_latein.sql
psql -d hueb_db -a -f sql_scripts/di_sueb/10_rename_and_move_latein.sql