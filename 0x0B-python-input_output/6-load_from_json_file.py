#!/usr/bin/python3
'''This module deals with handling JSON data'''


def load_from_json_file(filename):
    '''This function reads from JSON file and decodes the data'''

    import json

    with open(filename) as file:
        data = json.load(file)

    return data
