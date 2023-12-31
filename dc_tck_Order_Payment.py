import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=JoyDhRGIWlX_sqFGAZym7OIP; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODk4ODMwNDEsImV4cCI6MTY4OTg4NjY0MSwiaWF0IjoxNjg5ODgzMDQxLCJqdGkiOiI3MDdlYjY5ZS0yZjhkLTRiN2YtOWVjZi1mNjc1NzBlM2ZjODUiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.jgQuq2BO8bICWzs29fAJDMcqqYUk6TP_wuStcokAAt1oFpcEzDr510nrHbtJsRKns1jwMU2K87w0WCps4Htr0Ke42-CCX67Pi2WHxfSJBN9KOxHbD-wvZCtq8GIg9c0Oa8OqEETFBnEzBNBbq6gJc49SJ25kjYiXKkJGn7_zZQ56WKQAXG93ScGGDu170i3E6x-5o9ljwbaiIQGvfxXGWpfBQrSk9vUbOI801dxQzvKnSNyQ1wzG70bLMgbZgoBdMp1M3xLD847_k8lMwwqcioO0F4hpFgeYoAKZNulIYIHO-gi7M8QPiY3Vi6WVht9Q8S0Y9Mnv8bkVKqIM4tNmwA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiM05iZjJIcC1EaHZObnA3TUVrUEpiZyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoicllXOEc4RHJ6UlU4WlluY0RFU0ZGbElWRDVyaW5QX3NaM1JXb3Jva29iWmxGWXVDZy02ejljUlRVd0hVbUlhV0hKRlB6ajlYZ2NXb0tyYnZhVlI4ejk0Qm1sVXR6dTB5cUZOMkVNM05TQ01maGw3aWllUS1hZDVtMHJsUHRsQ0VWZUNVQ0M3eDlPUWRCdTFPVkpsUEZVcEFUQnlmeTdHNVNsX3M3MURWZXdNIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4OTg4MzA0MSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2ODk4ODY2NDEsImlhdCI6MTY4OTg4MzA0MSwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.FdL4RFgpjcmCvfle9qSEwm_YFi8t-ptr_yjILHcqbAQeKeKuoR19Rp55UcdUqp11ChBBdg4vlB-xcpbz-Y-Ubngr2c8TH7HwQeshTtB3rvglYNa8TWsUe_j3poj5lEAZ-oVhF-oNgJZH0AD7_3DgmPN3qMaKbSS84e6FNsN0PvHoaAyquzwNgRaX1LrsRYcR5iCp4--L_9hsGzm3i-jt9zubMZ6pEYPjkxvFrDF7P8Ee02ybq-FpWOXm-V3iTZpkBavnozLZQlPbP2NUdZto82kQjiErjo_r1VbbKrWmm8BmH49-jHBOIS7qq1xwJvqw5jfSF_c8tq5veWpl8ZxIgw; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.EegVEhqkDdzrKP7hIFhwLFwbNUl4fgb8zPtYF7dPYuB_NtPgC-CsxlhjJyUH7uOqCshMYykznd6PPpc6ZyK3gkrMmjWoSURbVRFoJHtUyB2zVqKYfQqDyF0oIQOc5apjFtolHxoGQhF-quxge3ZHLOF0SypX3SJARvTvXG8OoirDFhcz93xQUupYbMBGkag92OGsJlZ6Nt_k_-RcIlCFu8092H8qJMCdRvrsA7Ad0b9-WezoZ_esd-UxRCeIGI1BSg6NQ0x-mCWca0sX6709xIexig87_CcYBX6kuEUY7PpMOfoPEKSXYKH375ey45rLvclW-wuRrNAS7816M5WDcA.IkYgszs5bNhrxy1H.LeXJno1pg3DaraxRw_HGY3BgW4jHsaFWfxy4rh5RG0bWptE5xFYoLPB2_K_mePzo7jgmntfbLpjRbEqEVKXKDlvz5PlNmdDGefE2WpEeBN01P5IdEB-Hrl27lLf2omBrddOr7VwwIAX0hRmga3mR05j7FKt5wwm-rLhcE902BfkXiv0FeiDRgrdalv7uuIDqkwM9zWB0Qz3m8irg32OnsToKirwCUCSjoWBL2-y_PLuwYRruGPGQ4u2GgEIvuC4jAo_JvGg6MIpYDreyIQ4zt5j8sYF7tV8VuCMJJaLIeza1Gtmj7dVqVFyXhRtaDsTmJHoKb2m4g5h-a00rujIoR4lIQ4wX7litiq8WW8DgXU0ICnVulHx0yEU8bxtmITxokAFW-eX3JuLmnbjhcWZnomUiBk4kvvDz9BR-xJG2cdgEpOupO8m9hiwgdiuRgxzo9Dujcn4Uz3DCblWgfO9Oo9tg_li1b3AbZ67DUcMZobPHAtr32ha1htB2I5lk32wj0OObV1Z0m-6vCzUHr8t335JXPQ-qJojKHTItaURgTpJCeW_8yAzATX9G_AIhK_Ypv1abj_1jDHph8mwDMiJ3L2krIfcY4_wvUHyovkg8ICgXayUlaETS67NMqhaDLXAlM2lTD8DP2JUB8b37jWJUWhh7mCnzK_ctLTC6AqAFgfDzWk9ciXiSTgYsC029fD0A-iCYTKPUFme8zVbsmJZn3Sf708iZAh6BI78sBmgPt5SP2ccHcCHe3tQW_hunmaYorfkhMkI4GqVV6xJUF-njHbkpL23y-RR4oeTuZcEpzT6c0G06a9A1N_UinK11mHBLQNE-jks4CxmHrKMpKSAkD2QCd5UYL3cLU1xoYZJmQKPVFOmHe3w-ngVMvQ3nSnEPMWlHTkZ8gXBQcClRAO570_iISgSYlnwRVNxVLmNEnoDtOa3HzLbwHFqqIUHtAHdhzlNYNCLi4n9M9x3Ue-Na66mnoMKQCA3yhZxLHLrpoiwKJl28LKGS6-8ip2OOhV3mPFKsS4eZuClA3xSM7rzeTjhrKN9qlxAZzYiZT2v4EhOkr528HAqOPdrEWhrcjkBeCikn7BuWs1tiauiljFfdpWB-CzdcwJofJbm7vGtwxEW8L-0V3w0zkXIs26CUzLkLX7Yt46ewLazl29nOmM6tvIsJxL5Z1NXtvEKBRr_zG-NzG4UeYKzLxmjroDQO6B-07mUCD4degFhn19Kx2vEHXWM4iHlXaW70bBquIrQQHbSKqQdaAlN-srPAyBglqla8lNAOWqpb1Qr6fmw36A.1dFf3PN89OcjJacRwwmYCw',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'Mr1NTG1B--__FQBm1oZwnYBavZtdd9jM0M8M',
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

# ... (Previous code remains the same)

def getCardCreationRequest(client_req_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'client_req_id',
            'value': str(base64.urlsafe_b64encode(client_req_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params = {
        'service': 'ORDER',
        'entity': 'ORDER',
        'options': json_dump,
        'monorailId': '1',
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        print("API Response text:", r.text)  # Add this line to print the API response
        
        # Convert API response to JSON explicitly
        response_data = json.loads(r.text)
        dbInfo = response_data["dbInfo"]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for client_req_id: {client_req_id}. Error: {re}')
    except (KeyError, IndexError, json.JSONDecodeError) as ke:
        raise Exception(f'Error parsing API response for client_req_id: {client_req_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Downloads/Ticket_fund_TsID_upd.csv"
csv_output_path = "/Users/shariquerahi/Downloads/Payment_dc.csv"

# Read the CSV data with 'client_req_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(ticket, client_req_id, dbinfo):
    try:
        if isinstance(dbinfo, dict) and dbinfo:  # Check if dbinfo is a non-empty dictionary
            createdAt = dbinfo.get('createdAt', 'N/A')
            status = dbinfo.get('status', 'N/A')
            uiEntryPoint = dbinfo.get('uiEntryPoint', 'N/A')
        else:
            createdAt, status, uiEntryPoint = 'N/A', 'N/A', 'N/A'
    except Exception as e:
        print(f"Error while processing API response for client_req_id: {client_req_id}. Error: {e}")
        createdAt, status, uiEntryPoint = 'N/A', 'N/A', 'N/A'

    row = [ticket, client_req_id, createdAt, status, uiEntryPoint]
    card_results.append(row)
    print(f"Appended row: {row}")



# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        client_req_id = row['client_req_id']
        ticket_value = row['ticket']
        try:
            print("Attempting to get card creation request details for client_req_id:", client_req_id)
            dbinfo = getCardCreationRequest(client_req_id)
            print(f"API Response for {client_req_id}: {dbinfo}")
            append_to_results(ticket_value, client_req_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", client_req_id, e)
            append_to_results(ticket_value, client_req_id, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statusment to check the DataFrame before saving to CSV
# ... (previous code remains the same)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['ticket', 'client_req_id', 'createdAt', 'status', 'uiEntryPoint'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)
