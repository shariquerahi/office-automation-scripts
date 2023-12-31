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
        'entity': 'DC_FOREX_TXN_REFUND',
        'options': json_dump,
        'monorailId': '1',
    }
    '''r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        if dbInfo:
            return dbInfo
    except Exception as e
        raise Exception('API call failed', r.status_code, r.text, e)  '''
    
    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"]
        return dbInfo
    except requests.exceptions.RequestException as re:
        print(f'API call failed for card_id: {actor_id}. Error: {re}')
        return None  # Return None to indicate the error condition
    except requests.exceptions.HTTPError as he:
        if he.response.status_code == 500:
            print(f"Received a 500 Internal Server Error for card_id: {actor_id}")
            return None  # Return None to indicate the error condition
        else:
            raise  # Re-raise other HTTP errors
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {actor_id}. Error: {ke}')
    
def append_to_results(ticket, actor_id, status, dbinfo_list):
    for dbinfo in dbinfo_list:
        if isinstance(dbinfo, dict):
            txn_id = dbinfo.get('txn_id', 'N/A')
            txn_time = dbinfo.get('txn_time', 'N/A')
            txn_time_user_tier = dbinfo.get('txn_time_user_tier', 'N/A')
            total_txn_amount = dbinfo.get('total_txn_amount', {}).get('units', 'N/A')
            refund_status = dbinfo.get('refund_status', 'N/A')
            refund_sub_status=dbinfo.get('refund_sub_status', 'N/A')
            #refund_amount = dbinfo.get('refund_amount', {}).get('units', 'N/A')
            refund_info = dbinfo.get('refund_amount', {})
            if refund_info:
                refund_amount = refund_info.get('units', 'N/A')
            else:
                refund_amount = 'N/A'
            forexChargeAmount = json.dumps(dbinfo.get('forex_charges_info', {}))
            created_at = dbinfo.get('created_at', 'N/A')
            updated_at = dbinfo.get('updated_at', 'N/A')
        else:
            print(f"API response not as expected for actor ID {actor_id}: {dbinfo}")
            txn_id, txn_time, status,txn_time_user_tier, total_txn_amount, refund_status, refund_sub_status,refund_amount, forexChargeAmount, created_at, updated_at = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'

        row = [ticket,actor_id,status, txn_id, txn_time, txn_time_user_tier, total_txn_amount,
               refund_status,refund_sub_status, refund_amount, forexChargeAmount, created_at, updated_at]
        card_results.append(row)
    
'''def append_to_results(ticket, actor_id, status, dbinfo):
    for dbinfo_item in dbinfo_list:
        if dbinfo_item is None:
            print(f"DB info is None for ticket ID {ticket}, actor_id: {actor_id}")
            continue

        if isinstance(dbinfo_item, dict):
            txn_id = dbinfo_item.get('txn_id', 'N/A')
            txn_time = dbinfo_item.get('txn_time', 'N/A')
            txn_time_user_tier = dbinfo_item.get('txn_time_user_tier', 'N/A')
            total_txn_amount = dbinfo_item.get('total_txn_amount', {}).get('units', 'N/A')
            refund_status = dbinfo.get('refund_status', 'N/A')
            refund_info = dbinfo_item.get('refund_amount', {})
            if refund_info:
                refund_amount = refund_info.get('units', 'N/A')
            else:
                refund_amount = 'N/A'
            forexChargeAmount = json.dumps(dbinfo_item.get('forex_charges_info', {}))
            created_at = dbinfo_item.get('created_at', 'N/A')
            updated_at = dbinfo_item.get('updated_at', 'N/A')
        else:
            print(f"API response not as expected for ticket ID {ticket}: {dbinfo_item}")
            txn_id, txn_time, txn_time_user_tier, total_txn_amount, refund_status, refund_amount, forexChargeAmount, created_at, updated_at = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'

        row = [ticket, actor_id, status, txn_id, txn_time, txn_time_user_tier, total_txn_amount,
               refund_amount, forexChargeAmount, created_at, updated_at]
        card_results.append(row)'''


'''def append_to_results(ticket, actor_id, status, dbinfo):
    for dbinfo in dbinfo:
        if dbinfo is None:
            print(f"DB info is None for ticket ID {ticket}, actor_id: {actor_id}")
            continue
        
        if isinstance(dbinfo, dict):
            txn_id = dbinfo.get('txn_id', 'N/A')
            txn_time = dbinfo.get('txn_time', 'N/A')
            txn_time_user_tier = dbinfo.get('txn_time_user_tier', 'N/A')
            total_txn_amount = dbinfo.get('total_txn_amount', {}).get('units', 'N/A')
            refund_status = dbinfo.get('refund_status', 'N/A')
            #refund_amount = dbinfo.get('refund_amount', {}).get('units', 'N/A')
            refund_amount = dbinfo.get('refund_amount', {}).get('units', 'N/A')
            forexChargeAmount = json.dumps(dbinfo.get('forex_charges_info', {}))
            created_at = dbinfo.get('created_at', 'N/A')
            updated_at = dbinfo.get('updated_at', 'N/A')
        else:
            print(f"API response not as expected for ticket ID {ticket}: {dbinfo}")
            txn_id, txn_time, txn_time_user_tier, total_txn_amount, refund_status, refund_amount, forexChargeAmount, created_at, updated_at = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'

        row = [ticket, actor_id, status, txn_id, txn_time, txn_time_user_tier, total_txn_amount,
               refund_status, refund_amount, forexChargeAmount, created_at, updated_at]
        card_results.append(row) '''



'''def append_to_results(ticket, actor_id, status, dbinfo_list):
    for dbinfo in dbinfo_list:
        if isinstance(dbinfo, dict):
            txn_id = dbinfo.get('txn_id', 'N/A')
            txn_time = dbinfo.get('txn_time', 'N/A')
            txn_time_user_tier = dbinfo.get('txn_time_user_tier', 'N/A')
            total_txn_amount = dbinfo.get('total_txn_amount', {}).get('units', 'N/A')
            refund_status = dbinfo.get('refund_status', 'N/A')
            #refund_amount = dbinfo.get('refund_amount', {}).get('units', 'N/A')
            refund_amount = dbinfo.get('refund_amount', {}).get('units', 'N/A')
            forexChargeAmount = json.dumps(dbinfo.get('forex_charges_info', {}))
            created_at = dbinfo.get('created_at', 'N/A')
            updated_at = dbinfo.get('updated_at', 'N/A')
        else:
            print(f"API response not as expected for ticket ID {ticket}: {dbinfo}")
            txn_id, txn_time, txn_time_user_tier, total_txn_amount, refund_status, refund_amount, forexChargeAmount, created_at, updated_at = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'

        row = [ticket, actor_id, status, txn_id, txn_time, txn_time_user_tier, total_txn_amount,
               refund_status, refund_amount, forexChargeAmount, created_at, updated_at]
        card_results.append(row)'''


csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/input_Forex_ticket.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/DC_PythonScript/DC_Output.csv"

data = pd.read_csv(csv_input_path, usecols=['ticket'])
card_results = []

    

# Loop through ticket IDs and retrieve information
for ticket in data['ticket']:
    print(f"Retrieving information for ticket ID {ticket}...")
    actor_id, status = getTicketDetails(ticket)
    time.sleep(3)
    dbinfo = getCardCreationRequest(actor_id) if actor_id else 'NA'
    # Retrieve dbinfo1 after retrieving dbinfo
    
    append_to_results(ticket, actor_id, status, dbinfo)
    time.sleep(4)

# Write results to output CSV file
df = pd.DataFrame(card_results, columns=['ticket_id', 'actor_id','status', 'txn_id', 'txn_time', 'txn_time_user_tier','total_txn_amount','refund_status','refund_sub_status','refund_amount','forexChargeAmount', 'created_at','updated_at'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
