# CMS

## Description

Application web implémentant un CMS. Le site permet de publier, modifier et rechercher des articles. 
De plus, le CMS comporte un système de connexion (se connecter, s'enregistrer, retrouver son mot de passe), un panneau d'administration et des services REST pour les articles.  
Ce projet s'agit du travail de session développé dans le cadre du cours INF3005 - [Programmation Web avancée](https://etudier.uqam.ca/cours?sigle=INF6150) à [l'Université du Québec à Montréal](https://uqam.ca/).  


## Fonctionnement

Pour lancer le projet, exècuter la commande: ``` make ```    
Dans un navigateur web, entrer le lien: ``` http://localhost:5000/ ```    


## Contenu du projet

- La documentation pour les APIs se trouve dans le fichier [/API.md](API.md)  
- Le script SQL se situe: [/db/db.sql](db/db.sql)  
- Makefile | Exécute le projet  
- Le fichier de configuration pour l'envoie de courriels est [/config.json](config.json) (L'url de modification d'un mot de passe envoyer par courriel expire après 15 mins)  


## Auteur

Jean-Michel Poirier (POIJ26089200)

