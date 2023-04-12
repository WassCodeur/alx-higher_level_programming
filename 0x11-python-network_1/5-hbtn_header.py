#!/usr/bin/python3
import requests
import sys
"""Import resquests module"""


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    XRequestId = req.headers['X-Request-Id']
    print("{}".format(XRequestId))
