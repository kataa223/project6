# ------------------------------------------------------------------
# 課題6-6：楽天APIにより任意の商品の最安値と最高値を取得する
# ------------------------------------------------------------------
import sys
import requests

RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
APP_ID = '###'

args = sys.argv
keyWord = args[1]

payload = {
    'applicationId': APP_ID,
    'keyword': keyWord ,#検索するキーワード
    }
r = requests.get(RAKUTEN_API_URL, params=payload)
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