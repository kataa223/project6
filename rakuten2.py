# 課題6-2：任意のキーワードでAPI検索した場合

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
keyWord = args[1]

url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
payload = {
    'applicationId': 1056775690377075202,
    'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
    'keyword': keyWord ,#検索するキーワード
    'page':1,#何ページ目か
    'postageFlag':1,#送料込みの商品に限定
    }
r = requests.get(url, params=payload)
resp = r.json()

counter = 0
for i in resp['Items']:
    counter = counter + 1
    item = i['Item']
    print("-------------------------------------------")
    print('【No.】'+ str(counter))
    print('【Name】' + item['itemName'])
    print('【Price】' + '¥' +str(item['itemPrice']))