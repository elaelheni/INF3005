# coding: utf8

import sqlite3

connection = sqlite3.connect('musique.db')

name = "', 0, 0); drop table artiste; --"
solo = 1
number = 1

connection.executescript(("insert into artiste"
                          "(nom, est_solo, nombre_individus) "
                          "values('%s', %d, %d)") % (name, solo, number))
connection.commit()

connection.close()