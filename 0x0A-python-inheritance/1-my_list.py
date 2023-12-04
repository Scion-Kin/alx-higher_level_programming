#!/usr/bin/python3
"""A class module"""


class MyList(list):
    """A class MyList that inherits from list and a Public instance method."""

    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
