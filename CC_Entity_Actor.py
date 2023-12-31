import requests
import time
import pandas as pd
import json
import base64

# HTTP headers and cookies

headers = {
    'Cookie':'_csrf=5N5WmuOmRpoZfGc5EHp-A-C1; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.TXTfW4wwMLw1vrZ8-HRmqCL5HRPgN0cpyzEZslsMSWESZ2bG7WX-WzXJ2_HIA5LMphElRtIpYgMMa76b9ytTmhN_gwOHIKkdcFGQzf_AlxJfUkm_Z4KyCaCdgr7rv_87RiRtuxTnuw3x58iOfxYONMs5Kv5wOq-gd8YGcAmzEgNkUxFgEZdceoZSdWePHgmeh1yXpGWrdQuWKrSbiLm6_bjMhoI61Ya0SxHaxT7rkJ282TqwOUlwk7AIawLlUfR9IGguhGdmQfe6a5-ytgojHABu1VO6HFGnBoFwfal0HIDUSeh_tdvI4kzOnNA9yOJ-4If1Sqyj-9fxrS4r--sX_w.AS0PZK5w3qMnmAi3.23NmmC_iqpOHirVuU0_cApK7FiIptgLUmz0mxay_ntcRr5GcMVgtqC8k1RACBCqQBqSbvqPYAw9DZCBN8OsHbTd1UUGdw6Y8seMHSg5u4rzPMLpnkfiEHhtop1hh0A56KYKHqKmqezKn-AYAeTs7pDCpyBncVZDG_MmtJjJ_Gkq7adsIUIOOUvsRc-yqJy-JqKqTCoI13Aizo9cZUQO-SSTT6QZZ4yo85I8UrX6RRG8poLnDZbmTmMhvGbOuOxyGUiQduz-omms9l_3NZrtWDdLmBjs160k2YHDhuAkYHLxU8Tu3oWqbrpyw0pSB9vp1U5vaE5SMDhlOcIk5yqg4edvAug41jVRhjXQKMAYJp42dF6pZS890vPjnjhN3vsLolD_ra7sS175JNECjCwARoefdyfTgAd16HY6x9Vwo_2jS1FHmec0Y-Q3nihVpCZRf_cXTDF1rla7aw2cwQ3lzGlDEmjWIGNtJ_fQIg6JYZFadUfTRi9vAd8ob20x85A51X5tOEOq8-PbKGiBzCY1ZMo44AX-eSmVnpJuHqsje2SAclvUt6EJUCuwWDBcEo6SllVbByrTmi8kYS4fEuaT0etWOCb1FP1vewkDSMFroIpQBCQXvYNZ9Kd_4zvz7BUulzPQRmn0xfbliRTuYBoFZMn5zYKpdwdNUT3diAy3QMrT8A0bP9zJUaVP2536MwvyeV0Y2M2SoVCxhiJ6a2XSRgmgubxiDTAVn3V_VBArfO9IxCfH0d-z0F7c6E7-vX82sGF-KHoUbrKD12Q56q1eKwgM1orJpR1qefmVJMibxQ6681G4gOjiYHSG5aMsg6pqABAEgf4U_157mcfW42LR1_RpdeWdfFMFqiOvvspqKNW4lyEThwP0Oag7Y49-Ryaxxa0klc8c08JJ0Zq7ZcX_BGZYX1Q8yfPifwyDGtZ8Ta8Jihz3rYY5E-jkwciZtXKx_8XImV612tgp0RVoHpEzx8NQU9XsJlUjvhvTQxWeS1YWUb10vn-_PICa8NU-h2u-5L3uyZEudriIl-GhWMgVas8C8j07bOybVpF6Xc3XP8pCTRbEhuJfCG-QsI8ecYTT_kiBfm3KSlXdZJda0FJgMewlgrg6MFXeCz4Aczt8L3tkhckyqKKXwVzGLqa-9mMC-zc5b9t_IC4YRXstaImRpQyR-ebAMWRIgisG1rIj4VXLN5UbW3b1nOci81prIh3pr4LjvOWZghyzVY-ezhhH6fGviFhtAb5uMOn7y2hBCc_WpA9fkfGTOMNhpeTAn1GFrkvPPppCdrkSaKt7H-w.RzdDR6_DulBha684oCNw5Q; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTA5NjM5NzQsImV4cCI6MTY5MDk3MTIxMCwiaWF0IjoxNjkwOTY3NjEwLCJqdGkiOiI2NzgwYmYxNy0xY2YwLTQwYjEtODA5YS1hOTMxMjAxNWQ5YWUiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.hdySGM_XPRcMDX_r4FJmMp8nxscaGTP_R6gSIo6Gx9yFMndEfdQMoFv-0Xnf0gBj5c3LPIx55z5a_dt64rUHAiPwtf8DKtfA6p85lZYYVDBdLTQ-guK8PJWrYch5k3VAJiM5jUcTSAdmGYgcbqe_UOm1-lOLTNXCKOYxEecgqaIkeZbS19IfPVg61kmkHTmaf5x1rbwFxAWxCSi-Or-M7CfbkINuXepscLPFt-RIW03gV09iUlkk4L9PV5I99DtuXtPzp5zb_CUi7P8j6-4URIw2-XiNst52bg2OG-DQxucjmzkWtvA7Qo8I-SmluJ7QDgUqotO5lbIl_QWEpdBjdg; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiSnQwdWN5OGNlXzYzMWI4VHNlNFdfQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTA5NjM5NzQsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkwOTcxMjEwLCJpYXQiOjE2OTA5Njc2MTAsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.Ct5AC-HeXFzA0PPRrkiYvsOkEnT-9opcApV6DUE41kmPRq1MaF7_sVN_ObneRJHPdJ8-y2IJl2pdNqNA_xmMJgZLPiHKOxHlcv1XSFR-WNhxz1J1x13MVp8UyHe0AxqPrSeFKzDcT83iamSf6fykEu9RkBOc3xf4sPHKxb6UaP_QUbM08tQEhkL_gTRARyt6uO_mRJ7CiykGjSzCf5y6bMjTG4Ln6Op1filDATPpRvIU7oFZPeKMqt4M-Lgg5EMA3C_aVri3PdROk8EESuUPNQyLluLx48WBKSwDQu2KGzz3bZ_hPp_e8vzvhMTAyZWuYm7_0-RSK5-nTwUMCc3XYA',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'MLArFjyy-E3Bc1Z5wpL1QZzSR-f9V7ae95nM',
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

def getTicketDetails(ref_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'ref_id',
            'value': base64.urlsafe_b64encode(str(ref_id).encode("utf-8")).decode("utf-8"),
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
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo.get("actor_id")
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for ref_id: {ref_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for ref_id: {ref_id}. Error: {ke}')

# Function to retrieve ticket information
'''def getTicketDetails(ticketid):
    url = f'https://sherlock.epifi.in/api/v1/ticket-summary/{ticketid}'
    r = requests.get(url, headers=headers,cookies=cookies)
    try:
       time.sleep(3)
       ticketInfo=r.json()["ticketInfo"]
       return ticketInfo.get("actorId"),ticketInfo.get("status")
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)'''

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
    params  = {
        'service': 'FIREFLY',
        'entity': 'CREDIT_CARD',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for card_id: {actor_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {actor_id}. Error: {ke}')



# Append retrieved data to results list
def append_to_results(ref_id, actor_id, dbinfo):
    if dbinfo:
        vendor_identifier = dbinfo.get('vendor_identifier')
        maskedCardNumber = dbinfo.get('basic_info', {}).get('maskedCardNumber', 'N/A')
        customerName = dbinfo.get('basic_info', {}).get('customerName', 'N/A')
    else:
        vendor_identifier, masked_card_number,customerName = None, 'N/A', 'N/A'

    row = [ref_id, actor_id, vendor_identifier, maskedCardNumber, customerName]
    results.append(row)

# Set input and output file paths
csv_input_path = "/Users/shariquerahi/Downloads/Entity_id.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/entity_actor.csv"

# Read the input CSV data
data = pd.read_csv(csv_input_path)

# Initialize results list
results = []

# Loop through ticket IDs and retrieve information
for ref_id in data['ref_id']:
    print(f"Retrieving information for ticket ID {ref_id}...")
    actor_id = getTicketDetails(ref_id)
    time.sleep(1)
    dbinfo = getCardCreationRequest(actor_id) if actor_id else None
    print(f"API Response for {actor_id}: {dbinfo}")
    append_to_results(ref_id, actor_id, dbinfo)
    time.sleep(2)

# Write results to output CSV file
df = pd.DataFrame(results, columns=['ref_id', 'actor_id', 'vendor_identifier', 'maskedCardNumber', 'customerName'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
