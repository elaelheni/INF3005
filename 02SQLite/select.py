# coding: utf8

import sqlite3

connection = sqlite3.connect('musique.db')
cursor = connection.cursor()
cursor.execute("select * from album")
for row in cursor:
    identifier, album, year, artiste_id, publisher_id = row
    print "%s , %d" % (album, year)
    # print row

connection.close()
