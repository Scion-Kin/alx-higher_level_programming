#!/usr/bin/python3
'''This module contains a class definition'''
import json


class Base:
    '''A class defining a base for item construction'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Defines the class instances.'''

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open((cls.__name__ + ".json"), "w", encoding="UTF-8") as file:
            if list_objs is None:
                json.dump("[]")

            else:
                data = [obj.to_dictionary() for obj in list_objs]

                json.dump(data, file)

    def from_json_string(json_string):
        return json.loads(json_string)

    '''@classmethod
    def create(cls, **dictionary):'''
