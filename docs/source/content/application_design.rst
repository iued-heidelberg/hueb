Designing the new database structure
====================================

Content of the data model:
--------------------------

- Maintain content of data models
- Atayan and team will provide "light" additions to the data models


Extensions to the application:
------------------------------

- Quality assurance is important. Newly created entries must be revied before
   commiting them to the bibliography. Entries from the old database must be
   rechecked to maintain the quality -> django-fsm allows to create a
   state machine for a model f.e. imported -> checked -> released
- Changes between the different versions of a database entrie should (probably)
   be tracked as well to maintain traceability
- Regularly check if links are still alive. Alert if it isn't the case
- Export of search results. Maybe CSV, if possible a shiny pdf?
- Fuzzy search to prevent entering two datasets for the same e.g. author.
   Just because the name is written slightly different.
- Integration of GND identifiers as an option to identify authors and the
   different spellings of their name
