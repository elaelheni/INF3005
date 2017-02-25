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

    def get_search_articles(self, like_recher):
        cursor = self.get_connection2().cursor()
        cursor.execute("SELECT * FROM article WHERE paragraphe LIKE ? OR titre LIKE ?", (like_recher, like_recher))
        articles = cursor.fetchall()
        return articles

    def get_all_article(self):
        cursor = self.get_connection2().cursor()
        cursor.execute("SELECT titre, identifiant, date_publication FROM article")
        article = cursor.fetchall()
        return article

    def get_article(self, ident):
        cursor = self.get_connection2().cursor()
        print ident
        cursor.execute("SELECT id, titre, identifiant, auteur, date_publication, paragraphe FROM article WHERE identifiant = ?", (ident,))
        article = cursor.fetchone()
        if article is None:
            return None
        else:
            return article

    def insert_article(self, titre, identifiant, auteur, date_publication, paragraphe):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(("insert into article(titre, identifiant, auteur, date_publication, paragraphe) "
                        "values(?, ?, ?, ?, ?)"), (titre, identifiant, auteur, date_publication, paragraphe))
        connection.commit()

    def uptade_article(self, identifier, titre, paragraphe):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE article SET titre=?, paragraphe=? WHERE id = ?", (titre, paragraphe, identifier))
        connection.commit()

    def get_id_article(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id from article")
        identifiers = cursor.fetchall()
        return [identifier[0] for identifier in identifiers]

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