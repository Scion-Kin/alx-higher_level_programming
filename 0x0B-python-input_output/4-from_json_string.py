#!/usr/bin/python3
'''This is a module containing a function for handling JSON data'''


def from_json_string(my_str):
    '''This function eturns an object (Python data structure)
    represented by a JSON string'''

    import json

    data = json.loads(my_str)

    return data
