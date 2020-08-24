#!/usr/bin/python3
"""script that fetches"""


import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as responce:
        html = responce.read()
        print("Body responde:")
        print("\t - type: {}".format(type(html)))
        print("\t - content: {}".format(html))
        print("\t - utf8 content: {}".format(html.decode("utf-8")))
