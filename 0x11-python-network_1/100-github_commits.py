#!/usr/bin/python3
"""
get the lst 10 commits from a users github from the recent to oldest
arg1 is the repo name
the second is the owner name
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repo_name = sys.argv[1]
        username = sys.argv[2]
        commmits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        response = requests.get(commmits_url)
        json_obj = response.json()
        for i, obj in enumerate(json_obj):
            if i == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print(f"{obj.get('sha')}: {name}")
    except ValueError as invalid_json:
        pass
