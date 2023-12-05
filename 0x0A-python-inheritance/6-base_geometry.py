#!/usr/bin/python3
"""A module containing class"""


class BaseGeometry:
    """An class with a method that raises an exception"""

    def area(self):
        """raises an exception"""

        raise Exception("area() is not implemented")
