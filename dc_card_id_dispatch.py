import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=odX1HvdlQcUs1rgO8qbucsZZ; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.vy-1M5pcFnOFeEpFPigoHoj09GZh2PaHUTTFx9uRP4BrlIWB5bIPd4CWmBcPp2WnkGj0j9GKvwyFiQtkz6X8o9lvFsjBzRCGg9yN7ltO6BBgUpBSx7StekJuugPoZr2anzK74pS8AdT9wakWYAgavJs4DHwWFyqKfiGrEo_m44yUP8FtdF7kQymL8dhHp05Bz4nE8NXVcpxeCia7yAkoATLO9-H7xW_1cRaNRcMgGXd71gnTrs5iczLltMzDd1RGOY6MAHWWGsrDPeQwew8J9ikfmPXpOTisIJQtDbAbwhHZZIOK2j5uNIJenjTT3nAxtethppSB0l7Ht6RSuDQBlQ.kIEhzp2D65vGbDZN.w0Vs5MoeBETjGn_PTmxek-r4G4cwtcFWfay4A2AsRZIQOPUObfUTr9_hljtzPZrZpw1jGR28TEOz9ycYRa-7k6xGWWEj0bvmEZ3qLmXwCgvgvTaq6HgixT4a0cOD2BI3CLpMQ2_00o2YlyeE5_1J2c_dJkb-sBvS6I6xs2kkpMAMufQn5cE47HMHeN2-NBGNVv_r_MVeeoEn4i5uKBzQGGYrRjNxq055emAD9u1fj1ZeOSqOGi_rrGJ8G0T5l2dQZTiREEiHc5S5QvS4KHtNwslh5xv8YJIsjwY198ln0H1ECwWq58CTwBwq5x7wt-RNGBZc7RBlfgYz97KscHiY4BQ03-rLKHncw_J0G5cmEpMTqLgFyYtrSj8ehwAXOKh5uFyr4o5XOskffVR53sKfQ4W3v7fJ6vjdJnJoVd7HM_5OI1Nd748shFYyPQHpvSc7KthtPZzrABZPAlWFxdr74gyV1z3-0LR17MBHqCvLAqgOAm86Q4eF9Pld44MIsPDcdMvLd6R7_YGSi-itYF_P4WRERVL9FaV57Aptc030nVm58Gu96B19uDfp_VkFGcEWrjboDUdfFOctVTNE25RqqdRcTjwFBrqbSUsjRfTu7EA2znuMDGUj3KtxersFZLLw4WGEj-iCRG-9C1Bf-m2rNr9KCM9L8MncgoUcMu3uOMR-Fjd9v8GSP_81LUwFIjjqLyGBQkpmLfBE15P4Bnrs19lFCFOzCrACswdA4FvyL-VjA1MoZHjTIJecKuQtknB4Zuo6Kj5GQJQfO8n2i1XkIgzPFsqMzoS8k9oetgbZg_vAsAZ0W82ZaWzZZhwuwDZVntFXbv2lPwADQ3bMENsWK3yGbrNqizgdevwcazjgPbwWRhJJWfFSKVMKc1fn5BitanNP7uVppFdUSSuGb9oJsaGDJBhpVNMizViQTJ7fBKrTd02anmsfzXd7aYIu29yQnt6A52OIhK8b1Ca5XkVYeikTgj3liR0-GKcPJywKEmgznQfW1AS0-y3AfP6V7EzV-xkEvcfgXhzOHxvlIzbGDtY4wFHREPi1E1ejGOmcK5gXV2DJV4ZiRNwcBAW2MrYfLn4byeUhU75n_rN6dhWEeBS7QtFEXitNV5rvCzMYU0yBHeq3EQichYmI8MG_cJtE72_DO6B71N43dAa8aS2MxLdoNt65felBjXIGkNUwFHbrs-ifBsJkxas7CogY3cBsi_v62MB680c3uvgqhU90OZiZAH2fO_xGDisKUdmUageB7edVek_W75JwXRN7sOeoSJquZcLvUi98-HFKbA.8dR9nydqNIim-0XssCA0Lw; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTkyNTE0NjYsImV4cCI6MTY5OTI2MjI3MiwiaWF0IjoxNjk5MjU4NjcyLCJqdGkiOiJkNWZmNDc0Zi1iYmIwLTRlZmMtYTgwOC1jYTkyMThmOWEwN2QiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.IUWTSxc0acMSLh8nDOQwwGhNGq3NJcTmVOhg8DRsyLz872cjPUIhlZ1N0HYNFEsl-FejdsrK8XErQBNoOTCZmk3CXuoCAhvPDogIibvNHckDtaQ6hkgt55xZYNGieHstYVqhwmEku8iSy_uMQL6awhGZpe4FKzewNq_c3dpjkJ99ZxK9lTKkeOtkOD-kliYbs-cU8ZAgwsIvxKTRBN2pIHfY4zEJ6a-ff9OqaGNtlb3Zs4nr5w41BMIHAIMGnM6MDKlyMJr2HV0kpRdMk1uHV6BooqsnNx3f8OtO0fp2sLZ3rWplPH6M80edDKPnGKmMV8csuPY6kcCUHOXRpJ7G4g; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiOVpwTDRfOVMxRGNIQ3RaNTlVUXI2QSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTkyNTE0NjYsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjk5MjYyMjcyLCJpYXQiOjE2OTkyNTg2NzIsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.eFOFIsZxR_pEzgGnpEF8hMgUBBkJyZ9MnrbP95YjseimOTm0rwEVCNmOokeB015---nlvl_0glGQEKxPr2PNF2mogjPch9JZrUMh--uB5UyP09d0mb5zNWyGdGh9jo1kLFmjgEpZ-vRDZLHasRnyxnyoGoc96iAiIPruOOKo-iLKza718nnrpi5sG7pmMcxzJ_xxUsVCEBsHFuSbOJE77vu2jBGXMuNg6yYwb5c4XXF-f9nfo8Dolz-Fl_mBRcU2rAzz_a75og0ab7oXz5PvbNwr7Wfa4SirKgfhuL2kez6b8P5u4yvCWLV_HZgZdyI99U1iQVPVKv5ZqQRUOzPnCw',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'fUQhOpAW-V85SBQeXppOr8mUHQJzZZGBd7Bk',
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

def getCardCreationRequest(card_id):
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
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for card_id: {card_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/DC_physical_card_req.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/DC_Physical_output.csv"

# Read the CSV data with 'actor_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(card_id, dbinfo):
    if dbinfo:
        fund_transfer_client_req_id = dbinfo.get('fund_transfer_client_req_id', 'N/A')
        state = dbinfo.get('state', 'N/A')
    else:
        fund_transfer_client_req_id, state= 'N/A', 'N/A'

    row = [card_id,fund_transfer_client_req_id, state]
    card_results.append(row)
    print(f"Appended row: {row}")


# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        card_id = row['card_id']
        #ticket_value = row['ticket']
        try:
            print("Attempting to get card creation request details for card_id:", card_id)
            dbinfo = getCardCreationRequest(card_id)
            print(f"API Response for {card_id}: {dbinfo}")
            append_to_results(card_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", card_id, e)
            append_to_results(card_id, None)
        time.sleep(2)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['card_id','fund_transfer_client_req_id','state'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)


