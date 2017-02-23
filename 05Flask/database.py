# coding: utf8

import sqlite3


def build_artist_dictionary(row):
    return {"id": row[0], "nom": row[1], "est_solo": row[2], "nombre_individus": row[3]}


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/musique.db')
        return self.connection

    def get_connection2(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/musique.db')
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_artists(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id, nom, est_solo, nombre_individus from artiste")
        artists = cursor.fetchall()
        return [build_artist_dictionary(each) for each in artists]

        #return [build_artist_dictionary(each) for each in artists]
        # {% for artist in artists %}
        #   <li> {{ artist[1] }} ----- {{ artist1 }} -------------------------------------------------- {{ artist1["id"] }} }}  </li>
        #           N/A ----- {'nom': u'Michael Jackson', 'id': 1, 'est_solo': 1, 'nombre_individus': 1} --- 1
        # {% endfor %}

        #return [each for each in artists]
        # {% for artist in artists %}
        #   <li> {{ artist[1] }} ----- {{ artist1 }} --- {{ artist1["id"] }} }}  </li>
        #    Michael Jackson ----- (1, u'Michael Jackson', 1, 1) --- N/A
        # {% endfor %}

        #return [each[1] for each in artists]
        # {% for artist in artists %}
        #   <li> {{ artist[1] }} ----- {{ artist1 }} --- {{ artist1["id"] }} }}  </li>
        #              i ----------- Michael Jackson -------- N/A
        # {% endfor %}

        # return artists
        # {% for artist in artists %}
        #   <li> {{ artist[1] }} ----- {{ artist1 }} --- {{ artist1["id"] }} }}  </li>
        #    Michael Jackson ----- (1, u'Michael Jackson', 1, 1) --- N/A
        # {% endfor %}

        # cursor = self.get_connection2().cursor()
        # return artists
        # {% for artist in artists %}
        #   <li> {{ artist[1] }} ----- {{ artist1 }} --- {{ artist1["id"] }} }}  </li>
        #    Michael Jackson --- <sqlite3.Row object at 0x7fbb6674bfb0> -- 1


        # {% endfor %}

    def get_artist(self, identifier):
        cursor = self.get_connection().cursor()
        print identifier
        cursor.execute("select id, nom, est_solo, nombre_individus from artiste where id = ?", (identifier,))
        artist = cursor.fetchone()
        if artist is None:
            return None
        else:
            return build_artist_dictionary(artist)