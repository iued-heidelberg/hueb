#!/bin/bash
echo "Please enter root user MySQL password!"
echo "Note: password will be hidden when typing"
read -s rootpasswd

echo " "
echo "Loading di_sueb_latein"
echo " "
echo "  Dropping di_sueb_latein"
mysql -u root -p${rootpasswd} -e "DROP DATABASE IF EXISTS di_sueb_latein;"
echo "  Creating di_sueb_latein"
mysql -u root -p${rootpasswd} -e "CREATE DATABASE di_sueb_latein;"
echo "  Loading dump for di_sueb_latein"
mysql -u root -p${rootpasswd} di_sueb_latein < archive/original_dumps/di_sueb_latein.dump
echo " "

echo "Loading di_sueb_lidos"
echo " "
echo "  Dropping di_sueb_lidos"
mysql -u root -p${rootpasswd} -e "DROP DATABASE IF EXISTS di_sueb_lidos;"
echo "  Creating di_sueb_lidos"
mysql -u root -p${rootpasswd} -e "CREATE DATABASE di_sueb_lidos;"
echo "  Loading dump for di_sueb_lidos"
mysql -u root -p${rootpasswd}  di_sueb_lidos < archive/original_dumps/di_sueb_lidos.dump
echo " "

echo "Loading di_sueb"
echo " "
echo "  Dropping di_sueb"
mysql -u root -p${rootpasswd} -e "DROP DATABASE IF EXISTS di_sueb;"
echo "  Creating di_sueb"
mysql -u root -p${rootpasswd} -e "CREATE DATABASE di_sueb;"
echo "  Loading dump for di_sueb"
mysql -u root -p${rootpasswd} di_sueb < archive/original_dumps/di_sueb.dump
echo " "

echo "Loading all into Postgres"
echo " "
echo "  Dropping dump_di_sueb"
psql -c "DROP DATABASE IF EXISTS hueb_db_archive;"
echo "  Creating dump_di_sueb"
createdb hueb_db_archive
echo "  Loading mysql into postgres"
export PASSWORD=${rootpasswd}
pgloader ./archive/pgloader_scripts/di_sueb.sql
pgloader ./archive/pgloader_scripts/di_sueb_lidos.sql
pgloader ./archive/pgloader_scripts/di_sueb_latein.sql
