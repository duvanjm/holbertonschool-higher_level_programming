#!/usr/bin/python3
"""sends a request to the URL and displays
the body of the response."""

import requests
from sys import argv


if __name__ == "__main__":
    val = requests.get(argv[1])
    if val.status_code >= 400:
        print("Error code: {}".format(val.status_code))
    else:
        print(val.text)
