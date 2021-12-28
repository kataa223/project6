# ------------------------------------------------------------------
# 課題6-2：任意のキーワードで検索したときの、商品名と価格の一覧を取得
# ------------------------------------------------------------------
import sys
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import fire

RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = os.getenv('RAKUTEN_API_KEY')

def main(keyWord):
    payload = {
        'applicationId': APP_ID,
        'hits': 30,                 # 一度のリクエストで返してもらう最大個数（MAX30)
        'keyword': keyWord ,        # 検索するキーワード
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

    counter = 0
    for i in resp['Items']:
        counter = counter + 1
        item = i['Item']
        print("-------------------------------------------")
        print('【No.】'+ str(counter))
        print('【Name】' + item['itemName'])
        print('【Price】' + '¥' +str(item['itemPrice']))


if __name__ == "__main__":
    fire.Fire(main)