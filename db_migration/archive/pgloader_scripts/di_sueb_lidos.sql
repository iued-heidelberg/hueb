LOAD DATABASE
     FROM      mysql://root:{{PASSWORD}}@127.0.0.1:3306/di_sueb_lidos
     INTO postgresql:///hueb_db_archive

CAST type int when unsigned drop typemod,
     type int with extra auto_increment drop typemod;
