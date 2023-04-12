#!/usr/bin/python3
import requests
import sys
"""Import resquests module"""


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})
    print("Your email is: {}".format(email))
