# coding: utf8
#
# author: Jean-Michel Poirier
# code: POIJ26089200

from database import Database


class Article(Database):
    def __init__(self):
        self.connection = None

    def get_cinq_last_publications(self):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT * FROM article "
                       "WHERE date_publication < date('now') "
                       "ORDER BY date_publication DESC")
        publications = cursor.fetchmany(5)
        return publications

    def get_search_articles(self, like_recher):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT * FROM article "
                       "WHERE paragraphe LIKE ? "
                       "AND date_publication < date('now') "
                       "OR titre LIKE ? "
                       "AND date_publication < date('now')",
                       (like_recher, like_recher))
        articles = cursor.fetchall()
        return articles

    def get_all_articles(self):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT titre, identifiant, auteur, date_publication "
                       "FROM article")
        articles = cursor.fetchall()
        return articles

    def get_article(self, ident):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT id, titre, identifiant, auteur, "
                       "date_publication, paragraphe "
                       "FROM article WHERE date_publication < date('now')"
                       "AND identifiant = ?", (ident,))
        article = cursor.fetchone()
        return article

    def get_admin_article(self, ident):
        cursor = self.get_connection_row().cursor()
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


    def get_user_login_info(self, username):
        cursor = self.get_connection().cursor()
        cursor.execute("select salt, hash from users where utilisateur=?", (username,))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return user[0], user[1]

    def save_session(self, id_session, username):
        connection = self.get_connection()
        connection.execute("insert into sessions(id_session, utilisateur) values(?, ?)", (id_session, username))
        connection.commit()

    def delete_session(self, id_session):
        connection = self.get_connection()
        connection.execute("delete from sessions where id_session=?", (id_session,))
        connection.commit()

    def get_session(self, id_session):
        cursor = self.get_connection().cursor()
        cursor.execute("select utilisateur from sessions where id_session=?", (id_session,))
        data = cursor.fetchone()
        if data is None:
            return None
        else:
            return data[0]

    def get_emails(self):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT id, email FROM users")
        emails = cursor.fetchall()
        return emails