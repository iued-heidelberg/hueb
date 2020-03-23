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

echo "Loading di_sueb_latein into Postgres"
echo " "
echo "  Dropping dump_di_sueb_latein"
psql -c "DROP DATABASE IF EXISTS dump_di_sueb_latein;"
echo "  Creating dump_di_sueb_latein"
createdb dump_di_sueb_latein
echo "  Loading mysql into postgres"
pgloader mysql://root:${rootpasswd}@localhost/di_sueb_latein postgresql:///dump_di_sueb_latein



echo "Loading di_sueb_lidos"
echo " "
echo "  Dropping di_sueb_lidos"
mysql -u root -p${rootpasswd} -e "DROP DATABASE IF EXISTS di_sueb_lidos;"
echo "  Creating di_sueb_lidos"
mysql -u root -p${rootpasswd} -e "CREATE DATABASE di_sueb_lidos;"
echo "  Loading dump for di_sueb_lidos"
mysql -u root -p${rootpasswd}  di_sueb_lidos < archive/original_dumps/di_sueb_lidos.dump
echo " "

echo "Loading di_sueb_lidos into Postgres"
echo " "
echo "  Dropping dump_di_sueb_lidos"
psql -c "DROP DATABASE IF EXISTS dump_di_sueb_lidos;"
echo "  Creating dump_di_sueb_lidos"
createdb dump_di_sueb_lidos
echo "  Loading mysql into postgres"
pgloader mysql://root:${rootpasswd}@localhost/di_sueb_lidos postgresql:///dump_di_sueb_lidos



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
psql -c "DROP DATABASE IF EXISTS dump_di_sueb;"
echo "  Creating dump_di_sueb"
createdb dump_di_sueb
echo "  Loading mysql into postgres"
pgloader mysql://root:${rootpasswd}@localhost/di_sueb postgresql:///dump_di_sueb


echo "Create working copies of databases"
echo "  Creating di_sueb_latein"
psql -c "DROP DATABASE IF EXISTS di_sueb_latein;"
psql -c "CREATE DATABASE di_sueb_latein with TEMPLATE dump_di_sueb_latein;"
echo "  Creating di_sueb_lidos"
psql -c "DROP DATABASE IF EXISTS di_sueb_lidos;"
psql -c "CREATE DATABASE di_sueb_lidos with TEMPLATE dump_di_sueb_lidos;"
echo "  Creating di_sueb"
psql -c "DROP DATABASE IF EXISTS di_sueb;"
psql -c "CREATE DATABASE di_sueb with TEMPLATE dump_di_sueb;"
