# coding: utf8

# Marche / Pas de message d'erreur
try:
    file_handle = open("input/input1.txt")
except IOError as e:
    print "Erreur avec le fichier de lecteure :", e.strerror

# Marche pas / Génère un message un d'erreur
try:
    file_handle = open("input/not_exist.txt")
except IOError as e:
    print "Erruer avec le fichier de lecteure :", e.strerror

# Lancer une exception
chiffre = 10
if chiffre != 10:
    raise ValueError('Still no search engine')

# Errors and Exceptions
# https://docs.python.org/2.7/tutorial/errors.html

# Built-in Exceptions
# https://docs.python.org/2/library/exceptions.html