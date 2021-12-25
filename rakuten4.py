# ------------------------------------------------------------------
# 課題6-4：楽天APIにより取得したランキング一覧をcsv出力する
# ------------------------------------------------------------------
import csv
import sys
import requests

RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
APP_ID = '###'

args = sys.argv
genreId = args[1]

payload = {
    'applicationId': APP_ID,
    'genreId': genreId ,#ジャンルID
    }
r = requests.get(RAKUTEN_API_URL, params=payload)
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

