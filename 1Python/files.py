# coding: utf8

from os.path import exists

# Afficher le contenu d'un fichier à la console
text_file = open("input/input1.txt")
print text_file.read()
text_file.close()

print ""

# Lire une seule ligne d'un fichier
fichier_input1 = open("input/input1.txt")
une_ligne = fichier_input1.readline()
print une_ligne
fichier_input1.close()

# Créer un fichier et y écrire des données
output = open("input/result2.txt", "w")
resto_prefere = "Chez Maurice"
phrase = "J'adore manger %s pour souper." % resto_prefere
output.write(phrase)
output.close()

# Vérifier si un fichier existe
print exists("input/result2.txt")
print exists("input/result22.txt")