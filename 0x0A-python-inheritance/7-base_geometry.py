#!/usr/bin/python3
"""A module containing class"""


class BaseGeometry:
    """An class with methods that raises an exception if there is one"""

    def area(self):
        """raises an exception"""

        raise Exception(area() is not implemented)

    def integer_validator(self, name, value):
        """validates if a value is an integer and is > 0"""

        if not type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
