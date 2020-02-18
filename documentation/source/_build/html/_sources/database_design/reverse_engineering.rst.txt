Reverse Engineering the database structure
==========================================

Move the database schema from mariadb to postgresql and django models.

**Steps:**

1. Archive original dump
2. Move data to postgresql
3. Archive postgresql dump and structure
4. Create Django Models from old database structure -> automatic
5. Graph models
6. Compare the different versions of database schemas (_new-suffix) and the
   stored data
7. Document understanding of models and questions.
8. Insert Foreign Key constraints
9. Graph models




Designing the new database structure
====================================

Understand functional dependencies

