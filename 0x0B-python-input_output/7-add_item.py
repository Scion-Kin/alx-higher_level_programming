#!/usr/bin/python3
'''This script handles JSON data'''


if __name__ == "__main__":
    '''This writes arguments of this script in a file'''

    import sys

    writer = __import__('5-save_to_json_file').save_to_json_file
    opener = __import__('6-load_from_json_file').load_from_json_file

    argc = len(sys.argv)
    li = []
    word = ""

    for i in range(1, argc):
        word += sys.argv[i] + " "

    li += word.split()
    print(word)

    writer(li, 'add_item.json')
