# ------------------------------------------------------------------
# 課題6-1：楽天APIを実行して結果が返ってくることを確認する
# ------------------------------------------------------------------
import sys
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import fire

APP_ID = os.getenv('RAKUTEN_API_KEY')
RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'

def main(shopCode):
    payload = {
        'applicationId': APP_ID,
        'hits': 30,                 # 一度のリクエストで返してもらう最大個数（MAX30)
        'shopCode': shopCode ,      # ショップCode
        'page':1,                   # 何ページ目か
        'postageFlag':1,            # 送料込みの商品に限定
        }
    r = requests.get(RAKUTEN_API_URL, params=payload)
    try:
        r.raise_for_status()
    except Exception as e:
        print(f'APIエラー: detail={e}')
        return None
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
        
        
if __name__ == "__main__":
    fire.Fire(main)