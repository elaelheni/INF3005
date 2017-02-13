# coding: utf8

import sqlite3

connection = sqlite3.connect('musique.db')
cursor = connection.cursor()
cursor.execute(("insert into artiste(nom, est_solo, nombre_individus) "
                "values('Brain Surgery', 0, 7)"))

cursor.execute("select last_insert_rowid()")
lastId = cursor.fetchone()[0]
connection.commit()

cursor.execute("update artiste set nom = 'Unstoppable' where id = %d" % lastId)
connection.commit()

cursor.execute("select nom from artiste")
for row in cursor:
    # print row  // Affichie en format base de donne, ex: (u'Unstoppable',)
    print row[0]

connection.close()