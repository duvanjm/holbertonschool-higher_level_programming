#!/usr/bin/python3
"""module"""

import requests
import requests.auth
import sys


if __name__ == '__main__':
    name = sys.argv[1]
    pswd = sys.argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(name, pswd)).json()
    try:
        print(r['id'])
    except KeyError:
        print(None)
