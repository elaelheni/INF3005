#coding: utf8

#Afin de pouvoir importer les fonctionnalités d'un module, le répertoire contenant le module à importer doit avoir un fichier __init__.py vide

from person import Person
from student import Student
from teacher import Teacher

regular_person = Person("Vince", "Neil", 51)
print regular_person.get_complete_name()

steven = Student("Steven", "Stevenson", 19, "STES12129701")
print steven.get_complete_name()

teacher = Teacher("Jacques", "Berger", 87, "IEPSW3")
print teacher.get_complete_name()