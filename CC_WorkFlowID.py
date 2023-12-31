import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {

    'Cookie':'_csrf=OiXhHgGRUoZ6YC2eo-ULlujE; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTU3MzkwNjIsImV4cCI6MTY5NTc0MjY2MiwiaWF0IjoxNjk1NzM5MDYyLCJqdGkiOiIxNjdiMWYwMi00ZmE2LTQ5YjItYWNmMC0xMDI0YTJlYzZmNWUiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.FWS-ZiRIgLob-Epokgda9hakzFkUk8Mvedi1TeDAgr3REQdB4vuwpNCUxhFGraFDLLaA4Sii40hwZ-eRzSqDcwKkgMUO1f684cSUppT3JwpphXSVWMWDvNRo1sIzXDOlhIP-NzzJVSCbT-wE36cWBZWeVrN1vazSqOK6lmWK7WZSsXeT3Q9O3LTFZEvuhPKH78tozCnCiNBacwdwY0TrjeDVJhjRtShMx_1ZdaU0XGbzC_x-591pdk9FDF89jJb05uvdEQq_Jnu0aleZj9Ynb7P_l1jcmZN77NHP9QStUrV6C36EDUgGOuduQVZn_cpxwMCMsKrIY2hHTBr5z-MpwQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiNWJGYXZRaFZlb1h3VWtGYm4tbE5MZyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiVXMtd1NxcmJLbmR4YTg5cUNDQ29LQ3pYcDFFUGplZzFUX2tJdG4wcThaamFWcm4zei1JOGVrWHM2YUR1YllHVnQ0c3lZS2MxOG1PVzlFODZuOVEySWREZzlJRUFxckgzM2xnMnRwUHlNTjZKZEdNaUxWVUNBVUl5aFVEbi1UUGNxekloZUhMRHNPN0dPUnRTZVh2VHlHRGZzQWUzbTZ0LTJQUklSdDI3SGFRIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5NTczOTA2MiwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTU3NDI2NjIsImlhdCI6MTY5NTczOTA2MiwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.ApvCW4-xF8zfL3_AsehBlaCL--2JWiKCkDF4v_Ekup-ofapqskzU3M6ft72oLiSOY0YA3DHCOIwJ5tUceJ6MqvoZbhR6EPZ_aEd22U6Ahd9o404lvvrftCHzGi0dBDCcrcHlz44pEsbV9sqJZyYJvoDIsYsfKpxm-DsXw1fCuDAJGKZrmcVm5FeKW2KShyuq9UdiBzG-cIHhQ_U_7sJlzppmextZkzQ8F3qZUEvUINDgoiS72fVpK8jFhHvNx_GeVmlC5x9hwew60wz6Bz1ByL7QfroK0RpOqVrINKwYIN_iaicavyz7nAbPpHGMoPiMHhnQVJGSVyCY0qHGVD5Fyg; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.v3VoCAuBbcRIZwU4ScMj2QoomCYcjJFL4KxRXG5xU_FL2yWqbgZp_LMMaLFl6c-GJbt4S3pHWGRnK--rjm3jhoOoC2iA3TNh2ZhqSMqowNqeBhbh6U9SVJ5Hmu0Z2KKnMWAyTK6eGRVs2CYL-Gc-oLUAGDomR4bBftdfSvtD1OaaWDiEBQ1Iu-YUNZ7iR33L87BxU6M-GbCHuryZHeN7fP1UsjOMm-DzY7BF_IaAPLAWA3FAskTrHLqCT2tCEwpV1EIqF0fMmTK2h2xgZHRFg3tyICta5VuD-jeDPzSrMeH-UqxhruZJPOv5Cb2DF-NH2Iuwig_VO2rm6_MOdfRWDQ.yCwD-FLK6a8pgBSO.FeypIo-PW0XiiLlFxGC5EpxxO9bPyDMWbUdIoTALm-8QMzXKH_AYvySX0NDffUju7BEiToEFEjtvD6SRV5BLIBqBwjhBf7CD0rBm8VEeEj0lXLLYq8ZZL2xmVzTKRoMQ6XRHZAx3tmqOIR3JkWdRceD9vxy_gO-nUf7Jrfi0FPLr3AMYJDHCY96IqBMSIMa5tpeNyga9-6lY6MT6bYo9NlOTbTCN--rdxGYpm8kG121_4m1McmV1_i2k1nkY-Q1d-BDp_vrLp-MhYCm30jlnjUxQu9y4A1DLNO2INiiw1BfTU8jNE7B4ET1_ZjiXyVVuQSKyhBSYUA1kius8cQerVfBUwhyVZLrI59ii84sHyFTWhYmmqUuy11DysnE_ZsP1Ob6OYO0IXIav_ZpS9EB5XZgqfTW3H_xVTbVivQ7Z53FVtPOJuTXOOty0bpawFRYnV2M29gA65uDnjVb4nt-x5gU0lk2dot_81YBIHhsfQzBnJx6nFAOefuFbYkfhqcfJgREiFykk6a84mf7P6f-GKsO1BWlL6C7c5NWNxeyURTvy7Aj6u8VADPZpjFQjvqTOLKduROxpZUvuZBHVgGB0GuXM6s0w37-nKrI2twGxRSIIlKjlrL_Y9yPlmdcnWpkY4jUKw9YC-ljbBo_RxIF6UwJ6FPwR_gUGkaV78iFb7HwbjDwdLGuddjoEkKfP6dujJAaCFFLiVGFSTyxXTcKAgmR1roW1wJVAClnhmJ1TBH83FeIE6RSfC1fbTlwyWDJ-xUFC_IjODvugiOqhTcy4ltiDKxqsyunZiq7Y8KJ0Obs0sxaA8lqTiiaLOqmGBQ1MRCxA5TIzM7I_uw6SZDjdsrIQzvqwlOei-tJ-XXUqSitANmhV8csCC6KyXcbvCSH89GzH6lsJbAWVtCklgv9RoZns78wAmR8qbJPw-jCybRUGM7X5ovxl-cQ7TqJstb2yGVFqC1yJ5F1MC9tJlF_9a790lzhJ2RNRsy1NtOQUGWw1sy-bwDXeN_A_ff3nedzcAMaUVc6IJTRZURinKkFdhQGdb7oO_G-vxJwfxG1rEvXy9K2U8dSV3z6lmdX7LarmNQhzIZztke25uLuWXVBSJCdKceAXP4ljnWYXzNjjrrPCuT_lHd5ebHSTUu7b2AY-rPseMSUUPBdOwgzUlF2xvR5vqdsEmfjDhiu-PMnANVb06SRWbOmnzlxOyriehMbV3ZwXHEW8MRVZ-ny4tqDYYGQmTUg6AJcI9PAAPgiNDMZQ4CThiPf5NDBxFBnGk_L788s5nGWyy5pmpZrF9A.7VpyvKFkiWGZuTQLnG8JzA',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'njPZ54Im-YEDJIZ3ECALCEsr-ckDi4rZsDZk',
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
    # Define the options including the additional ones
    opts = [
        {
            'name': 'client_req_id',
            'value': str(base64.urlsafe_b64encode(client_req_id.encode("utf-8")), "utf-8"),
            'type': 1,
        },
        {
            'name': 'client',
            'value': 'FIREFLY',
            'type': 5,
        },
        {
            'name': 'ownership',
            'value': 'EPIFI_TECH',
            'type': 5,
        },
    ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service': 'CELESTIAL',
        'entity': 'WORKFLOW_REQUEST',
        'options': json_dump,
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbinfo = r.json()["dbInfo"]
        return dbinfo  # Add this line to return the dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)

# ... (Rest of the code remains the same)

csv_input_path = "/Users/shariquerahi/Downloads/input_client_id.csv"
csv_output_path = "/Users/shariquerahi/Downloads/out_workflow.csv"

data = pd.read_csv(csv_input_path, usecols=['client_req_id'])
card_results = []

def append_to_results(client_req_id, dbinfo):
    row = []
    row.append(dbinfo.get('id', 'N/A'))
    row.append(client_req_id)  # Append the client_req_id directly
    card_results.append(row)

count = 0
try:
    for client_req_id in data['client_req_id']:
        try:
            print("Attempting to get card creation request details for client_req_id:", client_req_id)
            dbinfo = getCardCreationRequest(client_req_id)
            append_to_results(client_req_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", client_req_id, e)
            append_to_results(client_req_id, {})
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['id', 'client_req_id'])
df.to_csv(csv_output_path, index=False)






