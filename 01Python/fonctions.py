# coding: utf8

# Le noms des fonctions sont en snake_case

import datetime


# Fonction sans valeur de retour
def print_error_msg(message):
    today = get_today()
    print "Erreur:", today, message


# Fonction avec valeur de retour
def get_today():
    return datetime.date.today()

print_error_msg("Le message d'erreur")

# Fonction dans une variable
new_function = get_today()
print new_function
