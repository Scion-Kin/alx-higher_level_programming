#!/usr/bin/python3
"""A class defining a Rectangle"""


class Rectangle:
    """Read the code"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def use_print_symbol(cls, print_symbol):

        cls.print_symbol = print_symbol

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

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

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):

        if self.__height == 0 or self.__width == 0:
            return ("")

        return ((str(self.print_symbol) * self.__width + '\n') *
                (self.__height - 1) +
                str(self.print_symbol) * self.__width)

    def __repr__(self):

        return ('Rectangle(' + str(self.__width) + ', '
                + str(self.__height) + ')')

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
