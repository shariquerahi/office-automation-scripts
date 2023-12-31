import requests
import time
import pandas as pd
import json
import base64

# HTTP headers and cookies
cookies = {
}
headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_csrf=03uf4ciaTkYLbnJi4-CNhku4; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.hu4pJYWw--lOp_fr05vf7TOaq8YO75IIVHq45XKRhvNWLn9zHGMZM_8v71Ifglh92pB1nGRbZkJFVVGEC_ZyD-_FuoX7VMFraPXDnOsMBZq_9tS8XHTvwufiBwBjH62f0IZzpmVpBowd4ZCROQ7g3LIVggUIErEmuz-0FZCOW2jsnzbH_AUyZMSZ0iEXSZOXL39Xss5uOuam3gHDPEe98HUeIqIxTwZXI9z7kpjS54SDj0xicNE4fZZ0rLiCwarsyNrNA7IdyPhRnhugEqmQ3pJm2Z6FwR1Urj8mq-4XsOZVqXF2qs_1s6vAoa0cJrYyoFh5CNqBXG0nGsHeQLcjOg.hiaj3TVWiJAEzwnr.PpaCHmzlPd3qonkbjWhNRH9iqyCZ3PAmnotiMgBmKJSRDY-4QNCft6eln3yBSpRUOGP_gjCH4lYlodlMjT5f8ltK_vrJW5x6Uwdg2HnjVr56q_2n94AaeyIiV0wqNYuogFwl9z5-x2OIdTMfQXw5o0qxYi7HSCEHsGfy-jRhvgNAssWBW88TdEA8UjcYzElYIOHA4PoLqijQDiOaH6tXYKLIE5_EekYCSCU8HM2bNraXXvWA7xz5mwh32R8tTE_Eqk_QpuA-SsmGriPKNXkMdeCHZX3Tm8maCQI4EPWCsx70CI6OrUGaMeDUcbyx_nKmNojlFmTlEohjr8GTJelm0ao4cYAUJxoQNGhS6jFIoauXF-zSsakgwzqjmdhaoo55n5IuLS5KjPn9QiT0YzV5TImqmFhsUqrc_0m9mP-_sGo1dTGBNI4C90yUESOZV4lA3vRh7W3UPBl7mchg9fxqGkO-HGyUD3G74JnLV-wMVzLDbWH343ePeRKQCTEo0KTDLwIh7hA3lwCpjv7Pn3CnTcukflVkmpENcvkHGLTWQSuHfPx3rZqeaVxu_Ync3vaNuaHQ83-UgDh6rMZbIotxbEJ9nnypO38BRnlOi_fvOYCOLrdtRfrzQffMOhkcj1iEJbp6H5xqSl_VNglf522A9cp0rmoFqmCKLL4WHWRQY8OPUzHxx5JVq9YPeo-jxL3NFfH7Qc_Xi6t2W1YuHskZYZjhhnvutqQpffbHo5x5w0BvdcByRWuf3ZhELyYevk0n9r863XmrUO1oOb1lvRpjDIg5zaF9XXnZC5XsDI2wkW_b-4dLQ4ll2Cq7hS2J8XNjitfROhu3otfMNJ6QbYuBnH5Bq8PClSk0Ws1rr3p1-LdMNuuTROGEZsB2QFB8GTOb8jndQ-JRWgfDJSF-y60YVqUwyF-v__ob2kPww92Y5v3li7rbsloU9wzggng3Ck7gPFGiVHm4AdvrdXDVtwiYXjuyyYtIKdvuYR4lxdnp5bJFhPUT2uGFsqtjrl6RYAVQ2uUx4LuYQxnFHsP3VnGTb0ZE5gRMStg69s7Gbg4VSkWl2MyssEBPAUZ7UkhDLtQ7xomlBiWgFbupDPkaotA6ih2KF91wHw8qfDPJ15yNHggb_C2BbiRe1tg3ApCxqfg7yU1oxQ827ogzlwG0t9J7xqLblryqOY1E6yucCuh7rJRxNeYDJF4aPT368deHBwQFnI5rjkxetP4DQwFnUNiNko7nbcTdLJGTY-nwuFdDhhca2tjDr2vX4oViT5xorrc4kmYROwuheMAaAcCQpg.eeh2luUXcHvsFI9_HhQM-Q; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTE1OTA3MjYsImV4cCI6MTY5MTYwODcxNCwiaWF0IjoxNjkxNjA1MTE0LCJqdGkiOiIyZmRkZWZmZS0yZjQ0LTQ5NzktYTcxMC1lZDlmMzVkMWY1YTIiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.XJdD2TTa3gADsfWH6blXDN7jwBrL6R1qq38UP3AFEX4Z69gpbJ40tSYbFG6xpEC7XdljZwoShRyMAaxFxvSHdywLlY7VmRVV8yhzPxnWCOLODwVRrgbYml8T1hW-4yrY0bFidiB_tu4BboTkg56Adm9OlxNRC_C43bLI-2TCupVzh0jT2R5p3q0h-heiGb_eEJGEjnl4jK5mwUv-R9-BmLepe6gh5h-6NhZJ337QVi-_EF8sgbKdxU3QhFsi_yMCbXVMkF2Qnxob85k5XX99hqh-ii17vpYuLQPkTv13ecQw7_CdPVN57K_fBY2Wz2I-OeaOPLKtecjUJmlgxtFyYA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiSGJ6ZDRjWFNyR3VuT1JPTnY0VjZzZyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTE1OTA3MjYsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkxNjA4NzE0LCJpYXQiOjE2OTE2MDUxMTQsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.X1vjIDhLYQDEeQ98pRRQqGfBODG_V4F5g6Tcrw6UtgbWrkD52njyWw4PlitkgrfmSD-CObBFBRbn4i7JApzSemwJo0r8Nd6_icSb2LXGNlRG65RXnHK5VGjgFNbuZABVngQQAcwSr8f82NblZT1RYPViu2o0I550I45tJpmFS6yplSgLRzbfytSo8F6l21OlhR627C86GG8-zP_lvwatqzerHC5uv_4e0sn-pLV2uA09ta6KYw8XyTYthK2S63vCQ7U3p5uOwkyu3Mm6Psw50nk5UC8ZN6MXgYHcvijrsle2ty1JjtTAzBLN-Qa04zHgl7yZHQAXzst8mWqz7UuCdA',
    'csrf-token': 'fW9y3x2w-HldeBdJczEI3vfRTLGSQOdzCyIY',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'en',
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
        raise Exception(f'API call failed for actor_id: {actor_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for actor_id: {actor_id}. Error: {ke}')
    
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
            return dbInfo.get("requestId"), dbInfo.get("state")
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for card_id: {card_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')


#added  PHYSICAL_CARD_DISPATCH_REQUESTS

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
        raise Exception(f'API call failed for card_id: {card_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')


# Append retrieved data to results list
def append_to_results(ticket, actor_id, status, dbinfo,dbinfo1):
    if dbinfo:
        card_id = dbinfo.get('card_id')
        state1 = dbinfo.get('state')
        card_form = dbinfo.get('card_form')
        bank_identifier = dbinfo.get('bank_identifier', 'N/A')
        masked_card_number = dbinfo.get('card_info', {}).get('masked_card_number', 'N/A')

         # Retrieve status and stepName using the loan_request_id
        requestId, state = getCardCreationRequest_1(card_id)
        #
        fund_transfer_client_req_id = dbinfo1.get('fund_transfer_client_req_id', 'N/A')
        Physical_requestID = dbinfo1.get('request_id', 'N/A')
        Physical_Card_state = dbinfo1.get('state', 'N/A')

    else:
        card_id, state1, card_form, bank_identifier, masked_card_number = None, None, None, 'N/A', 'N/A'
        requestId, state ='N/A','N/A'
        fund_transfer_client_req_id,Physical_requestID,Physical_Card_state='N/A','N/A','N/A'

    row = [ticket, actor_id, status, card_id,state1, card_form, bank_identifier, masked_card_number,requestId, state,fund_transfer_client_req_id,Physical_requestID,Physical_Card_state]
    results.append(row)

# Set input and output file paths
csv_input_path = "/Users/shariquerahi/Downloads/statement_generation_pending_report_2023-08-04.csv"
csv_output_path = "/Users/shariquerahi/Downloads/Bill_Generation_Date_4Th.csv"

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
    
    append_to_results(ticket, actor_id, status, dbinfo, dbinfo1)
    time.sleep(3)

# Write results to output CSV file
df = pd.DataFrame(results, columns=['ticket_id', 'actor_id', 'status', 'card_id', 'state1','card_form', 'bank_identifier', 'masked_card_number','requestId', 'state','fund_transfer_client_req_id','Physical_requestID','Physical_Card_state'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
