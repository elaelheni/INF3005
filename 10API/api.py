# coding: utf8
#
# Code pour appeler des fonctions d'une API


import requests

# Lire la liste des pays
response = requests.get('http://localhost:5000/api/pays/')
if response.status_code == 200:
    collection = response.json()
    for each in collection:
        print each['nom']
else:
    print "Erreur lors de la lecture du service"


# Créer un nouveau pays
nouveau = {'nom': 'Russie'}
post_response = requests.post('http://localhost:5000/api/pays/', json=nouveau)
if post_response.status_code == 201:
    print "Pays créé avec succès"
else:
    print "Erreur avec la création du pays"
#Cre la le pays:
# {
#   "_id": 18,
#   "nom": "Russie"
# }