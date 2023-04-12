#!/usr/bin/python3
import urllib.request
"""Import urllib module"""


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        status = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(status)))
        print("\t- content: {}".format(status))
        print("\t- utf8 content: {}".format(status.decode('utf8')))
