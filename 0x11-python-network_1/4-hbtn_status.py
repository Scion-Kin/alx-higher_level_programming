#!/usr/bin/python3
''' This script fetches a web page and displays it's content '''

if __name__ == '__main__':

    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(r.text))
