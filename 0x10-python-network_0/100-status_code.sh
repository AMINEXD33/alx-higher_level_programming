#!/bin/bash 
# sends a request to a URL (as arg), and displays only the status code of the response.
curl -s -L -X HEAD -w "%{http_code}" "$1"
