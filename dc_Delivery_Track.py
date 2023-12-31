import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd
import config
headers=config.cookies

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
        'entity': 'CARD_DELIVERY_TRACKING',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        if dbInfo:
            return dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)

csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/card_id_input_received.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/output_rcvbyuser.csv"

data = pd.read_csv(csv_input_path, usecols=['card_id'])
card_results = []

def append_to_results(card_id, db_info):
    row = []
    row.append(db_info.get('cardId'))
    row.append(db_info.get('createdAt'))
    row.append(db_info.get('state'))
    row.append(db_info.get('updatedAt'))
    card_results.append(row)

count = 0
try:
    for card_id in data['card_id']:
        try:
            print("Attempting to get card creation request details for card ID:", card_id)
            db_info = getCardCreationRequest(card_id)
            append_to_results(card_id, db_info)
        except Exception as e:
            print("Exception when processing card ID:", card_id, e)
            append_to_results(card_id, {})
        time.sleep(2)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['cardId', 'createdAt', 'state', 'updatedAt'])
df.to_csv(csv_output_path, index=False)