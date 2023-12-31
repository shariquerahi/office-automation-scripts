import requests
import json
import pandas as pd
import time
import base64

# Create a session object for persistent cookies
headers = {
    'Cookie':'_csrf=GMAjUMQ8aerhbAoICARfu4XG; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTI1OTU0MTQsImV4cCI6MTY5MjU5OTAxNCwiaWF0IjoxNjkyNTk1NDE0LCJqdGkiOiIyZWQ4ZGUzZi0wZTZhLTQ3NDctOWY1OS0yYjRiOTgwNzMwN2QiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.A66GShoAU8Ei92u0uw1tt_q_DqkDQIdq-R_zGNi1pjGGyLHe9fsZBDD8oSrxU7naaahqfgWB_8FpcB5k3PQiooz7ann9nNqhnROACxBCsy6y9V7Ts_yVhkfsN_wcYqbrq5rwSTLnFV7nR0UtqnSwQcs_GjVxSwvW-bi8II_j-M1M4Tx1oPX0jSF8LrPRWd35BjABaDMmZhbEcmpt-VfqhCWIy-RzfZzqVCJUs4vBXgp4QuKgoUv9jByBnE_mY4uYIhOZe2x-RuGR8dr5eSit87wwXgKIJ-RoVFCp50m4CqLmKq1wcJjqI7UYaQaVkNFG2R0mANNMGHcF4W65wuwcAw; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoieGxxQjNseWNRaWNLejlPakdXcDZ1ZyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiejdCdkRJUVB6VmE1WjRLTXA5SW1vWlcyVjJmaHZ4TWlMZWlXRlFzaW51OUVsd3lramtLS3Y2WGpMZDZiTG5rTzFmNkFzR0VTcENSc3RVUHdiYmdoakNNV2dHenJQdURBSDZEaTRqWi1FaWZsYnZMVE5URUhRVkJmd0M1Nm1GdVpYY24xenNtOGlfMTNBTXFGWVZHSUdTYXVDSE1vV3UwclJXZ1pwdmEzeURNIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5MjU5NTQxNCwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTI1OTkwMTQsImlhdCI6MTY5MjU5NTQxNCwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.smJiOptjV293l_paV0S4vpCAmOW5YDR922RpPhL2x0B6SIAfVLTea7u-52pUJWePAVJkFpokI30Q7PEJU17ypDgBP-iwP6l9TWomqvhKvBqEjl3s9_0LF3sMJ6lqhm1P0nmwHpj3pUT_MxRbzyXinEb5xzI5KJvU9CesTCHjAVHC8ZBMTqxqVIyzHW6ZM4VUKCeiHhtAA8d0Mu9D4PMnhjq5bAzvOHZwwfZY-MibfNUVGk-MbR9ERe3waiiphBV50nCcIZ6UdTmledF_xnKbKJZCTWY_om_Pqw_gIDcjxCTBI3YSXSb8GY2ZiP0IgGxlh7q3Z5SPvo_U49KknlhCOg; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.KfMHuDdnmuqnifDtLL4w0EiXigv9kP26hsPsf6ymT0eCU1JLINRXuBkNQdPKYiaNjjoiUapbf5_WIeFyM_ZquE2nD9ch8jEQqnbd-Hc6r7WTeIvMoslG0XNv5mOxTnxMzPo6n8OxjBZ3hvJdhScA2HHwM9u2X1PTE2RaBkOyuNk6D0kMmcV_-zMGBzsnRIdsIMuqt8KLydUUL9hDpAh25476xo8xLHxd7b7R77SBKL7Rh_7VxMeeGu22B-CvBBDtjQenIYSr3PamyFfnxUXLnYYUDRqRaNqs2aisicB-ETy0xh07yvML41zO8y0l-iirn85bL66yXF4MIWPkWhw2ew.HjLq_AAboF_ercWe.g0MojwnTodRXcXYwW2ICf88U53-Ofxl1yFvqouGGuRiMiyDMAfmaALZGPMa2IMxJPXJvy3XZPK6K8VZf8sExMI8Hr5LHXoHWwnSoPSYl14E9MN-H-Y9tMB0diEg5dJlKF7OaPLdxiAZx8c5JAKRa_a8HRm9JoqlEiCr6YCPGlchjsqvaYVETaepIyZcs9DgtHeV_qufU6FhEM5q8umGO9rCgWuXuNA6erk_kySjqNk6VJwwFY6Xf0TjHV5vq3GixoXReEvUsKayi7yiVxtTbs2mqvLEl4Zt9-bHnxGW0wgAMBw4SpxyPg86NIxGcFt2xw-ykv7icVanzMBn3IRxVgfwOaNHwGxlvxwCbZqOY2L4NSHJRXkCQvZ1JYtXTI3waduiFCzAT6YVhoNAHC4ZZw3GAMoI2a4214CkVTD2MtzkbqFRPNsF8x6gGBjLm1aRX_ZjZvh6O41GruqFWEFaHwn-m-W8jfBqS58nIm1OAI7JatVDj3dY_kunQFdRWzLPtfB13hJWnrEPA8c3RC7trm0xlyDsiJ8u5oV_bivQETyVizxsbKK_S4IKm_BkXcWN-ajxfXjiiikji4LCYAR165lMPgS2gcgE5ScxC71m3SXtUexEWLSemlb5Mx8334syYejIPQtJ4-8XSALCRKK5HffzUIBRFkWuWKsf90LwRUml43wSFgPveDsQp8_93nO9SjEkmvl2kcnJaAVPHdzQO1CbXrcWDLtzqsFQzFswwYPNR2l7uHcpdDtD4F5tjS3PeE1mxlflSgyIfcUjpD_JbmXV95HYIYbiYdJ67PKsaGmCR2a09V2WEwE0s6Z2vFaM74BWFg0ys52_PJC6CZtZNx6JlEQ7geO0AZ4ya0br-V3m2D4ay-wFnzzCCygMZj0ePifGTFYpxDGSQNX0ocjFVc_fcVcjmT3TD47ZDKK7KPTH0atMk5Ny5YC6cytczLPE1lg0Etalkl6USpKvBScwkwB8PCu5FQkzVgbom8toTCadkeYr3lNMyErggu3VbDwcgAeY1S6ZY9CpeovyUq2HUQ4Fsp2B6lF56Bc483ho3WA83RTCkV5ffPmWc-6YsDUiM2ELqc1-Ke9cgPMG4QkZmoBzzx71nC0QGUQ3xL-6jg1Alq_jdhIQk3M5TRibrjglcB1-Bj9kLbNTjfWsknDzC7w29Eh9OJKPgRr8UZhr9Rruxg5aIiAckYMlkz2Fzufb_BU-7VVH4UEnT2WXJEL1ycS_-s_SfQaKmrDsHb_ZTSC5kbRkHFwgKdSp5LNk5HG__l5UwuRszUjXu-uBH7A.d-sYN3fHVquP8BRRspiRvQ; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'eorkWuJO-ivxOzbQiVdHNpkXv0SPCYcY_UgU',
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
        'entity': 'DC_FOREX_TXN_REFUND',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        if dbInfo:
            print(dbInfo)
            return dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)



csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/account_id.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/ACTOR_ID_4thJuly2023.csv"

data = pd.read_csv(csv_input_path, usecols=['actor_id'])
card_results = []

'''def append_to_results(transaction):
    row = [
        transaction.get('id'),
        transaction.get('actor_id'),
        json.dumps(transaction.get('beneficiary_info')),
        transaction.get('external_txn_id'),
        transaction.get('transaction_authorization_status'),
        transaction.get('txn_category'),
        transaction.get('txn_origin'),
        transaction.get('txn_reference_no'),
        transaction.get('txn_status'),
        transaction.get('txn_time'),
        transaction.get('updated_at'),
        transaction.get('vendor_ext_txn_id')
    ]
    card_results.append(row)'''
def append_to_results(transaction):
    forexPercentage = transaction.get('forex_charges_info', {}).get('forexPercentage', 'N/A')
    forexChargeAmount = transaction.get('forex_charges_info', {}).get('forexChargeAmount', {}).get('units', 'N/A')
    refund_amount = transaction.get('refund_amount', {}).get('units', 'N/A')
    total_txn_amount = transaction.get('total_txn_amount', {}).get('units', 'N/A')

    row = [
        transaction.get('id'),
        transaction.get('actor_id'),
        transaction.get('created_at'),
        forexPercentage,
        forexChargeAmount,
        refund_amount,
        transaction.get('refund_status'),
        total_txn_amount,
        transaction.get('txn_id'),
        transaction.get('txn_time'),
        transaction.get('txn_time_user_tier'),
        transaction.get('updated_at')
    ]
    card_results.append(row)


count = 0
try:
    for actor_id in data['actor_id']:
        try:
            print("Attempting to get card creation request details for card ID:", actor_id)
            db_info = getCardCreationRequest(actor_id)
            for transaction in db_info:
                append_to_results(transaction)
        except Exception as e:
            print("Exception when processing card ID:", actor_id, e)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=[
    'id', 'actor_id', 'created_at', 'forexPercentage', 'forexChargeAmount',
    'refund_amount', 'refund_status', 'total_txn_amount', 'txn_id', 'txn_time', 'txn_time_user_tier', 'updated_at'
])
df.to_csv(csv_output_path, index=False)
