import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.g-_O0eXhQ5VAvqPyLRQy2JH99FFp-vlq-EcRHK7-6zIPmGvY_zxW8_YxRQUoJYuhnSxA0sA2FSc0JecJn6YVW99fCVl_G7mRGcuVH4VTEEDnAqU3cCY6x_QrlPX8etW42J6_KlrgAxyXG4cur6hwM5Zoh9FXQc-woETXm2FmQ8GK5PVFY6jU5gBWpD3eKuR2PwAIYAgYCA3gzJz6WFaKjHr-MfL0ZfV8NKJB1I1f4UuP3Qpn7UcXg_weV7QBfGhUfmlFzH-pCzehEIyUHQ-FU4vr7JPv6BI5J1lGETjyDqL3O9T2FUznwOa3MYLgZkZP2MCo9c7lLgr7K69JVw8I0g.6BS17U7_0zPPJW5Q.ah_FMoJVik7XoYNvcOxcH8YL8GtgMhkDMZNjM7GYDbfVnyN7bMGrkqyiDgxfe-c2sIaHmBUGoX-cM87KHdvCmriNrIFN5ZI_eSyKh6VRdoJx34xmPfDX2IvOd1D3igBFHcqCojzXFwhA0Jc6Kir9Ed0EdIfv6iawaGSPaKyZmLAkBcFiEW8IYqrXgujCdaeR4KM4xQ_X3yunpA3mCUDNbedOnUXSgZznTiWEA8W26hvV47te6vfJIofIZxQIKV5s0HyvyUQw2L3GT5EVxtz3QuU1TUGSREK66T7-ua1eLe2dTk2jlzpAXUB3bqtEZCMamUNBoFVCCKJ2BkUYevtmzSWmNM1C8odeFR5oIM1XLifH0Xn_zr01_wmaYBG3rsp88UChenThsPOFyXafMhmWoiWDXtryXddWXQIRRdqNWt0vcyDrdOWHb_gwoyzDttzx_3Ii0QSMhNF4n_xsoY_1H6XPIMDcPubsq-Eav-qckfuHjQ3b_Es7A_etcqO7PTY6I1TFFlVp86sIUubessrcXC-5jZ4VcHDYdPHVQea32pjNJDVsbXicX1d1m957qQxFmQbXgEAhdNsWZVYv7_lfQaQufotxB0dhopt00Ofd1HLBSIbf5XoW4rhkoOmbMPujjmmfsVymFPLzEq3Z4QPN_1gqlRSoF6e_j5zfRCRiUnELWcYSU978YUBukPpZX6rTfEDvpJapT_uRu56cGvMwJn4CFJbcPELARO0z0zYqVHGg3HdmfCn8HOZDQvEC0sz502F51Wm3fPeHQTVw3X4MDLkgQtYtBQgudco2z-_NvspZjwrpThiEiz_L9rqg3VIpOGi5BIac0OW1HDXnVvoGBZsU6JzL0GXBpe50cN4UJubF7PxjjbcIw90c2xf03gIEekCD93iaIJflOhzXuTB9jBQnq6kNiJLOwpPRI2WBaEdw7N7t8p_CXR4F1cMXDdFpVqOmSB87vivakklhBHz8Ogc4zO2k-aDsFUyhI-HHNomxXDztF36aFrYOVe8pPuYQ-oEyqS151eJNjYTBGxTOIQ8oYtnwEic8HwTVPlpwAp2V3jQJg-1XDgg9Fe1yiNi_r3rHq1zR2yvvMAx6Q3_85ssyO94S9nLiwJzM49_zDJ2Ywc3GvMKGPLz6N35SqBe5cfSrs2wBZVrB_RjGF4fgg0OCBO-h3bgdnxTwDGjVrBdgjTXyOTX7bzxZST3vP8nvevoNpJ5ktYqRp4pkEcUjOGGKMOOPs67NgSSq8AiNcNNW4l063sNf215J3xpWuEhwnq9BtX766r0eqYaGig.nFNcXBiqx9ovMvm7k4r03A; _csrf=TNdJQTHZ3DOahNkolmDWJm-k; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTE2ODQ1ODAsImV4cCI6MTY5MTc0NTA5MywiaWF0IjoxNjkxNzQxNDkzLCJqdGkiOiI5N2UyOTMxNS1jNDQyLTRkZWItOTcyZi03ODVlZGE5ZmEzZjUiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.ELZ6Mx5nsxXTkQh6xUnNkeYBQDMEVCw5rdu_al5zULCw17TkVvxoeIbqVFAv8aFsJZ5UDfodsJfzbEiaxlrrVAgJL7RSeUpiMsU_W0JRf6S6PXjjfHBl0-Ch3X72GUSDdV3ljweCV5iQv1kqNK1b8wbW1_xx5lvuL0q72t3wHlyV50PEeYFavv-EkIKUEdA6ISwFCp_8DM2oEkhYZh_3gJJ36MwS6tBmRVOAZhxwm6ZjOLet2taty_9WK2bZGntDEnhzOINKg0_1FtGidGltZqiQN5IPju_fmn5cI6dmXEOs_5WqSHfJm1FxBuJJhooxsGCxzWDo3qjMBmRYhSkI3g; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiN2dLU2p6blVFY0JkdXpYWmUxWEtzQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTE2ODQ1ODAsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkxNzQ1MDkzLCJpYXQiOjE2OTE3NDE0OTMsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.l5SuyvN9411txHJnBGMbXVHWCYJSAau_ymuvaONX28zkiCsUu-0wKkBXtg06s1ZRGY0pfIlDRPYX36pd__hVQx9MCkvHH2IIApEx3yb9ePnO9RFRblMt9ZW-8_ur3WmMp2cEGZtJaxO_BpPpBkPf6dY7vQiLuxP5DX4FshVfOhBpEgyjN7u1PqsFQKu5YtgK5253HcYpyHKbBFnKTgq-nGzlR-k6i0LPxrTBjmXOQvNy31EJjr8HfyeiTptAf-I866AKgnfttkQj2FwKmrvVL5dqUkMMPsmXIkbAf1gEgBtm8fyHGhbNxRMR_duszKGVlRj36JW0CWnKUVLw5yyC9w',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'u4R4jTrf-r550ukz7UUvqGG52nCj9N20Bi0g',
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
        raise Exception(f'API call failed for order_id: {order_id}. Error: {re}')
    except (KeyError, IndexError, json.JSONDecodeError) as ke:
        raise Exception(f'Error parsing API response for order_id: {order_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Downloads/order_id_input.csv"
csv_output_path = "/Users/shariquerahi/Downloads/order_id_output.csv"

# Read the CSV data with 'order_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(order_id, dbinfo):
    try:
        if isinstance(dbinfo, dict) and dbinfo:  # Check if dbinfo is a non-empty dictionary
            updatedAt = dbinfo.get('updatedAt', 'N/A')
            status = dbinfo.get('status', 'N/A')
            uiEntryPoint = dbinfo.get('uiEntryPoint', 'N/A')
        else:
            updatedAt, status, uiEntryPoint = 'N/A', 'N/A', 'N/A'
    except Exception as e:
        print(f"Error while processing API response for order_id: {order_id}. Error: {e}")
        updatedAt, status, uiEntryPoint = 'N/A', 'N/A', 'N/A'

    row = [order_id, updatedAt, status, uiEntryPoint]
    card_results.append(row)
    print(f"Appended row: {row}")



# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        order_id = row['order_id']
        try:
            print("Attempting to get card creation request details for order_id:", order_id)
            dbinfo = getCardCreationRequest(order_id)
            print(f"API Response for {order_id}: {dbinfo}")
            append_to_results(order_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", order_id, e)
            append_to_results(order_id, None)
        time.sleep(3)


        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statusment to check the DataFrame before saving to CSV
# ... (previous code remains the same)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['order_id', 'updatedAt', 'status', 'uiEntryPoint'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)
