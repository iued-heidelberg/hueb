#!/bin/bash
cd /hueb/src
export DJANGO_SETTINGS_MODULE=hueb.settings
export DATA_DIR=/data/
export HOME=/hueb
export NUM_WORKERS=$((2 * $(nproc --all)))


if [ ! -d /data/logs ]; then
    echo "Creating log directory at /data/logs"
    mkdir /data/logs;
fi
if [ ! -d /data/media ]; then
    echo "Creating media directory at /data/media"
    mkdir /data/media;
fi
echo "Collecting static files"
python3 -m manage collectstatic --noinput
echo "Migrating Database"
python3 -m manage migrate --noinput

echo "Starting gunicorn"
exec gunicorn hueb.wsgi \
    --name hueb \
    --workers $NUM_WORKERS \
    --max-requests 1200 \
    --max-requests-jitter 50 \
    --log-level=info \
    --bind=0.0.0.0:8000

exit 1
