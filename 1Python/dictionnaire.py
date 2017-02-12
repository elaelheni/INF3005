# coding: utf8


dictionnaire = {"nom": "Berger", "prenom": "Jacques", 66: 77, "age": 18}
print dictionnaire

# Accéder à un élément
print dictionnaire[66]

# Boucler sur les valeurs
for cle, valeur in dictionnaire.items():
    print cle, ":", valeur

# Supprimer l'âge
del dictionnaire["age"]
print dictionnaire

# Ajouter un élément
dictionnaire["vivant"] = True
print dictionnaire