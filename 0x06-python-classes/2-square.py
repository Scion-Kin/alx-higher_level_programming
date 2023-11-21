#!/usr/bin/python3
'''Defining a class'''


class Square:
    '''If anything apart from int is passed, I raise an error'''

    def __init__(here, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        here.__size = size
