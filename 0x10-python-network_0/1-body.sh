#!/bin/bash
# get the body of a 200 status request only
res=$(curl -sI "$1");if [ "$( echo "$res" | grep -Po '(?<=HTTP/\d.\d) \d{3}')" -eq "200" ];then "$(curl "$1")"; fi

