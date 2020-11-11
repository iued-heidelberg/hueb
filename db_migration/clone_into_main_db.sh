set -e
psql -c "DROP DATABASE IF EXISTS hueb;"
psql -c "CREATE DATABASE hueb with TEMPLATE hueb_db;"

psql -d hueb -a -f sql_scripts/10_rename_and_move_latein.sql