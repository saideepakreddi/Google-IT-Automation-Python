#!/usr/bin/env python3
from PIL import Image
import os

path = "supplier-data/images/"
images = os.listdir(path) #lists the image names in that directory
for image in images:
	if 'tiff' in pic:
		filename = os.path.splitext(image)[0] #splitting into extenstion for a file name, if 007.tiff is the file name, 007 store in [0] as root and .tiff is stored in [1] as its extension
		output = path + filename + ".jpeg"  #changing the image format
		Image.open(path + image).convert("RGB").resize((600,400)).save(output,"JPEG") #open image and resize and save it to jpeg format inthe same dir
