# coding: utf8

import hashlib
import sqlite3
import uuid # universally unique identifier

print "Nom utilisateur : "
username = raw_input()
print "Mot de passe : "
password = raw_input()

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute('select salt, hash from users where utilisateur=?',
               (username,))
user = cursor.fetchone()
connection.close()

if user is None:
    print "Utilisateur inconnu"
else:
    salt = user[0]
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    if hashed_password == user[1]:
        print "Accès autorisé"
    else:
        print "Accès refusé"