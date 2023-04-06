#!/bin/bash
curl -s -w "%{http_code}==200" $1
