#!/usr/bin/python3
''' This scripts handles JSON responses '''

if __name__ == '__main__':

    import sys
    import requests

    q = sys.argv[1] if len(sys.argv) > 1 else ''

    r = requests.get('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        if r.json() == {}:
            print('No result')

        else:
            for key, value in r.json():
                print('[{}] {}'.format(key, value))

    except ValueError:
        print('Not a valid JSON')
