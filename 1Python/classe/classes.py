# coding: utf8

# La méthode __init__ est le constructeur
# On place les variables d'instance dans la variable self
# Le nom des classes sont en PascalCase

class Person(object):
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def get_complete_name(self):
        return "Nom complet: %s %s" % (self.prenom, self.nom)

    def set_age(self, age):
        self.age = age

teacher = Person("Jacques", "Berger")
print teacher.nom
print teacher.prenom
print teacher.get_complete_name()
teacher.set_age(20)
print teacher.age