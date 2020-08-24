#!/usr/bin/python3
"""takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id"""


from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as responce:
        print(responce.headers.get("X-Request-Id"))
