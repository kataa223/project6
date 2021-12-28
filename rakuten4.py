# ------------------------------------------------------------------
# 課題6-4：楽天APIにより取得したランキング一覧をcsv出力する
# ------------------------------------------------------------------
import csv
import sys
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import fire

APP_ID = os.getenv('RAKUTEN_API_KEY')
RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'

def main(arg1):
    genreId = arg1

    payload = {
        'applicationId': APP_ID,
        'genreId': genreId ,        # ジャンルID
        }
    r = requests.get(RAKUTEN_API_URL, params=payload)
    try:
        r.raise_for_status()
    except Exception as e:
        print(f'APIエラー: detail={e}')
        return None
    resp = r.json()

    result = ""
    for items in resp['Items']:
        item = items['Item']
        result += "-------------------------------------------\n"
        result += '【rank】' + str(item['rank']) + "\n"
        result += '【itemName】' + item['itemName'] + "\n"
        result += '【itemCode】' + item['itemCode'] + "\n"

    # csv出力
    with open("ranking.csv", "a", encoding="utf-8") as f:
        f.write(f',{result}')


if __name__ == "__main__":
    fire.Fire(main)