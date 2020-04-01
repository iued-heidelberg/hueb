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

echo "Loading di_sueb into Postgres"
echo " "
echo "  Dropping dump_di_sueb"
psql -c "DROP DATABASE IF EXISTS hueb_db_archive;"
echo "  Creating dump_di_sueb"
createdb hueb_db_archive
echo "  Loading mysql into postgres"
pgloader mysql://root:${rootpasswd}@localhost/di_sueb postgresql:///hueb_db_archive
pgloader mysql://root:${rootpasswd}@localhost/di_sueb_lidos postgresql:///hueb_db_archive
pgloader mysql://root:${rootpasswd}@localhost/di_sueb_latein postgresql:///hueb_db_archive


