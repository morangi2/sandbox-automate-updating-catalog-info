#!/usr/bin/env python3

import os
import requests

fruit_dict = []
fruit_dict_keys = ["name", "weight", "description", "image_name"]
host_url = "http://[linux-instance-external-IP]/fruits/"
file_src_dir = "supplier-data/descriptions"

#instructions
# List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
# HINT: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.

#capture list of files
files = os.listdir(file_src_dir)

#read file lines into a list
def readeachfile(file):
    with open(file_src_dir + "/" + file) as f:
        lines = f.read().strip().splitlines() #REM split first, the splitlines
    return lines

#load feedback entries into dctionary
for file in files:
    lines = readeachfile(file)
    print(lines) #prints all the lines
    # A- change weight into an int
    weight_str, lbs = lines[1].split()
    weight_int = int(weight_str)
    lines[1] = weight_int

    # B- add value to key image_name
    filename, ext = os.path.splitext(file)
    image_name = filename + ".jpeg"
    lines.append(image_name)

    # C- append each file details to the fruit dictionary
    fruit_dict.append(dict(zip(fruit_dict_keys, lines)))

#post feedback entries
for eachentry in fruit_dict:
    response = requests.post(host_url, data = eachentry)
    if response.ok:
        print("SUCCESS!")
    else:
        print("Error! " + response.status_code)
