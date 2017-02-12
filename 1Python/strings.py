# coding: utf8

# Délimiteurs de chaîne
print "Chaîne avec des caractères accentués"
print 'Chaîne avec des caractères accentués'
print "J'aime les fruits."
print 'Ces élus sont "compétents", parfois!'

# Plusieurs paramètres au print (affichés avec un espace entre chacun)
nombre_pomme = 5
print "J'ai mangé", nombre_pomme, "pommes pour souper hier."
print "J'ai mangé %d pommes pour souper hier." % nombre_pomme

#Formatage
nombre_poire = 3
nombre_oranges = 4

phrase = "test"
print phrase

phrase2 = "J'ai mangé %d pommes, " \
          "%d poires, %d oranges pour ce matin."
print phrase2 % (nombre_pomme, nombre_poire, nombre_oranges)

phrase3 = ("J'ai mangé %d pommes, "
          "%d poires, %d oranges pour cette aprem.")
print phrase3 % (nombre_pomme, nombre_poire, nombre_oranges)

# Multi-lignes
longue_chaine = """Test"""
print longue_chaine

longue_chaine2 = """
Une petite anecdote que j'ai vécue lorsque j'ai terminé mon cégep et qui me
fait toujours rire, même aujourd'hui.

En 2003, le marché du développement de logiciels n'était pas aussi
intéressant qu'aujourd'hui à Montréal. À l'époque, il y avait plus d'offre
que de demande et les emplois étaient plus rares. Du moins, les bons emplois
étaient plus rares.

Fraîchement sorti du cégep avec mon DEC en informatique de gestion en poche,
"""
print longue_chaine2

# Longueur d'une chaîne
print "Longueur de ce texte :", len(longue_chaine2), "!!!"
