import requests
import json
import base64
import time
import pandas as pd
import config
import sys

# Access the cookies from the config module
headers = config.cookies
results = []  # Initialize results list

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
    params = {
        'service': 'CARD',
        'entity': 'CARD',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        actor_id = dbInfo.get('actorId')  # Add this line to get the actor_id
        return actor_id
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)

def getSavingAccountNumber(actor_id,bank_identifier):
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
        'service': 'PAYMENT_INSTRUMENT',
        'entity': 'PAYMENT_INSTRUMENT',
        'options': json_dump,
        'monorailId': '1',
    }

    max_retries = 5  # Maximum number of retries in case of API failure
    retries = 0

    while retries < max_retries:
        try:
            r = requests.get(url, headers=headers, params=params, timeout=100)
            r.raise_for_status()  # Raises an exception for non-2xx response codes

            op = ''
            dbInfo = r.json().get("dbInfo", [])  # Default to an empty list if 'dbInfo' is not present in the JSON response
            for x in dbInfo:
                if x is not None and x.get("Identifier"):
                    savings = str(x["Identifier"].get("account_type", "")) == 'SAVINGS'
                    type = str(x.get("Type", "")) == 'BANK_ACCOUNT'
                    State = str(x.get("State", "")) == 'VERIFIED'
                    if savings and type and State:
                        op = x.get("Identifier").get("actual_account_number")
                        results.append({'card_id': card_id, 'actor_id': actor_id, 'actual_account_number': op,'bank_identifier':bank_identifier})
                        break  # Since we only need one result, we can break the loop once we find a match
            break  # Exit the loop if the API call is successful
        except (requests.RequestException, KeyError) as e:
            retries += 1
            if retries < max_retries:
                print(f"API call failed. Retrying in 15 seconds... (Retry {retries}/{max_retries})")
                time.sleep(15)
            else:
                raise Exception('API call failed', r.status_code, r.text, e)

csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/Card_id_input.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/account_number_out.csv"

data = pd.read_csv(csv_input_path, usecols=['card_id','bank_identifier'])

for index, row in data.iterrows():
    card_id = row['card_id']
    bank_identifier = row['bank_identifier']
    actor_id = getCardCreationRequest(card_id)
    if actor_id:
        getSavingAccountNumber(actor_id, bank_identifier)
    else:
        print(f"No actor_id found for card_id: {card_id}")



df = pd.DataFrame(results, columns=['card_id', 'bank_identifier','actor_id', 'actual_account_number'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
