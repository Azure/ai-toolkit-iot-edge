import base64
import json
import importlib
import requests
locals().update(importlib.import_module("webserviceparams").__dict__)

# read input image
im = './sampletestimages/0.png'    
with open(im, 'rb') as file:
  encoded = base64.b64encode(file.read())

# prepared the payload and header
payload = []
payload.append("{}".format(encoded))
reqStr = json.dumps(payload)
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ apikey)}

# score the images using the REST API
resp = requests.post(scoringurl, data=reqStr, headers=headers)
print(resp.text)
