#!/bin/bash
# get the body of a 200 status request only
curl -sIX OPTIONS $1 | grep -Po '(?<=Allow: ).*'
