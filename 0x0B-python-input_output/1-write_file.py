#!/usr/bin/python3
'''This is a module containing a writing function'''


def write_file(filename="", text=""):
    '''This function writes to a file and
    returns the number of characters written'''

    count = 0

    with open(filename, mode="w", encoding="UTF-8") as file:

        for i in text:
            file.write(i)
            count += 1

    return count
