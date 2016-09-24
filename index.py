#!/usr/bin/env python

print("Content-type: text/html\r\n")
import requests
import pymongo
import json, ast
from pymongo import MongoClient
from bson import BSON
from bson import json_util


response = requests.get('http://maps.google.com/maps/api/geocode/json?address=moshi')

if response.status_code == 200:
    print  "Success..."
else:
    print response.status_code


# Now fetching values from DBS
try:
  client = MongoClient('mongodb://localhost:27017/')
  db = client.nbot    
except:
  print('Error: Unable to connect with database')
  client = None

try:
  cursor = db.nbot.find()
  if client is not None:
    for document in cursor:
      print json.dumps(document, sort_keys=True, indent=4, default=json_util.default)
except:
  print  'Collection Fetch Error!!!'
