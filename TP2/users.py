# coding: utf8
#
# author: Jean-Michel Poirier
# code: POIJ26089200

from article import Article


class Users(Article):
    def __init__(self):
        super(Users, self).__init__()
        self.connection = None

    def get_user_login_info(self, username):
        cursor = self.get_connection().cursor()
        cursor.execute("select salt, hash from users where utilisateur=?",
                       (username,))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return user[0], user[1]

    def save_session(self, id_session, username):
        connection = self.get_connection()
        connection.execute("insert into sessions(id_session, utilisateur)"
                           " values(?, ?)", (id_session, username))
        connection.commit()

    def delete_session(self, id_session):
        connection = self.get_connection()
        connection.execute("delete from sessions where id_session=?",
                           (id_session,))
        connection.commit()

    def get_session(self, id_session):
        cursor = self.get_connection().cursor()
        cursor.execute("select utilisateur from sessions where id_session=?",
                       (id_session,))
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

    def get_users(self):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT utilisateur FROM users")
        users = cursor.fetchall()
        return users

    def get_email(self, token):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT email, expiration FROM emails WHERE token = ?",
                       (token,))
        email = cursor.fetchone()
        return email

    def insert_reset_password(self, email, token, date):
        connection = self.get_connection()
        connection.execute("insert into emails(email, token, expiration) "
                           "values(?, ?, ?)", (email, token, date))
        connection.commit()

    def uptade_password(self, email, salt, hash):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET salt=?, hash=? WHERE email = ?",
                       (salt, hash, email))
        connection.commit()

    def insert_new_user(self, email, token, date):
        connection = self.get_connection()
        connection.execute("insert into new_user(email, token, expiration) "
                           "values(?, ?, ?)", (email, token, date))
        connection.commit()

    def get_email_new_user(self, token):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT email, expiration FROM new_user "
                       "WHERE token = ?", (token,))
        email = cursor.fetchone()
        return email

    def insert_user(self, username, email, salt, hash):
        connection = self.get_connection()
        connection.execute("insert into users(utilisateur, email, salt, hash)"
                           " values(?, ?, ?, ?)",
                           (username, email, salt, hash))
        connection.commit()

    def uptade_user(self, email, expiration):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE new_user SET expiration=? WHERE email = ?",
                       (expiration, email))
        connection.commit()
