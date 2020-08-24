#!/usr/bin/python3
"""takes in a URL and an email, sends a POST
request to the passed URL"""


from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            page = response.read()
            print(page.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
