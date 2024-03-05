#!/usr/bin/python3
''' This scripts fetches most recent commits in a github repo '''

if __name__ == '__main__':

    import sys
    import requests

    req = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[1], sys.argv[2]))

    r = req.json()

    try:
        for i in range(10):
            print('{}: {}'.format(r[i].get('sha'),
                  r[i].get('commit').get('author').get('name')))

    except IndexError:
        pass
