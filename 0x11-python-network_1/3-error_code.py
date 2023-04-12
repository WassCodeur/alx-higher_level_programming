#!/usr/bin/python3
import urllib.request
import urllib.error
import sys
"""import modules"""


if __name__ == 'main':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print("{}".format(result.decode('utf8')))
    except urllib.error.HTTPError as e:
        print("Erroer code: {}".format(e.code))
