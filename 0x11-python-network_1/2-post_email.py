#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
"""import modules"""


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        emailSend = response.read()
        print("Your email is: {}".format(emailSend.decode('utf8')))
