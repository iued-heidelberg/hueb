#!/bin/sh
file_name=postgres_dump

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo "Current Time : $current_time"

new_fileName=/backup/$file_name.$current_time.gz
echo "New FileName: " "$new_fileName"

touch $new_fileName

echo "Dumping: " "$POSTGRES_DB"

pg_dump -h $1 -U $POSTGRES_USER $POSTGRES_DB | gzip > $new_fileName