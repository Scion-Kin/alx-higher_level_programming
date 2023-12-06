#!/usr/bin/python3
'''This is a module containing a function that deals with JSON'''


def to_json_string(my_obj):
    '''Returns a JSON representation of a passed object'''

    import json

    data = json.dumps(my_obj)

    return data
