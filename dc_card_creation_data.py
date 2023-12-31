import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=7KbHuyvLJ2JQ6YKsgBCRrA5L; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.ZKljFOWsRqysWSvhqVpBJf_ND2LY-Oh3WXGulukgdzkGWVqOhfdLJ_Nv2sNe6azo3y5FunqmO2vQVUKESp_H7xMc_t8X2_nk9W9iYP1bjQyukwKD16cDBhJho_-bxP5NGUl1wkfe8Cv_-nx5zWlIybJ_PjEwepE72HP_crZat9xW5l7tpKdo0GUe-w3JNz6dgJWZDkN5J9linAqpugX4mIVu4K5VUw_9zH9u5GMN6THE403ADET702PnyWz0tQmKo0U4LLsL-KXwO-3sThstvMhfw7FmdmQhYrKQI819Pl3xBJZ-UmToERs3kvpujnQjSwJIwvoUagzYU1o6rdoffw.8fOuV3THyfsqGCrs.qHbGIwasXO4dF2p4R-R59XwXOLR3dSE0RIzMHb7uyOHALEjyQJx9If7SHGsvPTqjisALHCaXF-GQl6DU5GRPLcU42XUgcHTrQVianqhe0omke4Laa47eXWKCFgUvLAPpagyPZJGkFcXvDI2XtNKxmO-i4ulI8BTSvER4viAQFusc6CW4mhCMeeDc9Z0gF9zyDpazENyKQekUz6EzqB8Hu3Yq7wKYNaLfC-GOtgsLL6M2okDt7pPYTAM6mbVV56Zwg1qlZJlEjigVfud6NKypLjNz5ilbkvY-574ZepEVClGGjdTGCE_kPfQn4VcdB6IzoP4WfHVCyQl0FHp1JsNsY_bBuHP0Bx1_DHmdHNeUph2zfPXUY3zzFO9OtzGGBi49PKpKq3JX2H2dsbGlXVVzHRrxtCipKXscvKdy3kx-3_q1Ae-lGG-J_gxgHR1kHseIAt0_exBFE-64y3O1Xl0mTXG4muhBJIl8bST9UhchLjFFd1rVo6LF55nZyXa_4EtPobwv_0SkX1OLpq06i7ead9vT3doualXpBErQG5UU65yZkNMuGmxv-u5zplBhPPy2gDU8dO42_noqEgKedE2zuU6txVuXNFVKlNzApr3yaiooVnfvpqx_raWk1jDCJBnY8j3ks0RnYczlgA_LMKoRaVWBvRiYWkpyDvCu1eLmzwgmEfTU6prIYaIdv80Vvt6qVhK9_TW3Q2uH--JXAlSYuYdRlS2b2yOa-rdV2uDpBqM0U9-hVubG8TI4SW3unQcI63jpx0fi9aFmvPPx_TSMBUIDPM3rl4Po-H1XFKxah-eu29ac64nKj4VRDd7rNcx_kcieno4XiA8svexSthmJbkkn_32-85Mkodk4gRXNIqT5ncYnQQ05aXUBbo3FSTm1xjnH8UsPH3N945g4AVEamGonVd_rPj4hLDV37MBJbMMdY_RWeF6hyCaj7WCRU9Pj0O7QLVoq6q4s65QC2JcG0BeTvWtwLBc4fbLwBlD39Khp8AikPKcIEXE4D9Ca9Tj_oe9eFqPULSFqcYm4FNw8YP-rrRRcZ3BmlaZWY1iUcFZ10VVupXwSeN1zQArv8I-EQX9U4M6LExcFlMllK9hRKfhXicgTOkNUZpLMR24O6I0p6wjzgrRX43gQx4YDf2Yqta9eZewgDzJTSYF6VnELpqClxcnn8RzWlUbEoydFX4HR7sDYshOcnvueQua_GA-IgLJYCrzQqkGN6rb-0Mvf2RlPfgH7Gjz931cq--7uu72V3b3iXTc-9i-w4KfLl2geNmNlUxfRWM7xCO3o7Q.zXtbl2z0oHsUDk4qUvC2Nw; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODg5NTkyMTEsImV4cCI6MTY4ODk3MDAxNCwiaWF0IjoxNjg4OTY2NDE0LCJqdGkiOiJkYjE4ZmVlOC1lOTJhLTRiYjgtOWEzMy03MzcwYzg3MDlkN2EiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.m_fzedKdH3z1qGUnxOPkt9UufoY90sEpO76TmP4aj6EFUjk3v84dRPKegBiuOCciG1DY4qTlw1wBdpcIczVkP-ZgSZVSfu68oagumV3udhH7qz0QnmGLpVAHDo5Bo0zCKofYAOjmpGBaTnWuKxwYnUBK-GDTrk9S2b6a4ludHD7cg-jZuq8j1W9wKxdvfVqz2evRodoaMR3e7DnKSX94CY2cFo9tB8MlhtassWrmKQHC92mxEcawhE-ylDvEG0HuUxW5TBynbWkzDmZwfDauoE00LxDIvcifJD7OuVdndmKJ_aOp0jP_6hpDDaEd51_f3xg4DMzmBdhfA4ibWQsVCQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiTnBSMDNHaFY1WGtKZ2hGLWsxWlhydyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODg5NTkyMTEsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjg4OTcwMDE0LCJpYXQiOjE2ODg5NjY0MTQsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.sDLPIv9btywqFdbAeykB1HEMssxkyHuywhniCVpUykLImjIfPJTXmSCt29teO09UBD7_LxE8eZJZGJoGqNjChWQ8TL8qHfJMkht0OlPRqHVD7qyq4oxIbwnejTRQvsL94O69fr9XhqGFW6G8UySjh6DNin6m5SQSZqmx6plGk7fCFrRyFKYwm_e3eCs3E1zZ3u5Lo68qHvNwkhHRvMXQwPDRyM2vTDDZ7qegmE1W-IFJ816MnUL-jSCNaI7-dh2tKiyksDepcvF3HbZ7CsuESmnOgIfPz06tH64Z7UyuUOfDqZTsx4_R8UcxXX8cWMt26Ct_-33yYPSvM7dA9S58_w',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': '5cflEFhV-AfZZuVrr41Dg0JIyScUlfAx6_Y0',
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
    params  = {
        'service': 'CARD',
        'entity': 'CARD_CREATION_REQUEST',
        'options': json_dump,
        'monorailId': '40067',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        if dbInfo:
            return dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)

csv_input_path = "/Users/shariquerahi/Desktop/Git/Sharique-Git_Repo/RequestID_card_id.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Sharique-Git_Repo/RequestID_card_id_Output.csv"

data = pd.read_csv(csv_input_path, usecols=['card_id'])
card_results = []

def append_to_results(card_id, db_info):
    row = []
    row.append(db_info.get('cardId'))
    row.append(db_info.get('createdAt'))
    row.append(db_info.get('id'))
    row.append(db_info.get('requestId'))
    row.append(db_info.get('retries'))
    row.append(db_info.get('state'))
    row.append(db_info.get('updatedAt'))
    card_results.append(row)

count = 0
try:
    for card_id in data['card_id']:
        try:
            print("Attempting to get card creation request details for card ID:", card_id)
            db_info = getCardCreationRequest(card_id)
            append_to_results(card_id, db_info)
        except Exception as e:
            print("Exception when processing card ID:", card_id, e)
            append_to_results(card_id, {})
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['cardId', 'createdAt', 'id', 'requestId', 'retries', 'state', 'updatedAt'])
df.to_csv(csv_output_path, index=False)
