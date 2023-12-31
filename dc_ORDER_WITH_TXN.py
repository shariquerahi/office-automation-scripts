import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=GMAjUMQ8aerhbAoICARfu4XG; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTI5NTIxMjcsImV4cCI6MTY5Mjk1NTcyNywiaWF0IjoxNjkyOTUyMTI3LCJqdGkiOiI5OWRiYmE4OC0xNTRhLTRkMTgtOTY4Mi00NWE4OWVlODcwYmIiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.QlrJWT7RwHf_kLp22l5FjwA8qQgbG_NMUwBvNa3GKZ5cj9QGvBJl5UIGejnIO-XazM5dlUYFQseVltnYmfdB7FkkVXHJjY7mikA2H5E73b6U5U9m5KQSqSww5AeOEXxCeZ6wrVXZcNg-MtCo4qHkLQ0MTJArhaWMudVyApkndlQNpfZTVi0_T7FjJ9BQFUE2Zjy54gpGsTXL_DgnoP0hu6olBe94kFCX9InDGc9K2sxf685d_UujXUk1kHwUW8OPM1nXu5QEaF1_lmPtOgZ5KN83a9-i7jDFgdn3CWOrp3fecXUqRWoitY7Q5A2cZ69SxXkcV-tr3UGi5u4W3Kl9LA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoidnBsLWE5Y1pxME93bHdQYnF1VjBjQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoicHR0d01GY2NIZHpSOXBsci0xdkdORnNIQnlqQzNDT1dSQmhCNVc3TzZEbWNWc2t0bzN2REctQU5Lc2pCTGlST1Nkb24wd1ZGU3pfVWlpNmNILUd1RE84c1FWRHNNTEZ6bkVUckNaMlM1RVM3d2tObnpvZVlvaF9UOHRoYW9uaWI5bUlLMVBkQm5oeWxCcUI2UDFtVklwZlB4bVpqaDFkWmJKUDBYUEFaQ1hnIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5Mjk1MjEyNywibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTI5NTU3MjcsImlhdCI6MTY5Mjk1MjEyNywiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.pwsafa1VG78FRe2ZHHZVhtH9atF4kNQ8Yv_lw5gDn8A5YVTnTTmSIOIFS7DkOHYdpETyWUU-O8yguloJr8cSpprTOCMHwwjMD8_mQcwOLYFP6pmU0gk4A5MQwa3W_reR9j9RAzX0G4zxYeJFo0gY_WrbLvAitV--HzhHrEsfCcl72GCNed4Iw1Ma1mDxsvgnJNPxMg3Pb2WF9wf02su6Fo8MJh0gwjmNLBXW-0pSaVOEWwTHCshEylZxQPi-I-2dAQpXx4il5C7g713tDbQyJuAcv-kbalbaZe7kHJPb6weg4IMoxWjdHAaaD5edCHBS-TNeaplZp4yWwp0JOzlrqQ; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.dwWisbTGUayPi5Sz8x7vSSyNDIKKuzvj7WvECXkN3Pzt0na76Kq2ENum44vDU5k5GAlnRGmV0lFSs9nM31CeApJ7WBWnklDRBXup8_KgvvKq5-YJPY-vAuqY_hO3kdEC4wJQDtKrr5ffo5RaQR3yTeraK6whIXLJULDev-RbpwYsM2qRVs3S9Fpyoy4qo8Oxq6rUWFsKxqzbYT1wVmt-_D2yRx0i8bqy7U3GM2fcpITfvFWHJs_XX5CA7ocDkJEqPILhXVnzl6orBl_teelzYJ6pfqL0gq7P_nZuHnocMig7BnWJWWDjFpJLzBcEIXpo3Bg97Qxr6qXGy_t_9c-MjQ.pUURyvaMfXviWwv4.bDD-SQCJZyjqFxnkDM6ikvlmD7FIhxasKtKI994aElWhauh4I42wN6_6DhrZG89lgPT5CWBydh_jJPIcOXxT9N9cC3JRro87MrTq_A8Ottfxbq9bqRdYIenMkb4hhcYaFTzHrTx4SUoib3fMWNwVI4Rwf6oQmAoWSnXMfkzyuixa50LSuUqeb2hn7BFWetA0K_5fSvIA6NZ6ZI3rLZ7qM2SRwQ0jyVdxZy5ueVcxqCR_gKTmVQ1FYT5DLqhxiOBddtUfgALI80uM5yjKV59Hj48ROSSnl_m2Vd2ZXeBUoe92UGUo-JJY25GFBCps0wCRtBIqK-ef-GPPhw8Gz6taKH58EVgaKV_pG3ShTJdI7tzlvw10kO6nHhPqP5XOWl9dP6sZ1UQp_pHqiIHhWFTzBGC_dpiVn4No0uQbo2z81reOwuQ7YAVBWq3VTCAY35wE_Q65KQNlD1LcWh1iBtUxSmPKdB9X1F9BdJF1weA3-zcfsF4cwNENOclUtNbj79oH-aCcYN4fhWMIxEW_fEN_sj-mHTVvZwdHTtNWaH5tJGlCequ-wOsDxgs4LOqkrVNFxVVmky1bfGauxzJCwrAcdMDbm-KGI3mTS80K6sCH4vewN5xXDUcio9b9ho-3jlSQobR0sGJ5MaIEpBYxqlI1lMjgoKhbsaXGel9PfFRsvWQo0fJO7pYeOFcxENLemTwzlONrLtuGWYxh6OUaxk80yHEGa0NRt-1d68J8GFp4Y5G2pnb5m5dcIJCnTdnEwJ1-OKcabOxi0bqmKPW2NX5LTgoSVRPhoUvbvkJUwzp7PTCuzxklXbGo1aMAq0JeV2L4E3Ssxv5ETOfBd-tMswQwytXt_mAiQfFQLxkaso40Aqd8lbo3pcjIkHVK6vloUldYk-Xgmme8Vd2mNFIJgGRw68Wbjh7e9chYWwX3aGTVbtjln4KScmwGcShHhorHUs-RJ71Qg29osyJpYjSFyTjdla7bZVLNmA4jA-blFwKc7GJ1pvJnD-P95s1ZEJafhiKi9OjXpZv-7O1ZGXgOrEwnQYqKcqn-U6Qy1nXIHLU_HtAaVOZMSJU_-PnmssAA9LE9C_aAisNAu9NGxfIBEBiFVvTpVYa1XPgaa5bVG56m1rBFCeRxaW7kpGTcP_0X1KpQPVnRz3CXtUooN_Wt71zvR5Qnv8YrAzo8m04qKUFl9WCwBRrRieCcxeSyaXY3zpjmGGx57efzOi4Z2Y4Zo6fhLliCF-HdB0frKxbqzs35auMiCEKnJiV63C7v7iFxnGdP3syvL9Mhajru1Ltocw.I5hKzcVvJZ2r7rEWG3i1TA',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'SJa1fVkS-tZzmXygkQoWVEUr0IMgxgpl6KZo',
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

def getCardCreationRequest(order_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'order_id',
            'value': str(base64.urlsafe_b64encode(order_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params = {
        'service': 'ORDER',
        'entity': 'ORDER_WITH_TXN',
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
        raise Exception(f'API call failed for order_id: {order_id}. Error: {re}')
    except (KeyError, IndexError, json.JSONDecodeError) as ke:
        raise Exception(f'Error parsing API response for order_id: {order_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/Input_transaction.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/output_transaction.csv"

# Read the CSV data with 'order_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(order_id, dbinfo):
    try:
        if isinstance(dbinfo, dict) and dbinfo:
            transaction_id = dbinfo.get('transactions')[0].get('id')
        else:
            transaction_id = 'N/A'
    except Exception as e:
        print(f"Error while processing API response for order_id: {order_id}. Error: {e}")
        transaction_id = 'N/A'

    row = [order_id, transaction_id]
    card_results.append(row)
    print(f"Appended row: {row}")




# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        order_id = row['order_id']
        #ticket_value = row['ticket']
        try:
            print("Attempting to get card creation request details for order_id:", order_id)
            dbinfo = getCardCreationRequest(order_id)
            print(f"API Response for {order_id}: {dbinfo}")
            append_to_results( order_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", order_id, e)
            append_to_results(order_id, None)
        time.sleep(2)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statusment to check the DataFrame before saving to CSV
# ... (previous code remains the same)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['order_id', 'transaction_id'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)
