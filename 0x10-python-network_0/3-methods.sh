#!/bin/bash
# show all allowed methods
var=$( curl -sIX OPTIONS $1 ); echo "$var"  | grep -Po '(?<=Allow: ).*'
