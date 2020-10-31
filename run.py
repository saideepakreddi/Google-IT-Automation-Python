#!/usr/bin/env python3
import os 
import requests

path = "supplier-data/descriptions/"
texts = os.listdir(path)

url = "http://localhost/fruits/"

for text in texts:
	if file.endswith("txt"):
		with open(path+text,'r') as f:
			data = f.read()
			data = data.split("\n")
			weight = int(data[1].strip(" lbs"))
			image_name = os.path.splitext(text)[0] + ".jpeg"
			dict = {"name" : data[0], "weight" : weight, "description" : data[2], "image_name" : image_name}
			response = requests.post(url, json=dict)
			
			response.raise_for_status()        
        	print(response.status_code)
