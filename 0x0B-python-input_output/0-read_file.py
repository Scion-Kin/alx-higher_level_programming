#!/usr/bin/python
"""A module containing a function for reading files"""


def read_file(filename=""):
    """Prints the content of a passed file"""

    with open(filename, mode="r", encoding="utf-8") as text:
        print(text.read(), end="")
