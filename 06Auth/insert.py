# coding: utf8

import hashlib
import sqlite3
import uuid # universally unique identifier

print "Nom utilisateur : "
username = raw_input() # Lecture au clavier
print "Mot de passe : "
password = raw_input()

salt = uuid.uuid4().hex # genere identifiant aleatoire en hexadecimal
hashed_password = hashlib.sha512(password + salt).hexdigest()

connection = sqlite3.connect('users.db')

connection.execute("INSERT into users(utilisateur, salt, hash) "
                   "values( ?, ?, ?)", (username, salt, hashed_password))

connection.commit()
connection.close()
