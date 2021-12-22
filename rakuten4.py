# 課題6-4 ランキング

#coding:utf-8
import csv
import sys
import codecs
import math
import random
import requests
from time import sleep
import re

args = sys.argv
genreId = args[1]

url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
payload = {
    'applicationId': 1056775690377075202,
    'genreId': genreId ,#ジャンルID
    }
r = requests.get(url, params=payload)
resp = r.json()

counter = 0
for items in resp['Items']:
    item = items['Item']
    print("-------------------------------------------")
    print('【rank】' + str(item['rank']))
    print('【itemName】' + item['itemName'])
    print('【itemCode】' + item['itemCode'])
    
    
