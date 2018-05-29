#coding:utf-8

import requests
import json


with open("tt.json","r")as f:
    aa = json.load(f)
    
print(aa["sign"])