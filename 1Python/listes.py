# coding: utf8
# %d = decimal
# %s = string
# %r = objet

une_liste = ["Pascal", "Java", "Python", "Ruby", "Groovy", "Javascript", "SQL"]

# Boucler sur une liste
for each in une_liste:
    print each

print "Taille de la liste :", len(une_liste)

# Générer une liste de valeurs et boucler dessus
for i in range(0, 10):
    print i

# Opérateur []
print une_liste[2] #Python

# Version longue de la boucle
for i in range(0, len(une_liste), 1):
    print "Élément no. %d : %s" % (i + 1, une_liste[i])