# HUEB - Heidelberger Übersetzungs Bibliographie

> Im Rahmen der Digital Humanities wird die DFG-geförderte Heidelberger Übersetzungsbibliographie eine Informationsinfrastruktur bereitstellen, die zwei Zwecken dienen soll:
>
> Zunächst geht es um die Zusammenstellung einer Bibliographie von vorwiegend frühneuzeitlichen Übersetzungen aus dem Englischen und Niederländischen ins Deutsche (Erscheinungszeitraum 1450–1850).
>
> Diese soll dann gemeinsam mit zwei Vorgängerprojekten zur romanisch-deutschen und lateinisch-deutschen Übersetzung (Saarbrücker Übersetzungsbibliographie) zu einer Gesamtbibliographie integriert werden, um anderen Forschenden umfassende bibliographische Daten zur Übersetzung ins Deutsche in der frühen Neuzeit und darüber hinaus verfügbar zu machen.
>
> Durch die Zusammenführung der dann insgesamt drei Datenbanken (englisch/niederländisch-deutsche HÜB, lateinisch-deutsche SÜB-L, romanisch-deutsche SÜB) wird eine umfassende Übersetzungsbibliographie frühneuzeitlicher nichtfiktionaler Texte mit Lateinisch, Französisch, Italienisch, Spanisch, Portugiesisch, Englisch und Niederländisch als systematisch erfassten Original- und Brückensprachen entstehen, die Forschenden eine umfassende Datenbasis für Untersuchungen verschiedenster Ausrichtung liefern kann. Darüber hinaus soll die entwickelte Infrastruktur zugleich interessierten Kolleginnen und Kollegen für die Erfassung eigener bibliographischer Daten zur Verfügung gestellt werden.

This is the application that should one day achieve these goals. It is built upon [Django](www.djangoproject.com), its administration tooling and [PostgreSQL](postgresql.org). The frontend is build with [TailwindCSS](tailwindcss.com) and [Alpine.js](https://alpinejs.dev/).

The current implementation progress (07.21) is the following:
- a new normalized database schema is implemented
- an administration interface is implemented that is used to add and manage  entries, including a rudimentary review functionality and versioning of all entries
- all old databases are ported from ancient MySQL dumps to PostgreSQL, cleaned up, and made read-only accessible in the backend. Currently, they are kept in separate tables and not merged into the main data model because they aren't reviewed yet
- a public landing site and basic search functionality is implemented

![alt text](https://github.com/iued-heidelberg/hueb/raw/development/.img/index.png "Screenshot of the landing page, mainly containing the German text from above.")

![alt text](https://github.com/iued-heidelberg/hueb/raw/development/.img/search.png "Screenshot of the search view with two example documents.")


**For my successors:**

> Hey you 👋
> Thank you for continuing this project. I had a lot of fun working on it and learned a lot.
> I've handed over a set of files to the team for you to start off:
> - an ssh key set. This set has access to both servers. Use it to log in, add your own keys (newly created or your regular keys) to both servers, verify! that the new keys work, and then remove my old keys and the keys I've created for you from the server. These are now yours
> - `development_secrets.ini` and `staging_secrets.ini` their usage is described further down
> - `backup.sql` this is a backup I've created during the last weeks of my involvement. You can use it to seed your local dev environment or simply download a backup from the servers
> - I've added a list of possible todos/open topics at the end of this document
> Have fun,
> Lukas
> PS: Please apologize for the bodies you may find in this project...


### Setting up a development environment
1. Install [python3.8](python.org), [PostgreSQL](https://www.postgresql.org/) and [nodejs](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) on your local maschine.
2. Clone the repository
```
git clone git@github.com:iued-heidelberg/hueb.git
```
3. Change into the project folder `cd hueb`
4. Create a virtual environment and activate it
```
python3 -m venv venv
source venv/bin/activate
```
You have to activate this environment again whenever you want to start working on it.
5. Install all requirements (pre-commit will check that your commits adhere to the style guide before committing them.
```
pip3 install -r requirements.txt
pre-commit install
```
6. Template a new `.env` file:
```
cd src/hueb
cp .env.template .env
```
7. [Create a new local database user and database](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)
8. Add these credentials to .env
9. Change into `apps/hueb20` and install npm dependencies
```
cd app/hueb20
npm install
cd ../..
```
9. Execute database migrations
```
./manage.py migrate
```
10. Run the application
```
./manage.py runserver
```

Now you have a running Django application locally and can start developing.

### Structure of the application
The repository is split into three main sections:
- db_migration
- deployment
- src

**db_migration** contains the original Mysql dumps, a dump of the databases after importing them into Postgres, a dump of the cleaned-up data, and scripts to turn the raw Postgres dump into the later one. This is the place to look for  if there should be inconsistencies in the imported data for the three older datasets

**deployment** nearly everything is associated with the deployment of the application. The only exception being the `.github` directory with the CI/CD jobs and the Dockerfile for the main application. Both placed in the root of the project
The usage and function are described further down in this document.

**src** contains the code of the application. It is structured like a common Django application. It contains four apps. The three `hueb_legacy*` apps contain the administration interface for the older datasets. They are minimal, and you probably don't want to add too much functionality to them.
`hueb20` instead is the home of the new data structure, its administration, and frontend. The contained `data_migrations` folder is left as a reference for how you could implement a migration of the data from the old apps to the new one. They aren't used and are probably out of date.

### Adding new environment variables
Adding new environment variables for configuration is currently a bit of Rube-Goldberg-Maschine that could use improvement.
Assuming you want to add a boolean configuration variable, you have to make the following changes.

**For development:**
- add it to `/hueb/src/hueb/.env`. This is your local configuration file, used when you are starting the app on your machine. This file is deliberately added to `.gitignore` to prevent leakage of secrets by committing them to the repository.
- add it to `/hueb/src/hueb/.env.template`. So that the next person knows what variables must be set.
- add code that parses this environment variable to `/hueb/src/hueb/settings.py`. Look at the already implemented examples for reference. Be careful while adding a boolean flag. Pythons casting of the environment variable content is unintuitive at best.

**For CI/CD:**
- add it to `hueb/deployment/ansible/roles/docker/templates/env.j2`. This is a template file used by [this role](hueb/deployment/ansible/roles/docker/tasks/main.yml) to write the .env file to the server.
- add new [github secrets](https://github.com/iued-heidelberg/hueb/settings/secrets/actions) with the value for staging and production
- add the Github secrets to the `extraVars`-portion in the deployment steps of `.github/workflows/development_workflow.yml` and `.github/workflows/release_workflow.yml`. These are passed to Ansible to fill in the `env.j2` file.

**For manual deployment:**
- add them to the `production_secrets.ini` and `staging_secrets.ini` file found under `hueb/deployment/ansible/inventory/`

## Getting code into staging/production
Deployments are fully automated and are executed via Github Actions, Ansible, Docker, and Docker-Compose. Secrets are stored in the Github secret store.

**Important Note:** This project supports [sentry] and [honeycomb] as monitoring and observability solutions. I have replaced the API credentials with an empty string as the accounts ran under my name. You can add them back by registering accounts for these services and updating the Github Secrets with the tokens.

### Environments
Currently we have two different servers hosted in the [heiCLOUD](https://heicloud.uni-heidelberg.de):
- [hueb-staging.iued.uni-heidelberg.de](hueb-staging.iued.uni-heidelberg.de)
- [hueb.iued.uni-heidelberg.de](hueb.iued.uni-heidelberg.de)

On both servers, the backups are located on `/db_dump/backup/*` and the repository in `/hueb. Later one is only used to have all deployment scripts and configuration file (`/hueb/deployment/docker.env`) locally.

### Components
The applications consist out of three services, listed in the [docker_compose.yml](deployment/docker/docker-compose.yml):
- `hueb` - the Django application running everything
- `proxy` - the Nginx proxy handling SSL and proxying to `hueb`
- `database` - a Postgres database supporting everything with the cronjobs responsible for backing up the data

### Continuous Integration & Deployment
Commits pushed to Github will cause the `.github/workflows/development_workflows.yml` to run. This workflow runs [black](black.readthedocs.io), [flake8](flake8.pycqa.org), tests, the application- and database container build in parallel. The container images are pushed to [Githubs container registry](ghcr.io) under the tags TODO

The staging CI Process is normally aborted at this point. The exception is a commit published on the `development branch. It is deployed via Ansible directly to [hueb-staging.iued.uni-heidelberg.de](hueb-staging.iued.uni-heidelberg.de).

A deployment to [hueb.iued.uni-heidelberg.de](hueb.iued.uni-heidelberg.de) is triggered by pushing a tag with the structure `v*.*.*` and runs the same steps as for staging. It uses the tags: TODO for its docker images and adds two steps to publish release notifications to [Sentry](sentry.com) and [Honeycomb](honeycomb.io).

### Manual Deployment
The application can be deployed from your host computer via Ansible (`pip3 install ansible`).
Before the first execution, additional dependencies for Ansible must be installed. Change directory to `hueb/deployment/ansible` and execute the commands:
```
ansible-galaxy role install -r requirements.yml
ansible-galaxy collection install -r requirements.yml
```

You need a fully configured `production_secrets.ini` or `staging_secrets.ini` (depending on infrastructure) file placed in `hueb/deployment/ansible/inventory/`.
Pay additional attention to the `tag` variable. This should contain either a `git sha` or a `git tag`. This value is used to pull the correct docker image from the registry.

Change your working directory to `hueb/deployment/ansible` enter the following command to deploy to production:
```
ansible-playbook -i inventory/production.ini -e @inventory/production_secrets.ini  provision.yml
```
This executes the steps outlined in the `provision.yml` playbook against the host described in `inventory/production.ini` while supplying variables from `inventory/production_secrets.ini` (the @ is necessary there).
Exchanging `production` with `staging` affects the other environment.

The available playbooks are:
- `provision.yml` updates the server to run the configured version of the application. An empty server can be provisioned by temporarily removing the `create_backup` role.
- `restore_backup.yml` creates a backup of the database, drops the current database, and restores from another backup file. The name of which is asked during execution.
- `backup.yml` creates an additional backup of the database at this point in time.



## Todos:
Where could you start? Where is more work to do?

1. Fortify the review system. It is currently implemented without much complexity. Every document starts of as unreviewed, and only persons with the review permissions are allowed to change this. This property is not reset if changes are made to the document manually. This is tolerable because we are currently working in an append-only mode where a group of colleagues is adding documents and others are reviewing them. Later changes are not common. This should be changed. You can search for unreviewed changes by checking if a new document revision has been added to the document by a non-reviewer after it has been originally reviewed.
2. Migrate the old datasets to the new data model. The data is in Postgres and Django models exist. The migration should be relatively straightforward. You can use `hueb/src/apps/hueb20/data_migrations` as a reference. The bigger challenge is keeping the data sources distinguishable and making sure the data is correct. I suggest continuing marking all data with their source using the `HUEB_APPLICATIONS` enum provided in [utils.py](hueb/src/hueb/apps/hueb20/models/utils.py). Correctness will be especially challenging for the `hueb_legacy_latein` dataset because it contained tables named `*_new`, which added multiple m:m-tables. I suspect that the models with two `New` like `OriginalNewAuthorNew` are the most promising ones, which is the reason why they are displayed in the admin UI. But some kind of review is probably necessary.
3. Make a better search interface. The current one was created without real feedback or user interaction and more as a proof of concept. The implementation with Q-objects is probably fine for a start.
4. Make a better backend. The backend is pretty barebones. It uses autocompletion and whatnot but could benefit a lot from some kind of guidance/workflow for our users. For example: add a view to see which documents you've added yourself, what changes have you made last, create a nicer list view which isn't so wide, ...


