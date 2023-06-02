#!/bin/bash
# Only status code
curl -s -i -L -X OPTIONS $1 | grep -i "HTTP" |cut -d ' ' -f2
