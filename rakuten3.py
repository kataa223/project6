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

url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
payload = {
    'applicationId': 1056775690377075202,
    'keyword': keyWord ,#検索するキーワード
    }
r = requests.get(url, params=payload)
resp = r.json()

counter = 0
for products in resp['Products']:
    counter = counter + 1
    product = products['Product']
    print("-------------------------------------------")
    print('【No.】'+ str(counter))
    print('【productName】' + product['productName'])
    print('【productNo】' + product['productNo'])
    print('【maxPrice】' + '¥' +str(product['maxPrice']))
    print('【minPrice】' + '¥' +str(product['minPrice']))