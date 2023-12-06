#!/usr/bin/python
'''A module containingf a function for reading files'''


def read_file(filename=""):
    '''Prints the content of a passed file'''

    with open(filename, mode="r", encoding="UTF-8") as text:
        print(text.read(), end="")
