# coding: utf8

# On peux utiliser la fonction super() pour appeler des méthodes de la classe de base à partir d'une classe dérivée.


class Person(object):
    def __init__(self, prenom, nom, age):
        self.prenom = prenom
        self.nom = nom
        self.age = age

    def get_complete_name(self):
        return "%s %s" % (self.prenom, self.nom)


class Student(Person):
    def __init__(self, prenom, nom, age, code):
        super(Student, self).__init__(prenom, nom, age)
        self.code = code

    def get_complete_name(self):
        return "%s [%s]" % (super(Student, self).get_complete_name(), self.code)


class Teacher(Person):
    def __init__(self, prenom, nom, age, employee_number):
        super(Teacher, self).__init__(prenom, nom, age)
        self.employee_number = employee_number

    def get_complete_name(self):
        return "A teacher has no name"


person1 = Person("Paul", "Berger", 66)
print person1.get_complete_name()

student1 = Student("JM", "Poirier", 18, "POIJ26089200")
print student1.get_complete_name()

teacher1 = Teacher("Jacques", "Berger", 69, "INFPROF")
print teacher1.get_complete_name()