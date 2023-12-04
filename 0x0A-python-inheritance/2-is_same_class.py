#!/usr/bin/python3
"""A module to check for an instance's property"""


def is_same_class(obj, a_class):
    """checks if an object is an instance of the specified class"""

    return type(obj) == a_class
