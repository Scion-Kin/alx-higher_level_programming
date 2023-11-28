#!/usr/bin/python3
"""A class defining a Rectangle"""


class Rectangle:
    """Read the code"""
    def __init__(self, width=0, height=0):
        """documentation pending"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """documentation pending"""

        return self.__width

    @width.setter
    def width(self, value):
        """documentation pending"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """documentation pending"""

        return self.__height

    @height.setter
    def height(self, value):
        """documentation pending"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """documentation pending"""
        return self.__width * self.__height

    def perimeter(self):
        """documentation pending"""
        if self.__width == 0 or self.__height:
            return 0

        return 2 * (self.__width + self.__height)
