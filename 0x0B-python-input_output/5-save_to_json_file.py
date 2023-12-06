#!/usr/bin/python3
'''This module deals with handling JSON data'''


def save_to_json_file(my_obj, filename):
    '''This function writes the data in "my_obj" to the
    file passed as "filename"'''

    import json

    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
