#!/usr/bin/python3
"""
    Write a Python script that takes in a URL, 
    sends a request to the URL and displays the value of the X-Request-Id 
    variable found in the header of the response.
 """


import urllib.request
import sys
"""import modules"""


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        XRequestId = response.info().get('X-Request-Id')
        print("{}".format(XRequestId))
