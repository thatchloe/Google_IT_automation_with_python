# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:03:11 2020


"""

#!/usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"
path = os.path.expanduser('~') + "/supplier-data/images/"

 
for image in os.listdir(path):
  if image.endswith(".jpeg"):
    with open(path + image, 'rb') as file:
      r = requests.post(url, files={'file': file})