#!/bin/bash
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
