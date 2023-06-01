#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -i -L -X OPTIONS $1 | grep -i "Allow" | cut -d ':' -f2
