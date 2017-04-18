**Ajouter un article**
----
Cette API permet d'ajouter un article à la liste d'article.

* **URL**

  /api/articles/

* **Méthode:**

  POST

*  **Les Paramètres de l'url**

   N/A

* **Format des données reçues:**

   N/A

* **Format des données à envoyer:**

  Content-Type: application/json

  ex: {"titre":"", "identifiant":"", "auteur":"", "date":"", "paragraphe":""}

* **Success Response:**

  * **Code:** 201 <br />
   L'article à été ajouter avec succès

* **Error Response:**

  * **Code:** 400 <br />
    L'article n'est pas valide et n'a pas été ajouté

* **Exemple d'utilisation:**

```
nouveau = {"titre":"Les tigres", "identifiant":"tigres", "auteur":"Megane Provot", "date":"2017-08-08", "paragraphe":"paragraphe test test test"}
post_response = requests.post('http://localhost:5000/api/articles/', json=nouveau)
if post_response.status_code == 201:
    print "Article créé avec succès"
else:
    print "Erreur avec la création de l'article"
```


**Liste des articles**
----
Cette API permet d'afficher tous les articles

* **URL**

  /api/articles/

* **Méthode:**

  GET

*  **Les Paramètres de l'url**

    N/A

* **Format des données reçues:**

  Content-Type: application/json

  ex:
 ```
  [
  {
    "URL": "http://127.0.0.1:5000/article/singe",
    "auteur": "Jacques Berger",
    "titre": "Singe de lAfrique"
  },
  {
    "URL": "http://127.0.0.1:5000/article/ours",
    "auteur": "Burrell Verreau",
    "titre": "Ours polaire"
  },
  {
    "URL": "http://127.0.0.1:5000/article/bebe-singe",
    "auteur": "Megane Provot",
    "titre": "Bebe Singe"
  }
]
```

* **Format des données à envoyer:**

  N/A

* **Success Response:**

  * **Code:** 200 <br />
   La liste des articles a été générée avec succès.


* **Exemple d'utilisation:**

```
response = requests.get('http://localhost:5000/api/articles/')
if response.status_code == 200:
    collection = response.json()
    for each in collection:
        print each["titre"], "-", each["auteur"], "-", each["URL"]
else:
    print "Erreur lors de la lecture du service"
```



**Obtenir un article**
----
Cette API permet d'aller chercher un article en particulier spécifié dans un paramètre de l'url.

* **URL**

  /api/article/\<identifiant\>

* **Méthode:**

  GET

*  **Les Paramètres de l'url**

    -\<identifiant\> <br />
    Correspond à l'identifiant d'un article. (L'identifiant est unique pour chaque aricle)

* **Format des données reçues:**

  Content-Type: application/json

  ex:
  ```
    {
      "_id": 1,
      "auteur": "Jacques Berger",
      "date_publication": "2017-01-13",
      "paragraphe": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan.",
      "titre": "Singe de lAfrique"
    }
   ```

* **Format des données à envoyer:**

    N/A

* **Success Response:**

  * **Code:** 200 <br />
   L'artcle en question a été généré avec succès.

* **Exemple d'utilisation:**

    ```
    ident = "singe"
    url = "%s%s" % ('http://localhost:5000/api/article/', ident)
    response = requests.get(url)
    if response.status_code == 200:
        artcle = response.json()
        print artcle["_id"], "-", artcle["titre"], "-", artcle["auteur"], "-", artcle["date_publication"], "-", artcle["paragraphe"]
    else:
        print "Erreur lors de la lecture du service"
    ```