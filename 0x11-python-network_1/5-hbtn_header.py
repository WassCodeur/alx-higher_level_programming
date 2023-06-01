#!/usr/bin/python3
"""
    Write a Python script that takes in a URL, 
    sends a request to the URL and displays 
    the value of the variable X-Request-Id in the response header
 """
import requests
import sys
"""Import resquests module"""


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    X-Request-Id = req.headers['X-Request-Id']
    print("{}".format(X-Request-Id))
