#!/usr/bin/python3
'''This script handles JSON data'''


if __name__ == "__main__":
    '''This writes arguments of this script in a file'''

    import sys

    writer = __import__('5-save_to_json_file').save_to_json_file
    opener = __import__('6-load_from_json_file').load_from_json_file

    try:
        li = opener('add_item.json')

    except FileNotFoundError:
        li = []

    li += sys.argv[1:]

    writer(li, 'add_item.json')
