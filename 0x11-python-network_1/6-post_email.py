#!/usr/bin/python3
''' This script makes a request with custom parameters '''

if __name__ == '__main__':

    import sys
    import requests

    r = requests.post(sys.argv[1], params={'email': sys.argv[2]})

    print(r.text)
