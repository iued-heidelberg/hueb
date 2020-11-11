FROM python:3.8

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  default-libmysqlclient-dev \
  gettext \
  git \
  libffi-dev \
  libjpeg-dev \
  libmemcached-dev \
  libpq-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  locales \
  nginx \
  python-dev \
  python-virtualenv \
  python3-dev \
  sudo \
  supervisor \
  zlib1g-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  dpkg-reconfigure locales && \
  locale-gen C.UTF-8 && \
  /usr/sbin/update-locale LANG=C.UTF-8 && \
  mkdir /etc/hueb && \
  mkdir /data && \
  useradd -ms /bin/bash -d /hueb -u 15371 hueb_user && \
  echo 'hueb_user ALL=(ALL) NOPASSWD:SETENV: /usr/bin/supervisord' >> /etc/sudoers && \
  mkdir /static && \
  mkdir /etc/supervisord

COPY src/requirements.txt /hueb/src/requirements.txt

RUN pip3 install -U \
  pip \
  setuptools \
  wheel && \
  cd /hueb/src/ && \
  pip3 install \
  -r requirements.txt && \
  rm -rf ~/.cache/pip

COPY deployment/docker/hueb.bash /usr/local/bin/hueb
COPY deployment/docker/supervisord.conf /etc/supervisord.conf
COPY deployment/docker/nginx.conf /etc/nginx/nginx.conf

COPY src /hueb/src

RUN chmod +x /usr/local/bin/hueb && \
  rm /etc/nginx/sites-enabled/default && \
  cd /hueb/src && \
  mkdir -p data && \
  chown -R hueb_user:hueb_user /hueb /data data

USER hueb_user
VOLUME ["/etc/hueb", "/data"]
EXPOSE 80
ENTRYPOINT ["hueb"]
CMD ["all"]
