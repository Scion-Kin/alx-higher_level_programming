#!/usr/bin/python3
''' This script fetches a web page '''

from urllib.request import Request, urlopen

req = Request('https://alx-intranet.hbtn.io/status')

with urlopen(req) as data:
    data = data.read()
    print('Body response:')
    print('    - type: ', type(data))
    print('    - content: ', data)
    print('    - utf8 content: ', data.decode('utf-8'))
