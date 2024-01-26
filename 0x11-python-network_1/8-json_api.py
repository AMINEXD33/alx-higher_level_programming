#!/usr/bin/python3
"""
 a script that accepts a letter, 
 then initiates a POST request to 
 http://0.0.0.0:5000/search_user with the letter as a 
 parameter stored in the variable q. If no argument is provided, set q="".
 If the response body is both properly formatted as JSON and not empty, present t
 he id and name in the format: "[<id>] <name>". 
 In case the JSON is invalid, display "Not a valid JSON", 
 and if the JSON is empty, display "No result".
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {"q": q}
    response = requests.post(url, data=payload)
    try:
        json_outp = response.json()
        if not json_outp:
            print("No result")
        else:
            my_id = json_outp.get("id")
            my_name = json_outp.get("name")
            print("[{}] {}".format(my_id, my_name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
