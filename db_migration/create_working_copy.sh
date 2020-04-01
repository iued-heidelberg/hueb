echo "Create working copies of databases"
echo "  Creating hueb_db"
psql -c "DROP DATABASE IF EXISTS hueb_db;"
psql -c "CREATE DATABASE hueb_db with TEMPLATE hueb_db_archive;"