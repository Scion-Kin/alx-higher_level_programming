#!/usr/bin/python3
'''This module contains a class definition'''


class Student:
    '''Class that defines a student's properties and methods'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(passed) == str for passed in attrs)):
            return {i: getattr(self, i)
                    for i in attrs if hasattr(self, i)}

        return self.__dict__
