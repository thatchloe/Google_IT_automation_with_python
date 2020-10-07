# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:31:08 2020


"""

import requests
import os
import json

url = "http://127.0.0.1:80/fruits/"
basepath_descriptions = os.path.expanduser('~') + "/supplier-data/descriptions/"

list_text_files = os.listdir(basepath_descriptions)


for f in list_text_files:
      with open(basepath_descriptions + f, 'r') as opened:
          name = os.path.splitext(f)[0]
          data = opened.read()
          data = data.split('\n')
          dic = {"name": data[0], "weight": int(data[1].strip("lbs")), 
                 "description": data[2], "image_name": name + ".jpeg"}
          response = requests.post(url, json=dic)
          response.raise_for_status()
            