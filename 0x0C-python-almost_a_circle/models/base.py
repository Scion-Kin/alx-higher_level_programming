#!/usr/bin/python3
'''This module contains a class definition'''


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
