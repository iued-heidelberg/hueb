FROM python:3.8

RUN \
  echo "deb https://deb.nodesource.com/node_12.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  default-libmysqlclient-dev \
  gettext \
  git \
  nodejs \
  libpq-dev \
  libxml2-dev \
  libxslt1-dev \
  locales \
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

COPY deployment/docker/hueb/hueb.bash /usr/local/bin/hueb
COPY deployment/docker/hueb/supervisord.conf /etc/supervisord.conf

COPY src /hueb/src

RUN cd /hueb/src/hueb/apps/hueb20 && \
  npm run-script build_prod

RUN chmod +x /usr/local/bin/hueb && \
  cd /hueb/src && \
  mkdir -p data && \
  chown -R hueb_user:hueb_user /hueb /data data

ARG git_sha
ENV GIT_SHA=${git_sha}
LABEL git_sha=${git_sha}
ARG version
ENV VERSION=${version}
LABEL VERSION=${version}

HEALTHCHECK --interval=5s --start-period=10s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1

USER hueb_user
VOLUME ["/etc/hueb", "/data"]
EXPOSE 8000
ENTRYPOINT ["hueb"]
CMD ["all"]
