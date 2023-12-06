#!/usr/bin/python3
'''This is a module containing an appending function'''


def append_write(filename="", text=""):
    '''This function appends to a file and
    returns the number of characters written'''

    count = 0

    with open(filename, mode="a", encoding="UTF-8") as file:

        for i in text:
            file.write(i)
            count += 1

    return count
