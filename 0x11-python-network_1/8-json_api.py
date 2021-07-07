#!/usr/bin/python3
"""module"""

import requests
import sys
if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post(url, data={'q': q}).json()
    try:
        if r:
            idd = r['id']
            name = r['name']
            print('[{}] {}'.format(idd, name))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
