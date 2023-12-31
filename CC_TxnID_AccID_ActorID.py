from ast import Param
import requests
import time
import pandas as pd
import json
import base64

import urllib3

# HTTP headers and cookies
cookies = {
}
headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_csrf=fR7lNm8fzQ_GO-6HwX5S1wqx; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.DCjsN4A8G9DEJYHWnaaIr4D2H1P8ledD73dALv-7eHlVVh86jAXI7wyvGbXb43gLqmWzQdCLXBI6Sn7o0jo1a1TNFjpCPl3pmtIP2ENKAWjEL_WUtlTH3wE1UR_W8m2U8whmHIlf48MG9TKDSUMfA5DQBsa8hdlK4fBDThkXmphdVbZT2JthowYGoZ50q5RXeNYMyXLxTp0_8Z0YmHhsk8Q9pW2Q69d6aFCLzrZq940DsaGuXIYs3I-Yy6NOSt1ZRDgn3bxj4BcWx1Rn2OS6qruyY9FSpO2wxfdT_RASIOuzvzTqfjwePJS0X4GyZrJgsEH9YfjDJnbhxC8Ehrp0Dg.rqEuM7ngoPnVAdwO.4I5dbF7ZSI67y66vPXdUJ59QJsYIBBk_FBWANosy2x0Mo7FZNhSNsfU5Wvh9m0CQp7xcidFX1VpdW3VDZ66NxXqeV5kVUFAac1GJXeaGIaxlAjFMphr4g8jWLPHJaYUbSk9m3cSYD4TcHBEHb_Atc3iSPjtRvxVCRD3UYdVihK3NauKX6Ax-Wzr-S2ZV1OadC1R5yL0dXE5t0nsXHFNh9MU8xF9KJsnqGjmuPEzmtR_4YwlHK5TnFUzbMy4R2-NvXcBBGT_jiT3YbZh_zAQdC8GYm1hD7r1XqXrWe2FSNy2oCN4INfcYo9lvEcI9DrPWi1R-1-msqvgB7NoDThnvwf7Q6krPVCIkNKL6BKuq6lu8D_uT1GWpMQk7UFDZL6nFSUYlSD523mfe-F5hJgnJUotakKKsSMmShHm3KLhFk0aA8wdK60lYcxYMqYk2jGbxzfwmZ31RJ96RPlkbuX347n55vTQGT9HJYGC9KpjN0R1VPlpU2vwa4zjVGBj467qqgL1mQ81cqw9DCExKQgo7Te_BuxV7CQmz9jRpI1v8iK9v99f8bxQ0BwHWCeB5nGslmYcTfo406O9CNKd9IZa26xvrc0xWh_fdsbjrqa_2gAgKhmI2o9XBGe5f_Pqq0N56hnAwBsMB29jF5UPs6Rn8u7sjZwR0_aoZAPDGNeL48VtVqA6UauwdrVW3U7Wg8gbb7JwkP84N-XPBvCgLLgONNi1oPCbTs5R_A7Pr_6k5FguniQIF31O7lzOSj7RHPxaUCogdymN0R3KCoE4DmgTE94UqsDp_DjMZN02A_HNPU8o0sJtnKoNrc7TtgtS0ANJYiXPBrtIyMkFvEVXwPowP9tDN-v_1uAf3XffMCCCm8ex8SqKKqc0NyNrziU1bFI6Rp84T_Xlr0ugMiHuOouLDtMLn2Xe4-mHy6OE7OaE03zOSEY6j_PdQV_Ch7cjBv61MQLP6ek3uwj-nNfkGKpxMldgehaTiEHiGXHWwyzQjLg79LxIpE6_sFGoobtNKad1kqaQLDyavPsPhhxZbO49t8jO-qiYLg0VYEa8Dt24EqV4Us7-pmgKA449m9b2r_50tU8l4Q0g7XFYf2tJI_eRsewqWWWe4Xk-kzeh9RcHALNytjDVhCZccVH52YgSsHz6oOsgmXcajWz54lCMSNxPux-yk09AgT3yFjmiqo9Tb11OvV61dJM1KyWD_MUtSbZbR9qOcSb-AVjOaUEoPVQkbyhiR0R8US_gqKStQINZYp7zZHxe4dXuavkg83x792u3Fpt2b1_iPcEvZoL0KJA.zn79IGqz65Z2QTK_7STM4A; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTI2NDk5NDgsImV4cCI6MTY5MjcxMDkxMiwiaWF0IjoxNjkyNzA3MzEyLCJqdGkiOiJlMzRkYjk3Ni0xNzhjLTRlZjYtOTQ4NS01YTJjMjU0YjI2MTQiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.UuiYdgKRK1ZgByJ_WbhP6w04dKXJvUuO25h4a4DrLCO3pY3gWXGaUPjRGcNLMxssCSdWawUOWsZPpeGkrp24w1mEq-880BzC-b_WQLaGwjVXMMdPnZX8ASzxbEckUgkfAskA69EpjuJkZgh89aGmOgm4L96VUKbAtxcHn9KeO72ji2s4Darpp63WVDoA5EKp8p_XpPdly2iYOhhWhjUXiwA2UqVBx3g6Jye04Dybn0fiS-ttWvOwKBJGsru3BfNlQM_fyk1iS-dHuz8SJBbLY27cfZhK_bk8-tdcrlBATI1slyTo2TfhTPd40owyIHYeU493NRyP4CJOyBOfe0eSzA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiQWJIZ1hNMklyZ0dIY3A0cWRVaFNsUSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTI2NDk5NDgsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkyNzEwOTEyLCJpYXQiOjE2OTI3MDczMTIsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.KiADunArnTW-maSF6iwszV0fj7mIIkgkemsbVGTp6SMh-2Wd6z0-3BLJhQdApNrw14Kwks4ncFAYVAE1mXaEZXbNlqAIcVRFOSdWhLeHzJkdPRTSFRKtx5hcNW1VcTJkSDNmcqMIHzKOsHj3mcqK6ro_8ShrYVZnWDM3xeiS_SUl-vcKxkf3xl_SmNv_X6bdRmDGuOQu2_7paFCFpijOqvYOJTSsjBvjiFlrCcyzzYpp_TUrx1ZpeBlvm4t-2jd-r5-FAHawJFEC4HmiPFX47NCSkmJsTjFUyN3-trH8kbB6ukYHZB3K3Ypl5tI-FZf_TDuHbhhMHcgr5yeMDdB46A',
    'csrf-token': 'xHsVU5gR-C84w4QPPhFZRry44EPlzHoSs8ms',
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


# Function to retrieve card information
def getCardCreationRequest(txn_Id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'txn_Id',
            'value': str(base64.urlsafe_b64encode(txn_Id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params = {
        'service': 'FIREFLY',
        'entity': 'CARD_TRANSACTION',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for actor_id: {txn_Id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for actor_id: {txn_Id}. Error: {ke}')
    
def getCardCreationRequest_1(credit_account_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'credit_account_id',
            'value': str(base64.urlsafe_b64encode(credit_account_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service': 'FIREFLY',
        'entity': 'CREDIT_ACCOUNT',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo1 = r.json()["dbInfo"][0]
        return dbInfo1
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for credit_account_id: {credit_account_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for credit_account_id: {credit_account_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/Exter_Request_ID.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/output.csv"

# Read the input CSV data
data = pd.read_csv(csv_input_path)

# Read the input CSV data
#data = pd.read_csv(csv_input_path)

# Initialize results list
results = []

# Function to append data to results list
def append_to_results(txn_Id, dbInfo, dbInfo1):
    if dbInfo and dbInfo1:
        credit_account_id = dbInfo.get("account_id")
        actor_id = dbInfo1.get("actor_id")
    else:
        credit_account_id = 'N/A'
        actor_id = 'N/A'
    row = [txn_Id, credit_account_id, actor_id]
    results.append(row)
    print(f"Appended row: {row}")

# Loop through CSV data
for txn_Id in data['txn_Id']:
    dbinfo = getCardCreationRequest(txn_Id) if txn_Id else None
    if dbinfo:
        credit_account_id = dbinfo.get('account_id')
        dbinfo1 = getCardCreationRequest_1(credit_account_id) if credit_account_id else None
        append_to_results(txn_Id, dbinfo, dbinfo1)
        time.sleep(2)
    else:
        print(f"Skipping txn_Id: {txn_Id} due to missing data")

# Write results to output CSV file
df = pd.DataFrame(results, columns=['txn_Id', 'credit_account_id', 'actor_id'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")


















