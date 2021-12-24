# ------------------------------------------------------------------
# 課題6-2：任意のキーワードで検索したときの、商品名と価格の一覧を取得
# ------------------------------------------------------------------
import sys
import requests

RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = '###'

args = sys.argv
keyWord = args[1]

url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
payload = {
    'applicationId': APP_ID,
    'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
    'keyword': keyWord ,#検索するキーワード
    'page':1,#何ページ目か
    'postageFlag':1,#送料込みの商品に限定
    }
r = requests.get(RAKUTEN_API_URL, params=payload)
resp = r.json()

counter = 0
for i in resp['Items']:
    counter = counter + 1
    item = i['Item']
    print("-------------------------------------------")
    print('【No.】'+ str(counter))
    print('【Name】' + item['itemName'])
    print('【Price】' + '¥' +str(item['itemPrice']))