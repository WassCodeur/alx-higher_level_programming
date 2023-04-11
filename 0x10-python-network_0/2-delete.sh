#!/bin/bash
# h script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sSL -X DELETE $1
