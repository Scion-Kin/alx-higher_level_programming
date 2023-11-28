#!/usr/bin/python3
"""A class defining a Rectangle"""


class Rectangle:
    """Read the code"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
