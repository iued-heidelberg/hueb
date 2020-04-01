############################
Legacy Application Migration
############################

We have 3 database dumps from previous projects, which shall be incorporated to the new bibliography.

- ``di_sueb_latein.dump`` - currently implemented
- ``di_sueb_lidos.dump``
- ``di_sueb.dump``

The knowledge about the content of these databases is in is limited.
These database dumps were created from an old MySQL-instance and only contain primary-key constraints. Therefore completness and correctness cannot be guaranteed.
This is complicated by the lack of discipline in naming and deleting old tables. Many tables in these dumps have a sister table with the name-suffix ``_new``.

These datasets must be made accessible for the team to search through and inspect to identify and correct errors and missing information.

We will use Django and PostgreSQL for this job to be compatible to the new application and prevent duplicated work.

******************
Database migration
******************

Currently all steps to migrate ``di_sueb_latein.dump`` are implemented in the ``bash``- and ``.sql``-scripts contained in the ``db_migration`` folder.
The other two databases must be implemented when we have migrated the first one completely.

Prerequisites
=============

1. Install ``PostgreSQL`` and ``MySQL``
2. Install ``pgloader``. Guides can be found on the projects
   `Github page <https://github.com/dimitri/pgloader>`_
3. Clone this repository

Migrating the database
======================

1. Change into the ``db_migration``-directory of this repository.
2. Make the three scripts executable:

   .. code-block:: bash
      :linenos:

      chmod +x load_dumps.sh
      chmod +x create_working_copy.sh
      chmod +x db_clean_up.sh

3. Execute these scripts in order:

   .. code-block:: bash
      :linenos:

      # loads dumps into MySQL and PostgreSQL
      # relatively slow
      ./load_dumps.sh

      # creates a working copy which can be cleaned up
      # this means that you have only to execute this script again
      # to reset the working copy
      ./create_working_copy.sh

      # cleans up the working copy
      ./db_clean_up.sh

   Observe the individual output of the scripts, they will abort on an error.
   All steps are idempotent and can be executed repeatedly until all scripts finish successfully.


Process steps
=============

1. Import MySQL dumps into MySQL and move databases into PostgreSQL
2. Duplicate databases in PostgreSQL to create working copies
3. Clean up databases. Deleting unused tables and columns,
   renaming tables and columns to be more clear and readable.
4. Adding migration notes to each table, allowing the user to identify
   database entries which will be created during the migration.
5. Add foreign-key constraints to the tables, creating the database entries,
   which are missing to statisfy the constraints, on the go.

These steps are scripted to make all actions replayable to prevent cumbersome, slow and errorprone manual execution of the steps.
This way a mistake can be fixed by fixing scripts and running them.

