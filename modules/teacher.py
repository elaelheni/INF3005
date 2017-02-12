# coding: utf8

from person import Person


class Teacher(Person):
    def __init__(self, firstname, lastname, age, employee_number):
        super(Teacher, self).__init__(firstname, lastname, age)
        self.employee_number = employee_number

    def get_complete_name(self):
        return "A Teacher Has No Name"
