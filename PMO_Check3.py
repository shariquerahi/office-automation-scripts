import requests
import time
import pandas as pd
import json
import base64

# HTTP headers and cookies
cookies = {
}
headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_csrf=y7or7gpPlYlz6jQKsIjwwgKl; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTk5MzY4NTUsImV4cCI6MTY5OTk0MDQ1NSwiaWF0IjoxNjk5OTM2ODU1LCJqdGkiOiJkNjRlMDZkNi1lNThkLTRlZTEtOTVlNi0zZmQ1ZWYyNGM3YjkiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.em1RAE_1DymjKPg6kr2TLLgFmM9GFl7wm3QtRmliJkbifcrX5UV5pCKQrOvJhofyxAjhniEn7MCyi8pH-st8Y95764KzTa2kdRjtUYh_ydS606I-2k6lD-ZcQjBVNySs9LtEH91FA_exR4Jwnw62A73FCvMbgy9Yd6b4OUBvj3B3849LCze3IYEzOX8DITSUHWtnv6RAVc3LlIuQ7l7IFb-pmhxA-0xyeGLRZeMFYbFhw_GXJGO6ryy1Sv735yfoe6J_iQxPYSigzk4Wyd-wLiJ6NO8fXGg7jO0SbHstvspqGf__x_f_6M4K9qbLFaN3PDK4TvMwFX-0fkRs3cZ4Pw; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiZ0NkR29uTG9qUkZpZldhM3lPUjNXQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiZjhUbzNfbGpvSUxXdlItRnBJdXpTZ0l2TTVwMERWc1VvWFVJdElUZ3lscUlVYnRGS21EZVJDYlV2S3JUdGN5TE5HQkdQZDdpZm9TRFdqa2RVaDExWmQwcWYyYnpDRmdkZWkxRFh2VkJ0ZnpObWg3R2FKd1UweFhSVUZWN0VGNllmdndYTFNPZmxLLXQ3Tkc2LVNBU2J4a0hRQVl1dEs4Qk8zMWV6WkFMVDRFIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5OTkzNjg1NSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTk5NDA0NTUsImlhdCI6MTY5OTkzNjg1NSwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.UI4661nwJCGIYwzwt861klkjY3e3BUETmoyr9viht4Q3O7UT7IU89NFzt4gQCXc9ll1Ab56u1VxezYRbHzr6B83aL6FFVoYdXHPTglPd9F9xs2ugyxHTN17AoJdyiLssgQ0AqzTCg5-dVSxImoEtuMkhMhMN88aNbmifGHc6udQ_fmWwoCMhtoeOq8HTFg7BKKD58C3YpblZz4eukbok5r0QnLlWuogVeg0Cm8THT5XhL2_BiQ-H8XhD5eDQjuy-lTkKJF8OZ8s8V6e-U8clBDQ1y5mQ1POMJyIfIEQ-74uScrbmHhO9yTo3lZ4pK-5r76YWXx4x5fYX3yNLVC85GA; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.PpFFjHuM9vv7Jsm3VqKo1Iwrj6WgR0p5cViSNFdSCTbydbTQjb4hGzUEw0ZGpFN1pM99I7UGByIodYp3LSM59bun5F4UfpRPMzFRLJXmf-Aa8Gy6kM-9_QoISZ_mNoranYSEdBymfeNYEn_KMy5c0TvAwKqAFSbpfq1SKA6RHm3ZLLepZwNhXOwvDlq1no5yYovZQAegDyW2OgBXUQhPwDmoLSKHKLLHFpR8xR7lPzTcHjxqdzry1OqvbpNnTM7tj-iaesLe5HuEWgAuqec_yBihl5-flf8fl1Nn21UtER2B9bTQoa9OwxVx1_FcRn-sXnX-JRoMVedYbQdh22USPA.jEm81pXyFBzSR-Xz.Ca2xzb-tO1qM2ttnKC3G0_Ph90049amX2JP2rL7T2xOHnklQ5hMkzV5bg1tqAydl33H7SMtvfNi85yiG8ozS6l0IvaYHwnIXwFn6TW2Nx_bFGxJDEmQgZGtxXPl-l-FESMHwLRo2cBlKSN5zw6CEmu6SciT0B_PCcQ3fXFsXUmdUymRdBEV2F3YKX1CH6iefH9fpa1WU4__Rj9ysnyDby_mbl2A3Fh6RW335LwkiZVegCQrsiZSI_b4STHyUkmcoC3UjszyrzbrVVyuF0xBmMbFwA0NU-_NsfAo7XmSiIwXUOEOHK0rs4fuKpweHnG5aOUF_vEos-mTCBJqxWJozbMokwq1Ll4iXpto-VE0dMqj2V_NeIi0C3PM06TsebTa-ZzIEhGOpLdEFbEKRD8U4_5Wpbq9LSN3WNfX0cOprI1NLW2DmDZuGN_XLHkHp8tMSgf9eFo-Pd0OYL1LAhx4uRJ7iU0wDgf0avFOjX5j-GNCGhnyJmiwViBuoJbCj4ryPipHUK9vh5M837rPFNUfL8-n7YjfqgZltKi3kxyoCW81sQsT45WLK8LkIE9fh8kwDc0HgsJuztyQ2MHPPgwIk-FxRVMrW2k1ZVkBc0Yn29ZpH226sDVg6iiyrluH7bHpXVOGTsA6Xt9dX_Q_4RqMCfpBVgUODPU6hLp0PUyvmlK5y8gHOqFgUbZuT4QyrwKe1NWgfKVu8dqAVUymTbp9ptJG_fz_93g2zmts1SncHaGwW-Run9gLxxCNiIZWZzB6Wil4vO6zHDslR3_cLof5Vcq1BO24uhwKMNNBrE8JN1fSwNH3U0fDh5RLklCdJ066sXZDzD3PBznwFV-EyUxxN5qClXZz1THUk3GpuX3CzMK_swyDoXlBLtd0PR7mOBbALgO8PvZg1csHSR-OkCMt2AbdfEmgRPR57LjCUBw5CV871tjp9ecvsIGaAll35nIUuHl2dchz0PNcJofb8PTTSZeAa23xEahRtd_AzNyhOsRqn33R4yNEHfKP4SodyG9ialNgFlJqqSvwOc0VycdWXF5L3SwbrfZ_o84mid0wEFG76DQudsQIBElHwtiNHVhR-7JcT-CAiuAq2VCV5eW5eM7t1oTjB0MMxCA-rzwhseDXH61lDvgNPoAMnmyJ6r9jOVhemmwIPCg6pmtmsK6BsoaNa05BzA8gx_JunEh6wlyGCpbty0fcWjI-H78WU_PgqymLzOEYrg01lQdDXTBPEa5h1uR5AuQk0kEzteEhGqPlIpcoDNN4wnJsUQKT021KaQc0ARqAxMID-qtXiLA.LCk8tG1k_shKMvYWhAaZDA',
    'csrf-token': 'PPqEazPT-Uwm4_TRzcg0rVveaBtRRWsG6NFY',
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

# Function to retrieve ticket information
def getTicketDetails(ticketid):
    url = f'https://sherlock.epifi.in/api/v1/ticket-summary/{ticketid}'
    r = requests.get(url, headers=headers,cookies=cookies)
    try:
       time.sleep(3)
       ticketInfo=r.json()["ticketInfo"]
       return ticketInfo.get("actorId"),ticketInfo.get("status")
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

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
    
    # Function to retrieve card information
    
def getCardCreationRequest_1(card_id):
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
        'entity': 'CARD_CREATION_REQUEST',
        'options': json_dump,
        'monorailId': '1',
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfoList = r.json().get("dbInfo", [])
        if dbInfoList:
            dbInfo = dbInfoList
            return dbInfo.get("requestId"), dbInfo.get("state")
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for card_id: {card_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')


#added  PHYSICAL_CARD_DISPATCH_REQUESTS

# ... (previous code)

def getCardCreationRequest2(card_id):
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
    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        dbInfo1 = r.json()["dbInfo"][0]
        return dbInfo1
    except requests.exceptions.RequestException as re:
        print(f'API call failed for card_id: {card_id}. Error: {re}')
        return None  # Return None to indicate the error condition
    except requests.exceptions.HTTPError as he:
        if he.response.status_code == 500:
            print(f"Received a 500 Internal Server Error for card_id: {card_id}")
            return None  # Return None to indicate the error condition
        else:
            raise  # Re-raise other HTTP errors
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')

# ... (rest of the code)
def getCardCreationRequest3(card_id):
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
        'entity': 'CARD_TRACKING_DETAILS',
        'options': json_dump,
        'monorailId': '1',
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        response_data = json.loads(r.text)
        dbInfo = response_data["dbInfo"]
        return dbInfo
    except requests.exceptions.RequestException as re:
        print(f'API call failed for card_id: {card_id}. Error: {re}')
        return None  # Return None to indicate the error condition
    except requests.exceptions.HTTPError as he:
        if he.response.status_code == 500:
            print(f"Received a 500 Internal Server Error for card_id: {card_id}")
            return None  # Return None to indicate the error condition
        else:
            raise  # Re-raise other HTTP errors
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')



    '''try:
        r = requests.get(url, headers=headers, params=params, timeout=100)
        r.raise_for_status()  # Raise an exception for failed requests
        print("API Response text:", r.text)  # Add this line to print the API response
        
        # Convert API response to JSON explicitly
        response_data = json.loads(r.text)
        dbInfo = response_data["dbInfo"]
        return dbInfo
    except requests.exceptions.RequestException as re:
        raise Exception(f'API call failed for client_req_id: {card_id}. Error: {re}')
    except (KeyError, IndexError, json.JSONDecodeError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')'''


# Append retrieved data to results list
def append_to_results(ticket, actor_id, status, dbinfo, dbinfo1,dbInfo2):
    if dbinfo:
        card_id = dbinfo.get('card_id')
        state1 = dbinfo.get('state')
        card_form = dbinfo.get('card_form')
        bank_identifier = dbinfo.get('bank_identifier', 'N/A')
        masked_card_number = dbinfo.get('card_info', {}).get('masked_card_number', 'N/A')
        previous_card_id=dbinfo.get('previous_card_id', 'N/A')

        requestId, state = getCardCreationRequest_1(card_id) if card_id else ('N/A', 'N/A')
    else:
        card_id, state1, card_form, bank_identifier, masked_card_number,previous_card_id = None, None, None, 'N/A', 'N/A','N/A'
        requestId, state = 'N/A', 'N/A'

    if dbinfo1:
        client_req_id = dbinfo1.get('fund_transfer_client_req_id', 'N/A')
        Physical_requestID = dbinfo1.get('request_id', 'N/A')
        Physical_Card_state = dbinfo1.get('state', 'N/A')
    else:
        client_req_id = 'N/A'
        Physical_requestID = 'N/A'
        Physical_Card_state = 'N/A'
    try:
        print("Original dbinfo2:", dbinfo2)  # Add this line to print dbinfo2
        if dbinfo2: #and "dbInfo" in dbinfo2:  # Check for correct structure
            #dbinfo2_data = dbinfo2["dbInfo"]
            #dbinfo2_data = dbinfo2["dbInfo"]
            awb = dbinfo2.get('awb', 'N/A')
            deliveryState = dbinfo2.get('deliveryState', 'N/A')
            pickupDate = dbinfo2.get('pickupDate', 'N/A')
            createdAt=dbinfo2.get('createdAt', 'N/A')
        else:
            awb, deliveryState, pickupDate,createdAt = 'N/A', 'N/A', 'N/A','N/A'
    except Exception as e:
        print(f"Error while processing API response for client_req_id: {client_req_id}. Error: {e}")
        awb, deliveryState, pickupDate,createdAt= 'N/A', 'N/A', 'N/A','N/A'
    # Debug print statements
    print("Extracted values - awb:", awb, "deliveryState:", deliveryState, "pickupDate:", pickupDate)
    row = [ticket, actor_id, status, card_id, state1, card_form, bank_identifier, masked_card_number,previous_card_id,
           requestId, state, client_req_id, Physical_requestID, Physical_Card_state, awb, deliveryState, pickupDate,createdAt]
    results.append(row)

 
    #except Exception as e:
        #print(f"Error while processing API response for client_req_id: {client_req_id}. Error: {e}")
        #createdAt, deliveryState, pickupDate = 'N/A', 'N/A', 'N/A'

    '''row = [ticket, actor_id, status, card_id, state1, card_form, bank_identifier, masked_card_number,
           requestId, state, client_req_id, Physical_requestID, Physical_Card_state, createdAt, deliveryState, pickupDate]
    results.append(row)'''


    '''try:
        if isinstance(dbinfo2, dict) and dbinfo2:  # Check if dbinfo is a non-empty dictionary
            createdAt = dbinfo2.get('createdAt', 'N/A')
            deliveryState = dbinfo2.get('status', 'N/A')
            pickupDate = dbinfo2.get('pickupDate', 'N/A')
        else:
            createdAt, deliveryState, pickupDate = 'N/A', 'N/A', 'N/A'
    except Exception as e:
        print(f"Error while processing API response for client_req_id: {client_req_id}. Error: {e}")
        createdAt, deliveryState, pickupDate = 'N/A', 'N/A', 'N/A'

    row = [ticket, actor_id, status, card_id, state1, card_form, bank_identifier, masked_card_number,
           requestId, state, client_req_id, Physical_requestID, Physical_Card_state,createdAt,deliveryState,pickupDate]
    results.append(row)'''


# Set input and output file paths
csv_input_path = "/Users/shariquerahi/Downloads/dispatch_req_failures_report_2023-11-06 (1).csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/outpu_Physical.csv"

# Read the input CSV data
data = pd.read_csv(csv_input_path)

# Initialize results list
results = []

# Loop through ticket IDs and retrieve information
for ticket in data['ticket']:
    print(f"Retrieving information for ticket ID {ticket}...")
    actor_id, status = getTicketDetails(ticket)
    time.sleep(4)
    dbinfo = getCardCreationRequest(actor_id) if actor_id else None
    # Retrieve dbinfo1 after retrieving dbinfo
    dbinfo1 = getCardCreationRequest2(dbinfo.get('card_id')) if dbinfo and dbinfo.get('card_id') else None
    # Retrieve dbinfo1 after retrieving dbinfo
    dbinfo2 = getCardCreationRequest3(dbinfo.get('card_id')) if dbinfo and dbinfo.get('card_id') else None
    
    append_to_results(ticket, actor_id, status, dbinfo, dbinfo1,dbinfo2)
    time.sleep(5)

# Write results to output CSV file
df = pd.DataFrame(results, columns=['ticket_id', 'actor_id', 'status', 'card_id', 'state1','card_form', 'bank_identifier', 'masked_card_number','previous_card_id','requestId', 'state','client_req_id','Physical_requestID','Physical_Card_state','awb','deliveryState','pickupDate','createdAt'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
