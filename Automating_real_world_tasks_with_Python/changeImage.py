# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/env python3
from PIL import Image
import  os
path = os.path.expanduser('~') + '/supplier-data/images/'
for image in os.listdir(path):
    if '.tiff' in image and '.' not in image[0]:
        img = Image.open(path + image)
        img.convert("RGB").resize((600,400)).save(path + image.split('.')[0] + '.jpeg', "JPEG")
        img.close()