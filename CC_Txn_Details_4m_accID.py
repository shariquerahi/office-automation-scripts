import requests
import json
import pandas as pd
import time
import base64
import config

# Access the cookies from the config module
headers = config.cookies

def getCardCreationRequest(account_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'account_id',
            'value': str(base64.urlsafe_b64encode(account_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params = {
        'service': 'FIREFLY',
        'entity': 'CARD_TRANSACTION',
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



csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/account_input.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/OUtput_5430013524.csv"

data = pd.read_csv(csv_input_path, usecols=['account_id'])
card_results = []

def append_to_results(transaction):
    row = [
        transaction.get('id'),
        transaction.get('account_id'),
        json.dumps(transaction.get('beneficiary_info')),
        transaction.get('external_txn_id'),
        transaction.get('transaction_authorization_status'),
        transaction.get('txn_category'),
        transaction.get('txn_origin'),
        transaction.get('txn_reference_no'),
        transaction.get('txn_status'),
        transaction.get('txn_time'),
        transaction.get('updated_at'),
        transaction.get('vendor_ext_txn_id')
    ]
    card_results.append(row)

count = 0
try:
    for account_id in data['account_id']:
        try:
            print("Attempting to get card creation request details for card ID:", account_id)
            db_info = getCardCreationRequest(account_id)
            for transaction in db_info:
                append_to_results(transaction)
        except Exception as e:
            print("Exception when processing card ID:", account_id, e)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=[
    'id', 'account_id', 'beneficiary_info', 'external_txn_id', 'transaction_authorization_status',
    'txn_category', 'txn_origin', 'txn_reference_no', 'txn_status', 'txn_time', 'updated_at', 'vendor_ext_txn_id'
])
df.to_csv(csv_output_path, index=False)
