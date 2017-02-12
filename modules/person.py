# coding: utf8


class Person(object):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def get_complete_name(self):
        return "%s %s" % (self.firstname, self.lastname)