#!/usr/bin/python3
''' This scripts fetches most recent commits in a github repo '''

if __name__ == '__main__':

    import sys
    import requests
    # from requests.auth import HTTPBasicAuth

    # creds = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    req = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[1], sys.argv[2]))

    r = req.json()

    for i in range(10):
        print('{}: {}'.format(r[i].get('sha'),
              r[i].get('commit').get('author').get('name')))
