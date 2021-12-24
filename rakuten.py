# ------------------------------------------------------------------
# 課題6-1：楽天APIを実行して結果が返ってくることを確認する
# ------------------------------------------------------------------
import sys
import requests

APP_ID = '###'
RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'

args = sys.argv
shopName = args[1]

payload = {
    'applicationId': APP_ID,
    'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
    'shopCode': shopName ,#ショップID
    'page':1,#何ページ目か
    'postageFlag':1,#送料込みの商品に限定
    }
r = requests.get(RAKUTEN_API_URL, params=payload)
resp = r.json()
total = int(resp['count'])
Max = total/30 + 1
print("【num of item】",total)
print("【num of page】",Max)
print("===================================")

counter = 0
for i in resp['Items']:
    counter = counter + 1
    item = i['Item']
    name = item['itemName']
    print('【No.】'+ str(counter))
    print('【Name】' + str(name[:30]))
    print('【Price】' + '¥' +str(item['itemPrice']))
    print('【URL】',item['itemUrl'])
    print('【shop】',item['shopName'])
    print('【text】', item['itemCaption'])