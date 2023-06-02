#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body 
curl -s -o /dev/null -w "%{http_code}" $1 | grep -q 200 && curl $1 
