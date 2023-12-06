#!/usr/bin/python
'''This is a script generated documentation'''


def read_file(filename=""):

    import os

    with open(filename, mode="r", encoding="UTF-8") as text:
        for i in text:
            print(i, end="")
        print()
