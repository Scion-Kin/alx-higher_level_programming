#!/usr/bin/python3
"""A module containing a function for reading files"""


def read_file(filename=""):
    """Prints the content of a passed file"""

    with open(filename, encoding="UTF-8") as text:
        for i in text:
            print(i, end="")
