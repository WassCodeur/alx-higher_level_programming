#!/usr/bin/python3
"""
    a Python script that takes in a URL,
    sends a request to the URL and displays the body of the response.
"""


import requests
import sys
"""Import resquests module"""


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    statusCode = req.status_code
    if statusCode < 400:
        print("{}".format(req.text))
    elif statusCode >= 400:
        print("Error code: {}".format(statusCode))
