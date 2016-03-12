-- run in order to initialize database
-- WARNING: will delete current database

DROP TABLE IF EXISTS Messages;
CREATE TABLE Messages(
    mid integer PRIMARY KEY AUTOINCREMENT,
    sysplat varchar(60),
    sysver varchar(6),
    msg varchar(120)
);