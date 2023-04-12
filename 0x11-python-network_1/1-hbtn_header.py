#!/usr/bin/python3
import urllib.request
import sys
"""import modules"""


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        XRequestId = response.getheader('X-Request-Id')
        print(XRequestId)
