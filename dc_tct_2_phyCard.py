import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=iSD-dr-8JYSGTYOh4bkNCKqf; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.P8KDoAMfMysAV53zrKaWIq1dzm2GobUcJmx_sOsHoJZx0UlRCiXeeQ-7nyITA30oH_93NR1BFh4q8tKkRS6E3oTPTk8sdSACBYyuwlhES3FmrLG3XwIUSzJXmjsi-_SRMQ7ILVTqdGkenAnxKFyt8v4Sr8hzsR5cJorQNZjdKtAQii2AXGtoATmutJveyezn32RWTKGnkHdEnFklaKiWcFyu4hXIH9DS9jyKMwAyjitfMKMM75KTtUIkzO3Abwiw8NETjdphRCfzXjLMBrAW6U-QY7IzrcIoOWnhRZu_Fmpb-VjlIsMK3-tzs9ui8qRYdfzo1yHb4MnyUxKXBI5MlQ.23j5fbiY-VqOZNPf.zC3mmMTUDVI3UQfMIhqoRdlCNRjQn04Pe9aF6dPaqtxfa6YY5iPMoCnskWPhhIXjAqpqR-dDyBTIQCqj-npFVOCwjkArIyu0RG4GbD00EESZEwnjwDnTFVv8_6X7APZJ4pDWF3vqN9o3T5_YmqOc4QDKwJk1K9iDrxzeVMu-wguFysJSD9cp2B48F7e2-aXOW7YHtHyhFTK_MIla_1WYujPPl9AgeXrAm30Fw53M1RYPnRSSKJ9FHUjnQStFiuNZo20NsKmZCrKRw0I39Q2WFBj-9VUN2KBx6IlhiiGMnUaPNOy1dd2ycbPNYtducpTshzOciHhTbxCTp3rPH7KFh34MQmUR8zwgWL7GaGok4CYajdO037ChdVSYAoxLdDo94eZK8rHo-JqtAfNdGrqlickl2xU648T-yJ_V4RF-KCrwzwx-iNbQodJg7y2wWeDQ8nDdXpQKKbwg55yxwXWdgceMbvyHU7Nt7qLMjZA4xd6yI-OoWO_UJvPBPwNWaUctuXlZ3C0Zjl8azDhuBEvI1_E8wzXfmDKacNPDY9JW7OHdzBk0zvLxgmB4vluG8iqmjsJA5vsCA3iTnLKCfLIGxUTcd7obXnS7aV47avROy2L5RlO3LEOw0ScsIZngdblC6S71J1hWq-rILOZ6ZahYw7nXJ6mIjh6lwiglMcuwEXHS_zYquoA2d5NQ7BZCq3kMc_Jwx6uIdM7AmOuSSqrA6zgMcS9GbHFBEVI7lM4XbVEi5QVP8jU5fPLLlks3w85QlC_UlpkItNyswxMK0a0vG-O3M0E_TgRJDTS3DMmEW3DOOqs7ltmkwgVa70H5zf-xtglWxFF2YT3uhr7svVLL0Jyaozb-rN3209NfFe6ArC9LnaCo-Paqr17ldaKlghc55zu42zvcBs7JrcWZWUapkMu8IpV3ljWqE2I5O8V77OzfkFYZoTSLiaoeNRHoVNxNiUkwHLjUVwy4__M0mD5enFan-4WcmXO2afzS0iGnqa0YerT4BgNiXYAXZt1JIr6FeD3b2jIb7H52nCSmZnr91H72dJSSEJ9bI3MN2Z0snYc8KBYMrQ2Gm2RJCDZEjG-Z99M_60TMZvnpiZ6Tf4PZCnHlwghGgtE8MSahPq5dh9Cs-zPpwEQ9GVsa1dBUGatrKXkukp7tIAPSrmkjLoDbgA-vG5dLVD07lfPmeGs7ZLyyyNFPVHoJC8bthhuNyG7Z5AVYbXl18I75DnvqK8H7QY_KkEoS0pYt15tCUB82DYUu5S_2JazJ5kN99JZJa86cwq7iJM0_YOngM4cOcQ.yeleK3paOEJ82WIAnQ10kg; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODk3NjIyNDEsImV4cCI6MTY4OTc3MzE1MCwiaWF0IjoxNjg5NzY5NTUwLCJqdGkiOiI5Nzk4OTZmZS1hNDIwLTQyMmMtOTMxYy0yMzg0ODdhMTE3YWUiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.XhV0-UE6RCGXdRAY7msHK5HJzD4mXHwA-hpVo9HqFxqrc3BwTd-foSaU1o9wtxQNQ6AmblbfjmpFgwgee-n2K5xVeskZGWqJz4SuXtZzAIRlkmN2s-F_JmWGTql_6wrxxHCFDGGyzOeihLe6WZ4WTdnzosTzxFYvU3C2lc7VMK0_2DGaxcqiyMkXuMchV32c12In6heC2Ml7VBBqmbwbf6pnxIPLpuRsIkHcgnC3rDo12BF319_ozGzvri93RFaugzVXO1ATaSmOhHVhh49KS3RzP49_-n3VkNsoIXBOTtuiotlEIVcEbYHhJsE3kHTmkoC96sevcKP2B8Orj8s-TA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiUGhfM2ZLRnJuN1h0Um93WGo5WFJLdyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODk3NjIyNDEsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjg5NzczMTUwLCJpYXQiOjE2ODk3Njk1NTAsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.ogZqlHcBxmvDIobkqZohMyNyk2KP9SjXk5zhmwQvPn9uHmpMMXClnM_bOULseq5kjUuEtAcd9IwOk2BuSTszGJxeS_exUq95wUJ6OFfyjGfQ7ko78D6_jWaHwLX1u4e0T1mswBfqfykNfbCSOMr4Pvtyvxvg2AIIsfvLCRe0r69JN8Q3aIWE4bkopwdRExS5BwrppEr1VY6yWwmk4fMKSRj566MJgdh7_akLYr97KDbEAhM1MsRmZJRSGc6LI1-33TdaWMipMG9O_LRUJg_NXKhtDKTyh5LUmG-iSCgz57os7_Lp2bib4COIAX_p03O2qxGdDbg-3ePfDYnec_aYkg',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'Od5TpdM6-p7ZYZ1zJE1HVJphkU3GMPCh0YWs',
    'Connection': 'keep-alive',
    'Method': 'GET',
    'DNT':'1',
    'TE':'trailers',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Accept-Language': 'en-US,en;q=0.5',
    'Sec-Fetch-Site':'same-origin',
}

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

def getPhysicalCardDispatchRequest(card_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts1 = [
        {
            'name': 'card_id',
            'value': str(base64.urlsafe_b64encode(card_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts1, separators=(',', ':'))
    params1 = {
        'service': 'CARD',
        'entity': 'PHYSICAL_CARD_DISPATCH_REQUESTS',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params1, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for card_id: {card_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')

def getOrderInfo(client_req_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts2 = [
        {
            'name': 'client_req_id',
            'value': str(base64.urlsafe_b64encode(client_req_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts2, separators=(',', ':'))
    params2 = {
        'service': 'ORDER',
        'entity': 'ORDER',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params2, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for client_req_id: {client_req_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for client_req_id: {client_req_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/ATM_setting_input.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/out_atm_setting.csv"

# Read the CSV data with 'actor_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(ticket, actor_id, dbinfo_card, dbinfo_dispatch, dbinfo_order):
    if dbinfo_card:
        card_id = dbinfo_card.get('card_id')
        state = dbinfo_card.get('state')
        card_form = dbinfo_card.get('card_form')
        bank_identifier = dbinfo_card.get('bank_identifier', 'N/A')
        masked_card_number = dbinfo_card.get('card_info', {}).get('masked_card_number', 'N/A')
    else:
        card_id, state, card_form, bank_identifier, masked_card_number = None, None, None, 'N/A', 'N/A'

    if dbinfo_dispatch:
        state_dispatch = dbinfo_dispatch.get('state')
        fund_transfer_client_req_id = dbinfo_dispatch.get('fund_transfer_client_req_id')
    else:
        state_dispatch, fund_transfer_client_req_id = None, None

    if dbinfo_order:
        state_order = dbinfo_order.get('state')
        status = dbinfo_order.get('status')
        uiEntryPoint = dbinfo_order.get('uiEntryPoint')
        createdAt = dbinfo_order.get('createdAt')
    else:
        state_order, status, uiEntryPoint, createdAt = None, None, None, None

    row = [
        ticket, actor_id, card_id, state, card_form, bank_identifier, masked_card_number,
        actor_id, state_dispatch, fund_transfer_client_req_id, status, uiEntryPoint, createdAt
    ]
    card_results.append(row)
    print(f"Appended row: {row}")

count = 0
try:
    for index, row in data.iterrows():
        actor_id = row['actor_id']
        ticket_value = row['ticket']
        try:
            print("Attempting to get card creation request details for actor_id:", actor_id)
            dbinfo_card = getCardCreationRequest(actor_id)
            print(f"API Response for {actor_id}: {dbinfo_card}")

            if dbinfo_card:
                card_id = dbinfo_card.get('card_id')
                dbinfo_dispatch = getPhysicalCardDispatchRequest(card_id)
                print(f"API Response for card_id: {card_id}: {dbinfo_dispatch}")

                if dbinfo_dispatch:
                    fund_transfer_client_req_id = dbinfo_dispatch.get('fund_transfer_client_req_id')
                    dbinfo_order = getOrderInfo(fund_transfer_client_req_id)
                    print(f"API Response for client_req_id: {fund_transfer_client_req_id}: {dbinfo_order}")
                else:
                    dbinfo_order = None
            else:
                dbinfo_dispatch, dbinfo_order = None, None

            append_to_results(ticket_value, actor_id, dbinfo_card, dbinfo_dispatch, dbinfo_order)
        except Exception as e:
            print("Exception when processing card ID:", actor_id, e)
            append_to_results(ticket_value, actor_id, None, None, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['ticket', 'actor_id', 'cardId', 'state', 'card_form', 'bank_identifier',
                                         'masked_card_number', 'actor_id', 'state', 'fund_transfer_client_req_id',
                                         'status', 'uiEntryPoint', 'createdAt'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)







