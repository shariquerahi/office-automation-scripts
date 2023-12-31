import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.U1bTeE81LTPUV_eWNFRyHqUekphc4KoYLc4o_EarblvkdqcJYm1Nn-OeLnZR1ZkWRMISLTHuWQpjoBlGv13qlRSR0IesDoc1MYT8WyHhkZy2wZfZ97CyDDq9dohdES2fAGORzfshu67ZgKTwvLlmEAq0sPsGVDbckFDgBwuOIcjt5oc5lg8rhN1ZA6atnmPGJdKQ7cvG1NqLbMi5ItERzzRM7K27WWMJYbzGLFTOv1Zt0xKwC8niOTCxtLz4mcSTWSCKyUhNW7EJBWXTNmkdgHsMD-YI8FPfQN5kJ3mDBwzmJoOrsQKCEiN_oBIotMGTfJi76UDsbg3CfN5eXXloyg.zcZdwtn1UXmnv8h7.A0JF2iImVFD-PVuUZi4cYdDY8sDTwmFiLdb_4eZjYTSGJsn9xmzdvgMJ5FlT9_qDIVvzewxeua1YAkH5_UQlEC7Mar9bDLc7atLL8HmaxmWWjJN7tJGj86SnsKeYIemwrVS6btnbK-hl3J8q0VBs8IelkjVKf3ElUge27FIPxauultgweE5XwuxRm2w3CLxACRgZC1ReqtxSsxlSLQ2Ln9zeHJSWEs1-lJS1TSDIZgjY5PrKIxpADckA-cLC64iUWWUCRiozmuJiwKwAC1iDOcO8Kb0eBft6o2gnTWS61jNOnUDEogBlBTlGsz0CCD8D5MKPHRoWvhRkxfIuKe1y2eOxP7AGfbgk7FuAqMICYma6aqG-IupKDTCSa-TLAbVLgQa6gkKozzFD4CCqltCL1LIE3ZvoQVHkd-hjXZwJeRkaNlVT1Nrubw5-kmP1oJF__u5auU1zASz6gDWu7SkPDeYM7j0-mEFMnU3XKON6Wphnigtky2Om4_DiQPD5rViKXNuXSWyCMnOt_nfatP_V7cpk3iGLfIcisH7ZV2X1OmWen499AIxig9xLQTKthepW9VINgZyPIqOKvvyb0FHZtAIbXjvF_x4Z7EYIjHgkw9QD0wzL4KUaSnuEJSRgizX1lYC5k8o1z94VfPNljKZyGGCyaxEPc7-j-U9x_mZEm2ETtxE5mFO7eOubrRH0_tFm2btgoYh4Du3MR-loDVEtz67efpuTwLJgvKvjNgXXuZqPIF9zj3azgEfGB7GWXPfXrZVJFX-tmFRzzqhIntBpHwv_M4XwMBbhBR-jVGlupnINBjssODRTVtaBYT5Euh3HKKzl_80BudBWkItBAU5grd_9MBxMmpknKHCIK5n7hGfUniavwVToWhMTIJ3E0LMHdSPq_dtpkAazTaVVAaw3geCvHoUY4bBciJIyfE0aLhf7CF-E3rY6zErWRM7E5NHr5AJ1modpmN54sOvI4jVbefQbZxxqyQWS3grehHweIBZUE0gs26raTb3LY7R4wvJGR2jti9qF15Udngd7QgeAtX6PujqUU0bwlwbqFnTmDuUkVocVb-BvLilZczRJCsF2OnqQpXDIGzM_XpYpug1SByP1WM-KPyMJUHEsZJBrymU1boy5kIGp7RQ0-P-IU7W5eBnYErgFCfZ205ZnUiTtlVamPzA9n3C0nJfN1kuQJSmHzWVWco2ntUh3kk9x1kS3J33vNXXrGeF0A9uoLJEB0GON2Mg2tpC6UqnBSE3SftjtW0COkCyAAvkEmXEbbdV4GuyhXtztqfqqXBNWxA.3sp7b1VGIXythVYLhbIHyA; _csrf=r6oa06-B0jCXBWhiA5Z-JPjd; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTAxMTUzMTcsImV4cCI6MTY5MDE5MTQyMywiaWF0IjoxNjkwMTg3ODIzLCJqdGkiOiI1ZWE1MzhjOS04OGE5LTQ1NzgtYTg1Ny03OWIzMmU0MjhlNmYiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.CdJrFc0VUGuF_vZy4XPzY709At6Fkcoiz5rwyRvTcR5TNkoG7TEhY-QI_97HuNei2ahpp0CyBRMqKH3dzrZ2NsiyivWO6vqDBdA496QWf9P5CFC54zUw9GOjBO7m_62a0WXAT7T5woDdNcaAEtBqQwHxNyGtA__WZE_oce1sbCVPZGK_Jsw0Sg0rfPsYOSNSdsROUA6PQFKxd2LAWAlvFPW2XFj_ZnIvd74Sj_DyaChHN2HOjqci6WCWaKrjz-8SCyNDP1p59YmUUY-jWubdQtroQ73PtpVga2L-Ev-DeKw2Wija0fXVcRqBkgU8e-BuUl5TTcU5N_j-XcBBxYFCXg; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiS1pibFJ2RU9rU05WN1FOdkdVaV9jdyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTAxMTUzMTcsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkwMTkxNDIzLCJpYXQiOjE2OTAxODc4MjMsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.HHjJ6uBgF5z3xJOf-YRQsBRzmr8JR-czzhnVxfLCStxcxkxJp9ORxkC2z_dNAUAwYOAeZNoOaZHvi-pjAa17ZAuc_4j2jjofRmSKtNLkOmkz0-QfjYX7j460Tu_zeMpqpTKHkUjOQVEyRRLc3zAhBJv9BhUZYwYgVj2skkcVV0QfiEvTgaDnFZAAk86HMdQ6FBG1YcNfHj6V_Btx7NWw9M6LTMqA3S2otn9q0GAer2i-p9x-T045DKmM0zE6_nmRiac0ofcTedC-B_kAN8kVim96dAspqhPa0nYlOcLTFVidBcB1VOP-PIRy69cCb7maUZ2TPQstblHOLP5aszQJ1Q; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': '1YzQ9ira-wU0xPTHTYKvg5PL92UPyjCmACqU',
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

def getCardCreationRequest(reward_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'reward_id',
            'value': str(base64.urlsafe_b64encode(reward_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params = {
        'service': 'REWARDS',
        'entity': 'REWARD',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for reward_id: {reward_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for reward_id: {reward_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/reward.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/reward_output.csv"

# Read the CSV data with 'reward_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(ticket, reward_id, dbinfo):
    status = dbinfo.get('status') if dbinfo else None
    row = [ticket, reward_id, status]
    card_results.append(row)
    print(f"Appended row: {row}")

# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        reward_id = row['reward_id']
        ticket_value = row['ticket']
        try:
            print("Attempting to get card creation request details for reward_id:", reward_id)
            dbinfo = getCardCreationRequest(reward_id)
            print(f"API Response for {reward_id}: {dbinfo}")
            append_to_results(ticket_value, reward_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", reward_id, e)
            append_to_results(ticket_value, reward_id, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['ticket', 'reward_id', 'status'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)