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
        '''This static method converts and returns a string
        into json format'''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves objects to a file in json format'''
        with open((cls.__name__ + ".json"), "w", encoding="UTF-8") as file:
            if list_objs is None:
                file.write("[]")

            else:
                data = [obj.to_dictionary() for obj in list_objs]

                file.write(Base.to_json_string(data))

    def from_json_string(json_string):
        '''converts json strings to a "normal" python string'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Creates class instances from dictionary arguments'''
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''loads from a json file and creates class instances'''
        try:
            with open((cls.__name__ + ".json"), "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**i) for i in list_dicts]
        except IOError:
            return []
