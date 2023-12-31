import requests
import json
import time
import pandas as pd
import logging
import base64
import config

# Access the cookies from the config module
headers = config.cookies

# Configure logging
#logging.basicConfig(filename='api_log.txt', level=logging.INFO)

# Function to make API request and handle errors
def get_cc_onboarding_details(actor_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"

    params = {
        'service': 'FIREFLY',
        'entity': 'CARD_REQUEST',
        'options': [
            {
                'name': 'actor_id',
                'value': base64.urlsafe_b64encode(str(actor_id).encode("utf-8")).decode("utf-8"),
                'type': 1,
            },
            {
                'name': 'workflow',
                'value': 'CARD_REQUEST_WORKFLOW_TYPE_CARD_ONBOARDING',
                'type': 1,
            },
        ],
        'monorailId': '1',
    }

    try:
        print(actor_id)

        r = requests.get(url, headers=config.cookies, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        data = r.json()["dbInfo"][0]
        print(dbInfo)
        return data
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for ref_id: {actor_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for ref_id: {actor_id}. Error: {ke}')

# Read the CSV data with 'actor_id' and 'ticket' columns
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/input_onboarding.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/output_onbrd.csv"
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(actor_id, dbInfo):
    if dbInfo:
        card_id = dbInfo.get('card_id', 'N/A')
        card_req_id = dbInfo.get('id', 'N/A')
        created_at = dbInfo.get('created_at', 'N/A')
        card_limit = dbInfo.get('request_details', {}).get('cardOnboardingDetails', {}).get('cardLimit', {}).get('units', 'N/A')
        selected_reward_type = dbInfo.get('request_details', {}).get('selectedRewardType', 'N/A')
        status = dbInfo.get('status', 'N/A')
    else:
        card_id, card_req_id, created_at, card_limit, selected_reward_type, status = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'

    row = [actor_id, card_id, card_req_id, created_at, selected_reward_type, card_limit, status]
    card_results.append(row)
    logging.info(f"Appended row: {row}")

# Loop through the CSV data and make API requests
count = 0
try:
    for index, row in data.iterrows():
        actor_id = row['actor_id']
        logging.info(f"Attempting to get card creation request details for actor_id: {actor_id}")
        dbInfo = get_cc_onboarding_details(actor_id)
        logging.info(f"API Response for {actor_id}: {dbInfo}")
        append_to_results(actor_id, dbInfo)
        time.sleep(3)
        count += 1
    logging.info("Completed")
except Exception as e:
    logging.error(f'Exception at count: {count}, Error: {e}')

# Save the results to a CSV file
df = pd.DataFrame(card_results, columns=['actor_id', 'card_id', 'card_req_id', 'created_at', 'selectedRewardType', 'cardLimit', 'status'])
df.to_csv(csv_output_path, index=False)
