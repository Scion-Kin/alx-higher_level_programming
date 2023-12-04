#!/usr/bin/python3
"""Module containing a function"""


def inherits_from(obj, a_class):
    """Checks if obj is inherited from a_class"""

    return (issubclass(type(obj), a_class) and obj != a_class)
