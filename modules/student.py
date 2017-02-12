# coding: utf8

from person import Person


class Student(Person):
    def __init__(self, firstname, lastname, age, code):
        super(Student, self).__init__(firstname, lastname, age)
        self.code = code

    def get_complete_name(self):
        return "%s [%s]" % (super(Student, self).get_complete_name(),
                            self.code)