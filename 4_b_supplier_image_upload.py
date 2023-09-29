#!/usr/bin/env python3

import requests
import os

up_url = "http://localhost/upload/"
from_url = "supplier-data/images"

for image in os.listdir(from_url):
    f, e = os.path.splitext(image)
    if e == ".jpeg":
        image_url = from_url + "/" + image
        with open (image_url, "rb") as opened:
            r = requests.post(up_url, files={"file": opened})
