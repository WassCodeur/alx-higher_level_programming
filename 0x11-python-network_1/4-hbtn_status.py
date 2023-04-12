#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status
 """


import requests
"""Import resquests module"""


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    print('Body response:')
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
