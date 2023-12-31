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

def getCardCreationRequest(actor_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'actor_id',
            'value': str(base64.urlsafe_b64encode(actor_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params = {
        'service': 'CARD',
        'entity': 'CARDS_FOR_ACTOR',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for actor_id: {actor_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for actor_id: {actor_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Downloads/Invalid_CVV_dTAILS.csv"
csv_output_path = "/Users/shariquerahi/Downloads/output_invalid_id.csv"

# Read the CSV data with 'actor_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(actor_id, dbinfo):
    if dbinfo:
        card_id = dbinfo.get('card_id')
        state = dbinfo.get('state')
        card_form = dbinfo.get('card_form')
        bank_identifier = dbinfo.get('bank_identifier', 'N/A')
        masked_card_number = dbinfo.get('card_info', {}).get('masked_card_number', 'N/A')
    else:
        card_id, state, card_form, bank_identifier, masked_card_number = None, None, None, 'N/A', 'N/A'

    row = [actor_id, card_id,state, card_form, bank_identifier, masked_card_number]
    card_results.append(row)
    print(f"Appended row: {row}")


# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        actor_id = row['actor_id']
        try:
            print("Attempting to get card creation request details for actor_id:", actor_id)
            dbinfo = getCardCreationRequest(actor_id)
            print(f"API Response for {actor_id}: {dbinfo}")
            append_to_results(actor_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", actor_id, e)
            append_to_results(actor_id, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['actor_id', 'cardId','state','card_form','bank_identifier','masked_card_number'])
print("DataFrame before saving to CSV:")
print(df)
df.to_csv(csv_output_path, index=False)


