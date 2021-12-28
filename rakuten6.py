# ------------------------------------------------------------------
# 課題6-6：楽天APIにより取得したランキングをスプレッドシートへ出力する
# ------------------------------------------------------------------
import sys
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
load_dotenv()
import os
import fire

# 接続情報など
SHEET_NAME = 'test'
APP_ID = os.getenv('RAKUTEN_API_KEY')
SPREADSHEET_KEY_PATH = 'D:/Python/project6/key/thematic-cursor-336014-0b37a4afb843.json'
RAKUTEN_API_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'

# スプレッドシートへの出力機能
def write_spreadsheet(vlist):
    # スプレッドシートとの接続
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SPREADSHEET_KEY_PATH, scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open(SHEET_NAME).sheet1

    # スプレッドシートの読み書き
    sell_last = 'A' + str(len(vlist))
    range = worksheet.range(f'A1:{sell_last}')

    idx=0
    for val in vlist :
        range[idx].value = val
        idx+=1
        
    worksheet.update_cells(range)
  
  
# ランキング取得機能
def get_ranking(genreId):
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

    result = []
    for items in resp['Items']:
        item = items['Item']
        result.append("-------------------------------------------")
        result.append('【rank】' + str(item['rank']))
        result.append('【itemName】' + item['itemName'])
        result.append('【itemCode】' + item['itemCode']) 
    return result


def main(genreId):
    # ランキングを取得
    ranking = get_ranking(genreId)
    # スプレッドシートに取得結果を出力
    write_spreadsheet(ranking)
        
        
if __name__ == "__main__":
    fire.Fire(main)
    