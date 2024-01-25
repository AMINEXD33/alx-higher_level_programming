#!/usr/bin/env bash

# get the header size of a response
if [ -n "$1" ]; then
    curl -sI "$1" | grep -Po "(?<=Content-Length: )[0-9]+"
fi
