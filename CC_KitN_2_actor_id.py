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


def getCardCreationRequest(vendor_identifier):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'vendor_identifier',
            'value': base64.urlsafe_b64encode(str(vendor_identifier).encode("utf-8")).decode("utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service': 'FIREFLY',
        'entity': 'CREDIT_CARD',
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


csv_input_path = "/Users/shariquerahi/Downloads/Invalid_CVV_dTAILS.csv"
csv_output_path = "/Users/shariquerahi/Downloads/output_invalid_id.csv"

data = pd.read_csv(csv_input_path, usecols=['vendor_identifier'])
card_results = []

def append_to_results(vendor_identifier, dbinfo):
    row = []
    row.append(dbinfo.get('actor_id'))
    row.append(dbinfo.get('vendor_identifier'))
    card_results.append(row)

count = 0
try:
    for vendor_identifier in data['vendor_identifier']:
        try:
            print("Attempting to get card creation request details for vendor_identifier:", vendor_identifier)
            dbinfo = getCardCreationRequest(vendor_identifier)
            append_to_results(vendor_identifier, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", vendor_identifier, e)
            append_to_results(vendor_identifier, {})
        time.sleep(2)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['actor_id', 'vendor_identifier'])
df.to_csv(csv_output_path, index=False)