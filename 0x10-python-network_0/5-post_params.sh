#!/bin/bash
# post two variables to the server
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
