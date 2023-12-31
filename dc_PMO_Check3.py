import requests
import time
import pandas as pd
import json
import base64
import config
# Access the cookies from the config module
headers = config.cookies

# HTTP headers and cookies
cookies = {
}
# HTTP headers and cookies
cookies = {
}

# Function to retrieve ticket information
def getTicketDetails(ticketid):
    url = f'https://sherlock.epifi.in/api/v1/ticket-summary/{ticketid}'
    r = requests.get(url, headers=headers,cookies=cookies)
    try:
       time.sleep(3)
       ticketInfo=r.json()["ticketInfo"]
       return ticketInfo.get("actorId"),ticketInfo.get("status")
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

# Function to retrieve card information
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
        print(f'API call failed for card_id: {actor_id}. Error: {re}')
        return None  # Return None to indicate the error condition
    except requests.exceptions.HTTPError as he:
        if he.response.status_code == 500:
            #print(f"Received a 500 Internal Server Error for card_id: {actor_id}")
            return None  # Return None to indicate the error condition
        else:
            raise  # Re-raise other HTTP errors
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {actor_id}. Error: {ke}')
    
    # Function to retrieve card information
    
def getCardCreationRequest_1(card_id):
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
        'entity': 'CARD_CREATION_REQUEST',
        'options': json_dump,
        'monorailId': '1',
    }

    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfoList = r.json().get("dbInfo", [])
        if dbInfoList:
            dbInfo = dbInfoList
            return dbInfo.get("requestId"), dbInfo.get("state"), dbInfo.get("createdAt"),dbInfo.get("updatedAt")
    except requests.exceptions.RequestException as re:
        print(f'API call failed for card_id: {card_id}. Error: {re}')
        return None  # Return None to indicate the error condition
    except requests.exceptions.HTTPError as he:
        if he.response.status_code == 500:
            #print(f"Received a 500 Internal Server Error for card_id: {card_id}")
            return None  # Return None to indicate the error condition
        else:
            raise  # Re-raise other HTTP errors
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')



#added  PHYSICAL_CARD_DISPATCH_REQUESTS

# ... (previous code)

def getCardCreationRequest2(card_id):
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
        'entity': 'PHYSICAL_CARD_DISPATCH_REQUESTS',
        'options': json_dump,
        'monorailId': '1',
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo1 = r.json()["dbInfo"][0]
        return dbInfo1
    except requests.exceptions.RequestException as re:
        print(f'API call failed for card_id: {card_id}. Error: {re}')
        return None  # Return None to indicate the error condition
    except requests.exceptions.HTTPError as he:
        if he.response.status_code == 500:
            print(f"Received a 500 Internal Server Error for card_id: {card_id}")
            return None  # Return None to indicate the error condition
        else:
            raise  # Re-raise other HTTP errors
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')

# ... (rest of the code)
def getCardCreationRequest3(card_id):
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
        'entity': 'CARD_TRACKING_DETAILS',
        'options': json_dump,
        'monorailId': '1',
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        response_data = json.loads(r.text)
        dbInfo = response_data["dbInfo"]
        return dbInfo
    except requests.exceptions.RequestException as re:
        print(f'API call failed for card_id: {card_id}. Error: {re}')
        return None  # Return None to indicate the error condition
    except requests.exceptions.HTTPError as he:
        if he.response.status_code == 500:
            print(f"Received a 500 Internal Server Error for card_id: {card_id}")
            return None  # Return None to indicate the error condition
        else:
            raise  # Re-raise other HTTP errors
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')


# Append retrieved data to results list
def append_to_results(ticket, actor_id, status, dbinfo, dbinfo1,dbInfo2):
    if dbinfo:
        card_id = dbinfo.get('card_id')
        state1 = dbinfo.get('state')
        card_form = dbinfo.get('card_form')
        bank_identifier = dbinfo.get('bank_identifier', 'N/A')
        controls=dbinfo.get('controls', 'N/A')
        #row.append(dbinfo.get('cardInfo', {}).get('maskedCardNumber', 'N/A'))
        #row.append(dbinfo.get('cardInfo', {}).get('expiry', 'N/A'))
        #masked_card_number = dbinfo.get('card_info', {}).get('masked_card_number', 'N/A')

        requestId, state,createdAt,updatedAt = getCardCreationRequest_1(card_id) if card_id else ('N/A', 'N/A','N/A','N/A')
    else:
        card_id, state1, card_form, bank_identifier,controls = None, None, None, 'N/A','N/A'
        requestId, state,createdAt,updatedAt  = 'N/A', 'N/A','N/A','N/A'

    if dbinfo1:
        client_req_id = dbinfo1.get('fund_transfer_client_req_id', 'N/A')
        Physical_requestID = dbinfo1.get('request_id', 'N/A')
        Physical_Card_state = dbinfo1.get('state', 'N/A')
    else:
        client_req_id = 'N/A'
        Physical_requestID = 'N/A'
        Physical_Card_state = 'N/A'
    try:
        print("Original dbinfo2:", dbinfo2)  # Add this line to print dbinfo2
        if dbinfo2: #and "dbInfo" in dbinfo2:  # Check for correct structure
            #dbinfo2_data = dbinfo2["dbInfo"]
            #dbinfo2_data = dbinfo2["dbInfo"]
            awb = dbinfo2.get('awb', 'N/A')
            deliveryState = dbinfo2.get('deliveryState', 'N/A')
            pickupDate = dbinfo2.get('pickupDate', 'N/A')
            createdAt_1=dbinfo2.get('createdAt', 'N/A')
        else:
            awb, deliveryState, pickupDate,createdAt_1 = 'N/A', 'N/A', 'N/A','N/A'
    except Exception as e:
        print(f"Error while processing API response for client_req_id: {client_req_id}. Error: {e}")
        awb, deliveryState, pickupDate,createdAt_1= 'N/A', 'N/A', 'N/A','N/A'
    # Debug print statements
    #print("Extracted values - awb:", awb, "deliveryState:", deliveryState, "pickupDate:", pickupDate)
    row = [ticket, actor_id, status, card_id, state1, card_form, bank_identifier,controls,
           requestId, state, createdAt,updatedAt ,client_req_id, Physical_requestID, Physical_Card_state, awb, deliveryState, pickupDate,createdAt_1]
    results.append(row)


# Set input and output file paths
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/DC_PythonScript/card_crtn_input.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/DC_PythonScript/out_card_crtn.csv"

# Read the input CSV data
data = pd.read_csv(csv_input_path)

# Initialize results list
results = []

# Loop through ticket IDs and retrieve information
for ticket in data['ticket']:
    print(f"Retrieving information for ticket ID {ticket}...")
    actor_id, status = getTicketDetails(ticket)
    time.sleep(3)
    dbinfo = getCardCreationRequest(actor_id) if actor_id else None
    # Retrieve dbinfo1 after retrieving dbinfo
    dbinfo1 = getCardCreationRequest2(dbinfo.get('card_id')) if dbinfo and dbinfo.get('card_id') else None
    # Retrieve dbinfo1 after retrieving dbinfo
    dbinfo2 = getCardCreationRequest3(dbinfo.get('card_id')) if dbinfo and dbinfo.get('card_id') else None
    
    append_to_results(ticket, actor_id, status, dbinfo, dbinfo1,dbinfo2)
    time.sleep(4)

# Write results to output CSV file
df = pd.DataFrame(results, columns=['ticket_id', 'actor_id', 'status', 'card_id', 'state1','card_form', 'bank_identifier','controls','requestId', 'state','createdAt','updatedAt' ,'client_req_id','Physical_requestID','Physical_Card_state','awb','deliveryState','pickupDate','createdAt'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
