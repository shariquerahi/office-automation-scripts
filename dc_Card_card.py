import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd
import config
# Access the cookies from the config module
headers = config.cookies 

# ... (Previous code remains the same)

def getCardCreationRequest(card_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'card_id',
            'value': str(base64.urlsafe_b64encode(card_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service': 'CARD',
        'entity': 'CARD',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        return dbInfo  # Add this line to return the dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)

# ... (Rest of the code remains the same)


csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/card_id_data_input.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/card_details_output.csv"

data = pd.read_csv(csv_input_path, usecols=['card_id'])
card_results = []

def append_to_results(card_id, dbinfo):
    row = []
    row.append(dbinfo.get('actorId'))
    row.append(dbinfo.get('cardId'))
    row.append(dbinfo.get('cardForm'))
    
    row.append(dbinfo.get('state'))
    row.append(dbinfo.get('cardInfo'))
    row.append(dbinfo.get('cardInfo', {}).get('maskedCardNumber', 'N/A'))
    row.append(dbinfo.get('cardInfo', {}).get('expiry', 'N/A'))
    #masked_card_number = dbinfo.get('cardInfo', {}).get('maskedCardNumber', 'N/A')
    #expiry = dbinfo.get('cardInfo', {}).get('expiry', 'N/A')
    card_results.append(row)

count = 0
try:
    for card_id in data['card_id']:
        try:
            print("Attempting to get card creation request details for card_id:", card_id)
            dbinfo = getCardCreationRequest(card_id)
            append_to_results(card_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", card_id, e)
            append_to_results(card_id, {})
        time.sleep(1)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['actorId','cardId','cardForm','state','cardInfo','maskedCardNumber','expiry'])
df.to_csv(csv_output_path, index=False)