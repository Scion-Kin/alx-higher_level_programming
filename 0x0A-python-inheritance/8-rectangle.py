#!/usr/bin/python3
"""A module containing a class definition"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class definition """

    def __init__(self, width, height):
        """ Method determining values """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
