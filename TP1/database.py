# coding: utf8

import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/db.db')
        return self.connection

    def get_connection2(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/db.db')
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_5_last_publications(self):
        cursor = self.get_connection2().cursor()
        cursor.execute("SELECT * FROM article WHERE date_publication < date('now') ORDER BY date_publication DESC")
        publications = cursor.fetchmany(5)
        return publications

    def get_id_article(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id from article")
        ids = cursor.fetchall()
        return [identity[0] for identity in ids]

    def get_titre_article(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select titre from article")
        titres = cursor.fetchall()
        return [titre[0] for titre in titres]

    def get_identifiant_article(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select identifiant from article")
        identifiants = cursor.fetchall()
        return [identifiant[0] for identifiant in identifiants]

    def get_auteur_article(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select auteur from article")
        auteurs = cursor.fetchall()
        return [auteur[0] for auteur in auteurs]

    def get_date_publication_article(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select date_publication from article")
        dates = cursor.fetchall()
        return [date[0] for date in dates]

    def get_paragraphe_article(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select paragraphe from article")
        paragraphes = cursor.fetchall()
        return [paragraphe[0] for paragraphe in paragraphes]


    # def get_albums(self):
    #     cursor = self.get_connection().cursor()
    #     cursor.execute("select titre from album")
    #     albums = cursor.fetchall()
    #     return [album[0] for album in albums]
    #
    # def insert_artist(self, name):
    #     connection = self.get_connection()
    #     cursor = connection.cursor()
    #     cursor.execute(("insert into artiste(nom, est_solo, nombre_individus) "
    #                     "values(?, ?, ?)"), (name, 0, 0))
    #     connection.commit()