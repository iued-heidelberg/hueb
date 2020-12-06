#!/bin/sh
set -e
file_name=postgres_dump

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo "Current Time : $current_time"

new_fileName=$1/$file_name.$current_time.gz
echo "New FileName: " "$new_fileName"

touch $new_fileName

echo "Dumping: " "$POSTGRES_DB"

pg_dump hueb | gzip > $new_fileName