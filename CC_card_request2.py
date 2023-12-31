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
cookies = {
}
# ... (Previous code remains the same)

def getTicketDetails(ticketid):
    url = f'https://sherlock.epifi.in/api/v1/ticket-summary/{ticketid}'
    r = requests.get(url, headers=headers,cookies=cookies)
    try:
       time.sleep(3)
       ticketInfo=r.json()["ticketInfo"]
       if ticketInfo:
           actor_id=ticketInfo.get("actorId")
       return actor_id     #ticketInfo.get("actorId"),ticketInfo.get("status")
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

def getCC_CardRequests(actor_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'actor_id',
            'value': str(base64.urlsafe_b64encode(actor_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
        {
            'name': 'workflow',
            'value': 'CARD_REQUEST_WORKFLOW_TYPE_CARD_ONBOARDING',           #'CARD_REQUEST_WORKFLOW_TYPE_CARD_ONBOARDING',
            'type': 5,
        }
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service': 'FIREFLY',
        'entity': 'CARD_REQUEST',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo  # Add this line to return the dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)
    
# ... (Rest of the code remains the same)


csv_input_path = "/Users/shariquerahi/Downloads/printing-delay-2023-10-25.csv"
csv_output_path = "/Users/shariquerahi/Downloads/output_card_request.csv"

data = pd.read_csv(csv_input_path, usecols=['ticket'])
card_results = []

def append_to_results(ticket,dbinfo):
    if dbinfo:  # Check if the response is not empty
        actor_id=dbinfo.get('actor_id','N/A')

        card_results.append(dbinfo)

count = 0
try:
    for actor_id in data['ticket']:
        try:
            actor_id = getTicketDetails(ticket)
            print("Attempting to get card creation request details for actor_id:", ticket)
            dbinfo = getCC_CardRequests(actor_id)
            append_to_results(dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", actor_id, e)
        time.sleep(1)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)
   

# Create a DataFrame from the list of results
df = pd.DataFrame(card_results)

# Write the DataFrame to the output CSV file
df.to_csv(csv_output_path, index=False)