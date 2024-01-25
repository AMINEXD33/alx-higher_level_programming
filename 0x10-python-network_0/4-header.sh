#!/bin/bash
# sends a GET request to the URL, and displays the body of the response with a var in the header
curl -sX GET -H "X-School-User-Id: 98" "$1"
