#!/usr/bin/python3
"""A module containing a class definition"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class definition """

    def __init__(self, width, height):
        """ Method determining values """

        self.__width = self.integer_validator(width)
        self.__height = self.integer_validator(height)
