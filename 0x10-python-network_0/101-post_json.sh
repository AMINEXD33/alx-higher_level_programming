#!/bin/bash
# sends a JSON POST request to a URL passed as(arg 1), and displays the body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
