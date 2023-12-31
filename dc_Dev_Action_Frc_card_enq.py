import requests
import pandas as pd
import time

def force_card_creation_enquiry(card_id, reason):
    url = "https://sherlock.epifi.in/api/v1/dev-actions/execute"
    headers = {
        'Cookie': '_csrf=kHlfPOnhqdhYAqX1Z4rKu_Zo; auth_version=v2;',
        'Host': 'sherlock.epifi.in',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'csrf-token': 'q8jRMf1c-VXfKpUCkmCoQjA_1qrxiwFR6E8g',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Language': 'en',
    }
    body = {
        'monorailId': '1',
        'parameters': [
            {'name': 'card_id', 'value': str(card_id), 'type': 1},
            {'name': 'reason', 'value': str(reason), 'type': 100},
        ],
        'action': 'FORCE_CARD_CREATION_ENQUIRY'
    }
    try:
        r = requests.post(url, headers=headers, json=body, timeout=40)
        if r.status_code == 200:
            return r.json()["executeInfo"]["savingsLedgerRecon"]["status"]
    except Exception as e:
        raise Exception('Force process order API call failed', r.status_code, r.text, e)

csv_name = "/Users/ashwinkonaje/Downloads/Scripts/DevActions/ForceTriggerRecon/input.csv"
data = pd.read_csv(csv_name, usecols=['card_id', 'REASON'])

for index, row in data.iterrows():
    card_id, reason = row['card_id'], row['REASON']
    print('card_id:', card_id)
    print('reason:', reason)
    print("Attempting to trigger force recon for account id -->", card_id)
    status = force_card_creation_enquiry(card_id, reason)
    if status:
        print('Status:', status)
    print('-----------------------')
    time.sleep(5)
