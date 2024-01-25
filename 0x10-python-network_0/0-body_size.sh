#!/bin/bash
# get the header size of a response
curl -sI "$1" | grep -Po "(?<=Content-Length: )[0-9]+"
