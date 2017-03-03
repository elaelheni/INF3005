# coding: utf8

from database import Database


class Article(Database):
    def __init__(self):
        self.connection = None

    def get_cinq_last_publications(self):
        cursor = self.get_connection2().cursor()
        cursor.execute("SELECT * FROM article "
                       "WHERE date_publication < date('now') "
                       "ORDER BY date_publication DESC")
        publications = cursor.fetchmany(5)
        return publications

    def get_search_articles(self, like_recher):
        cursor = self.get_connection2().cursor()
        cursor.execute("SELECT * FROM article "
                       "WHERE paragraphe LIKE ? "
                       "OR titre LIKE ?", (like_recher, like_recher))
        articles = cursor.fetchall()
        return articles

    def get_all_articles(self):
        cursor = self.get_connection2().cursor()
        cursor.execute("SELECT titre, identifiant, date_publication "
                       "FROM article")
        article = cursor.fetchall()
        return article

    def get_article(self, ident):
        cursor = self.get_connection2().cursor()
        print ident
        cursor.execute("SELECT id, titre, identifiant, auteur, "
                       "date_publication, paragraphe "
                       "FROM article WHERE identifiant = ?", (ident,))
        article = cursor.fetchone()
        return article

    def insert_article(self, titre, identifiant, auteur, date_pub, paragraphe):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(("INSERT into article(titre, identifiant, auteur, "
                        "date_publication, paragraphe) "
                        "values(?, ?, ?, ?, ?)"),
                       (titre, identifiant, auteur, date_pub, paragraphe))
        connection.commit()

    def uptade_article(self, identifier, titre, paragraphe):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE article SET titre=?, paragraphe=? "
                       "WHERE id = ?", (titre, paragraphe, identifier))
        connection.commit()
