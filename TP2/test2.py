# coding: utf8

import requests

# Lire la liste des pays
response = requests.get('http://localhost:5000/api/articles/')
if response.status_code == 200:
    collection = response.json()
    for each in collection:
        print each["titre"], "-", each["auteur"], each["URL"]
else:
    print "Erreur lors de la lecture du service"

# Lire la liste des pays
ident = "singe"
url = "%s%s" % ('http://localhost:5000/api/article/', ident)
response = requests.get(url)
if response.status_code == 200:
    artcle = response.json()
    print artcle["_id"], "-", artcle["titre"], "-", artcle["auteur"], "-", artcle["date_publication"], "-", artcle["paragraphe"]
else:
    print "Erreur lors de la lecture du service"

# Créer un nouveau pays
# nouveau = {"titre":"Bebe Sing22e", "identifiant":"bebe-singe22", "auteur":"Megane Provot", "date":"2017-08-08", "paragraphe":"paragraphe test test test"}
# post_response = requests.post('http://localhost:5000/api/articles/', json=nouveau)
# if post_response.status_code == 201:
#     print "Article créé avec succès"
# else:
#     print "Erreur avec la création de l'article"