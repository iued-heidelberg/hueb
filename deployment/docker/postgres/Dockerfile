FROM postgres:13
RUN apt-get -y update && \
  apt-get install -y supervisor cron && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN mkdir /etc/supervisor.d
RUN mkdir /backup

COPY pg_backup.sh /pg_backup.sh
RUN chmod a+x /pg_backup.sh
COPY pg_backup.sh /delete_old_backups.sh
RUN chmod a+x /pg_backup.sh

COPY cronjob /etc/cron.d/backup_job
RUN chmod 0644 /etc/cron.d/backup_job
RUN crontab /etc/cron.d/backup_job

COPY postgres_cron.ini /etc/supervisord.conf

ENTRYPOINT printenv | sed 's/^\(.*\)$/export \1/g' > /project_env.sh && \
  /usr/bin/supervisord -c /etc/supervisord.conf