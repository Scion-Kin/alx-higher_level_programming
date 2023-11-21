#!/usr/bin/python3
'''Defining a class'''


class Square:
    '''If anything apart from int is passed, I raise an error'''

    def __init__(here, size=0, position=(0, 0)):

        here.size = size
        here.position = position

    @property
    def size(here):
        return here.__size

    @size.setter
    def size(here, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        here.__size = value

    @property
    def position(here):
        return here.__position

    @position.setter
    def position(here, value):
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        here.__position = value

    def area(here):
        return here.__size * here.__size

    def my_print(here):
        """Print the square with the # character."""
        if here.__size == 0:
            print("")
            return

        for i in range(0, here.__position[1]):
            print("")

        for i in range(0, here.__size):
            for j in range(0, here.__position[0]):
                print(" ", end="")
            for k in range(0, here.__size):
                print("#", end="")
            print("")
