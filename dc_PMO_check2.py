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
headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_csrf=raYE7kCikp55qNxPLl03rvcG; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.honD18mUXwttinqmsCE4mHzfCLEowVm-gp2rKsqIQBHHE-rlo6Jb6RY7bNv3v8jrUvgSmm4TA0WQONQX-3ony-glKVJeHakFfisuYJbwsz-Z2K6HlcZeiLopD-gWDJokVC85cj0JEha5o_SJPYtLjcEqhOFm_X_LAkEOxhiiZaHli7nkFg0KaUpaek1HsypUY7ftZp-t33pWcibD9KbRy34ZyYk_ZgfSBLELYKRbVZ0-HUxmHbJZ9GzdHMtf8_YWjWyaRhOJ5DW5trOJLLIk2YoCviPr_a0UhrErfoBkWapivFqY0Vh10Ag_N1HXxGUCXm-0V5H7q0esJLmc74EPzA.IG1I9QMSY0ZjrMV6.XHgcMbQnd2VracPsu4mry-cBBp4Xrp0evPqbi9n0pmsYGsg4X_5EziySdU4xsuSOh-6HiRdsEegQJan3EA2cfAxmCHt0mpGfJ_89s1pyT64NN6ROXtrJh7o23oD09jk8_vxvc3UQ_fBjN5fGNwnyKw2Aqfp1Y6gbd2L2--TCgBo4_m6pywC_J-yUDWA0V-uQK1n6kTyNZhyNwws4UogSorbCWAaOG95C0WITf56UwfbFUvgeUeE20_9rB1DI3RZnu11IpUbQWyt-F4w8KI6jt9WEqSpy7tzm775g7YbViN435k2fjlxbIh4JMaWxMNShCY5V3IjYLEWYkBeiO6xveW_LTxGKLiYXiJQUq4l-sQOfHlb6nf78jQMAvxAEYj2TR2CJUaW9u_W8gkXrkLLRXI5UYOE8QW4-mOLGCDsAjaIXY-hQY2XDnNO2zYzNJ6yDJtsKZ3440XvOeyh4yCVa7I0qvlswraeH7n_jxdPVY50MB3K_IdPvTt0ZhdfSpnlLcj_2H4ycksaGf1Dxfm1ICf0kP3g-NCtRgT7cdAujScMHWTP-PPRlKHSK0QDkr8A_2dypRGOZFlxRkgb86_Tpiw3l9ob3l3oUVE9HqnlRJP_WW2VGvNQppNsIkDMDwISBYZG91Iot5JeNt92jOvD9m92eqEJL9GiGDNJY8akpFamKDYAcFBBUYxveFFo-U6lNap4pGzCKi2o7JoytrTVjONI1f_Pso24C8mpNts3QnbwR8LqxquGCp2n5XiFDR6ORp7ObPApeA3UQPo5ThXTrEqIB_o83mxW5gxtrphFjmU9eXjIAMnf_9ZGjJpzAUHHLMx8VQMIhfJ_V46LusuAC4h4VxRhTRmSbDZF0eRTHkDKczYMDt_ICMF_B8wRDukR56MmQWbkkjIJ-mZPPSOpkzNc0MmtmV9CeyIbTvpaBQdvSYRFsYLCQ741SyKludHxFEaC8v55t4Y4SIS4Zc7ytJfXxOFiuZrvCS36HPdg_HrWcWi20M26_QIpR30RWal3j60Cb9fJkGaBCaUJ4UM59AJ9K2Yhj1ckjLDxQiC3xXjEIWtfaOudBujnFS_DUFX6BEFS4EdTAiUQPRicsQYBiJeEGPfi0NSmrSWpMJ6k8SUB4GgdjlUKs2wiE--z8rMhho7lNgQdq-2rwpo-M8lo323AKk-6thT02WtxHdtcEkbCGalkw_6o7aAH274OhfFfSz59xNDEltgIj55Y-ZxNrAsjrl7IalrezunohY21VlB5_bCypjcBcPNgj3KSNmzYxneZEZMT-qEX6IZ149Q.5qh_J-oNsM_vxsc5JEYlIg; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTgyMTM5OTgsImV4cCI6MTY5ODIyODQzMCwiaWF0IjoxNjk4MjI0ODMwLCJqdGkiOiI5MGU1ZmU2YS0xY2RiLTRkZWMtOGVmNS0yNGYzNzE5MjJjYWEiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.FYk2r5g86T8hQIJPQNwRs2Gl_0bT68ImNhQ8HolO32oyWM3RycO9J5vAyxvIPzrNDzrbxCfp68uJBp_PrrCF0Z9n61sjbqG1yxgVXJR_12k8LymGSIPS7uz6MKrnHNmzQWWGzE7vOwzB35OanmZMYPMG9m1uzJLgU0D_lYWULgG4SzYi8Sho0e11rRTM0iD3fImABsZWQOcDBvfflEhLkkBDdia6ser5eeijd6VGn8o_lvXcbEeyFrbfrkGzkOyvRyzh55O6kB1Gpt93Pcy3Wie5UKGJCqZatq5_hZRH0J6R0NCz9QF2VYvP1HKHGx5L415dFuLCaDpDhulrbTBc0A; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiejdLS1RmNlNWOTJKamgyMkdZbHZ1ZyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTgyMTM5OTgsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjk4MjI4NDMwLCJpYXQiOjE2OTgyMjQ4MzAsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.UFU6Ld974E1ADaJ-2sWy82DB9puXQC6_W7jcuf3ziQKw0POWsnbOIDRZOp09puHvL1k4NK7jMgrSL9YMkFF0sNlhWcQfMxAOA3fsqJCZlMaCAY9R_wsc8iqGnY4wFdhhMXM3G9AV200Chtnt1mMAEaNGr1FfjT5b9AyqzukcBcAvmnvOP9tUxkWilEjvG1-UKas0SlWLJs7qyixfy7X9rqUmQ_3YskdsK3skZj8CDTcARrhWa787j-o7WtrR967XKiOrCISGVky8F9k9M4-rYth9X4sIp1haziKcJtqWaPI5qPtlL4klCUDNLYBQTmcLKEApd0xLUTzAS3cRaHKosA',
    'csrf-token': 'YMTmRS9f-swVicHbgfpQ3Yxvx-LITYwJkGbo',
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


# ... (rest of the code)


# Append retrieved data to results list
def append_to_results(ticket, actor_id, status, dbinfo, dbinfo1):
    if dbinfo:
        card_id = dbinfo.get('card_id')
        state1 = dbinfo.get('state')
        card_form = dbinfo.get('card_form')
        bank_identifier = dbinfo.get('bank_identifier', 'N/A')
        masked_card_number = dbinfo.get('card_info', {}).get('masked_card_number', 'N/A')

        requestId, state = getCardCreationRequest_1(card_id) if card_id else ('N/A', 'N/A')
    else:
        card_id, state1, card_form, bank_identifier, masked_card_number = None, None, None, 'N/A', 'N/A'
        requestId, state = 'N/A', 'N/A'

    if dbinfo1:
        fund_transfer_client_req_id = dbinfo1.get('fund_transfer_client_req_id', 'N/A')
        Physical_requestID = dbinfo1.get('request_id', 'N/A')
        Physical_Card_state = dbinfo1.get('state', 'N/A')
    else:
        fund_transfer_client_req_id = 'N/A'
        Physical_requestID = 'N/A'
        Physical_Card_state = 'N/A'

    row = [ticket, actor_id, status, card_id, state1, card_form, bank_identifier, masked_card_number,
           requestId, state, fund_transfer_client_req_id, Physical_requestID, Physical_Card_state]
    results.append(row)


# Set input and output file paths
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/PMO_ticket.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/PMO_ticket_Output.csv"

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
