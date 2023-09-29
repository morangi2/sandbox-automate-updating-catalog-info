#!/usr/bin/env python3

from PIL import Image
import os

images_folder = "supplier-data/images"

for oldimage in os.listdir(images_folder):
    f, e = os.path.splitext(oldimage)
    if e == ".tiff":
        newimage = f + ".jpeg"

        with Image.open(images_folder + "/" + oldimage) as im:
            im = im.convert("RGB")
            im.resize((600,400)).save(images_folder + "/" + newimage)
           