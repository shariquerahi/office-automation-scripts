import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=OiXhHgGRUoZ6YC2eo-ULlujE; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.Vy-TLXMtmUTILdU08vydGM76ELSTL350FJHV8VHbvCdKqDK7XNk6QN7wkDZJHGnT-ozEUIwcvP1P70ewiRKueqLaFnI9FIXBrakNPzcLLMo0dYCXvxyv-BpQvsKW66xKt0T8iUZW8iYAOMUrFfr5FGX0_Np6IsgvGPqmGd93fLvxcw34X7LkMSEphZkPU8RjBAHvQwXPYkE5iy-pVglBWBrAmhisX-FOs6aNnu6vsGMiwPc0mwPk7-1xlfLnpnpF4NzRBK41lxXJBUsbAKQvlip-qknhC4vlAcHTuEtFcScQcevhfOwDvzh-09YuuVsvyxgmW461q9BZKsN0Llpffg.uEQ8vj43pekRPoyw.iifu9qf7n-bNKwfMldS0--nm1Qf84_AO7DBR6F1bJFA2mFliCZvrX7YDC3ilxPAIP3T8hb_DtMPjL2GZSQpUYk9rE3lM0HTsGfPY7sJIohP_jT4u5Qty3_f_t9krLVP0eRZFbahQkHPaNKP7NfG6oef0SZmokjtgk7NruvYkLSL8iSivQWuqzoOTXVCONvlGMxrovv4RIEQoZqlXIYtmphwq94n4_QcJJoA9w4GJlvaWt7sxBE8pYB5IpwYWfmE8I9XBRpHnfqxe6_abSAfWOdZA2eMc7w9PDqUfsUxN35ctUVLZHyEXuQYXFEYfNz-zzwQtkuKtkVlmrkloKItNreHKrehIZir1gKc1Kxj5wZC7gpOjm9LpYjSmPTLk-sDxB3GFC5A8M4EbCLIULm7W4ct3RsvprYoHGXgtZmMO80d77BUx67BdN4csnPZNb2PWU8ywhRffVoTtCm5avxHoXgCSn7j2olkBZBCh8FuzPUvHgyDWMEd6URzqQSa4NL6XQWEw2EyVTTlQAvJ_qlo1dPpewkohiI3wFnXHX_FCoBwPO9_BMOaDrhDsoIcgafq4kvzZLerH7mM_z2Ke9mfcbR5I5vEkMpJzFaNJERFsN9sUBjNQ7RMO5DyYF-WuCFtr9JN0fCqGxU2ibGjg8fGvzrjDWLtrchYo0QYD7Rdx6uwCx4xVK0HknuKZIhg5GILRBMXK5p8Fgnm_mrxOJjwGKGROqPv3LX7sfsn3RADtz_PnC7FAvChTEoH0P35wEA7VWriVupGMTkMT-Lw6e-kopOvY0d3geTFGdzWsL5kn5NEl9O5Jqf2Xjq9ZttXZCOYmebKLK4n9topYz-hKmAuDKRzK5A5N_ErhODfELcvEpYRXC1LxExM1W-nwsCRRdPDqT6Du8M3U_8XYAP72Qn-TN2MVOL9D33N3Z3uskVOqcM5BSKCtoyWxv06muyu6nKFnFP65tQ_iSD90QFqSos6Np68uJXY8zliuswUpu-FTaolOJ57ozC_oAAkc0O2bn0xKCt2IZsx28jJm8aWTTKTBsd7AftaKmKzY7bB7WM8Wodwho1H1Txd_d-CqYa4ifWlG-Ncslpk9iO2osvRpvDDxIusp4YyofmPFgwiRahAe5gQ206ko93cFj6aaVdDfmFSSDvZB2TzChf5VT-dJTSLUkbA31fE5GfWToN_EYpNzutL3OPSCHpNHy1CzwwJ3d8nmDWVu4PIIlFfurR0oTXMtMWB8x26A0Pn2PhkJI0d87txNHIyTmvMM5oLZZ8D1Z0bEFRUSEoZBaRgR95TcTg.qsQKZoxxUynDg7FVS33cqw; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTU2MjM5MzIsImV4cCI6MTY5NTYzODM3OCwiaWF0IjoxNjk1NjM0Nzc4LCJqdGkiOiI4ZTUzNzA5ZC1hYjMwLTQ4MjAtYjE2ZS02MDM0MWQ3MGQzOTEiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.RsHgfRv9mlXTy1bIFW6UaQFz828I5kX07UjOc3t7ZOssC_abwUAbBsBmgl6RGGBW0IQ4QNO6eKS83S80CIu2fSfKnjxZC7Y43byvZjwgvBnPKdkyp7Rza8kvRttcfG5Az7JQoZ0dmMjhwfcBwt4mWUPzHdy-ZWWEtFw2140jS0NLNby2YzrXh3L_9oU22HHoqHhQchFutEVIk2DmHaCdM9_kXzhN0w1OkTURmXlKNpbalGqqgoYL5-POMf26W1TpFr5CGTb_zxauMhaua9mrPkU2K1bGd3mciMI5-nOB1RbgjhFHJRZLhSO_pWGcCh95_qPmeuax2KNAmI4fg7y8eA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoid1pqMXZvY2RscEFrMDNMU0FNVEt5dyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTU2MjM5MzIsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjk1NjM4Mzc4LCJpYXQiOjE2OTU2MzQ3NzgsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.FQXAF29p9wgGqkAR9aNRDPz3dsxEAfbb7P9wK07r84IGQhjpOEnhgcsi3AuXuhufd-ertPPVjfgX8EMCE2CIx9_GzPW2qj8LP0pELFqvArbNlG2wZ3R2Y16I8Ze1-nmL5fulE-vWk_Yn6170iOrTP21IufX-NDiPaklZZt-vnrd323yVN-H_aqoaubTkZwNS1qyV2nNPvaj99sX6Nes6UrywrPp0Zk3pGYjIjP3HQIV2Vq0tuEn41Zrrw3lp0uzL_kHoJF_5BoULGWu-iFgL6hQBVP3-U5duUgJvuFVTiE2r89FmwBY7u0liBqQ89H28CWjUbAmgZv8JVx6FtJRE2g',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': '9yJScNrf-PKSJu87r35I52VbHDdrvpf9W7WM',
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

def append_to_results(reward_id, dbinfo):
    status = dbinfo.get('status') if dbinfo else None
    actorId=dbinfo.get('actorId') if dbinfo else None
    row = [reward_id, status,actorId]
    card_results.append(row)
    print(f"Appended row: {row}")

# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        reward_id = row['reward_id']
        #ticket_value = row['ticket']
        try:
            print("Attempting to get card creation request details for reward_id:", reward_id)
            dbinfo = getCardCreationRequest(reward_id)
            print(f"API Response for {reward_id}: {dbinfo}")
            append_to_results(reward_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", reward_id, e)
            append_to_results(reward_id, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['reward_id', 'status','actorId'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)