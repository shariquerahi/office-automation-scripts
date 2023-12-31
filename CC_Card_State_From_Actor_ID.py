import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_csrf=5N5WmuOmRpoZfGc5EHp-A-C1; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTExMzE2MTksImV4cCI6MTY5MTEzNTIxOSwiaWF0IjoxNjkxMTMxNjE5LCJqdGkiOiJlOWM4ZGIyMy02NzlkLTQwNmEtYWJkMS1lNTczZDRmNWVlMmIiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.GXQHoA3IMGiGcpDNWLg5AKolTkclUeG03YV3L6P_1ax_Vnd35evYeaOMAHzpdX5zyZpw-0kQtBqQiJulRH84ZvcnKwkv4WfiNOHuvwGKeKR7AciIBdoRpLh4xeRZpP_UjAHez2VCpiuq0kPlHtBvoRopGomzy3XB0VM32SIGwwOS9lMxAnCtd4hLEyGDxccVsuGaga_XGlAt3OAe_MF4wM_nuypRXvoe8lQu3cVKklq5fInM1zfSeA_A6Imfb4ApxuVwpXrLCd2ADqHWVy1-40liqMwfu1n4XrZ0eipQvoGnOCbamfse-yaarzmIpcg6MWrKogOpy6L1d37u9qIBKQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiZlMyZDhtRFcyTnFDQnJzZV9FSWt1QSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoibi1rZnVrWDZfN0lBRFIxeUs3X3h0NUZUOEpacm1kV1JCaEdveVc0TnNZeTlsTXB3MFNyeWxsd3E0VXFiU0pKNzk0bVBBbk9oZ1UwTFZzOWh1aHkyTEVQY0t1VnFxbUkzYW9keEtqcERqdWtRcGFZSTJEN0NpbXo1TnozMWIzZV9NNDktMUVjSHM2cGlPNFQzNUEyLXoxcDVBUmY2OHRBWVRJTUM4SURZQjJJIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5MTEzMTYxOSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTExMzUyMTksImlhdCI6MTY5MTEzMTYxOSwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.HbIPSx-FDEyOKJ5233874_j0j1WIXV2ITvymgme5eD42moo0Kd3-llg0AS5mEzlrOxGi6xpez0mbtfOT69084UUKvqA5EbsIH0TYkE_Vme2vjhxqZDXS1XX8WeeNMmOKeCMK4H00X10h1nX9Vq9zbDOGRcd8OD7iqOftIYA8lfzqhoe4SMBEi6BdpUjtfHZZVaww2g4ELf6cQ6fUOYgMUboMWMIa9fbU-SaKjGRXvXjzfOmLB3aSU3YbeCF0BcStDFATPsZ323rOQHJB7uhNWlk0aDGzhTIVcHQ4L6CWifH3-lljkwVvVvR0juZvQ38wNhgvKmZxnAUZyvwSMmIGMw; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.fiXJUNuP_rA9n1Cq-7wkgpuuP_LVIakllk8DTu5FzSkqrSRrhYyKy9JeDRdnR6hyVfQGhZi4IxM2toC5liGz_SezGgrtnXfDgxu09AyOHv4EZy_o0-2rmk-I5ItHbc55d7lrcRdKBA2-yfbVVSu-kx6-McYdhrQt2QDSIL1OJxl4PQG5GGsNwWy7HwTE6eHZ2CmbAndjAeIxMj9kUsA3gPiMVO54Adjo3wICEAoafs_JCVv59XmoJJcGrkFj4FxiyodEss-fgz1nWZtKLCDzDWTnYIVyRYbAT_MgJpLtFHzfidANywGGrB9J2s1OOW4iZgGKQqk3bq2BtgA3lWJEtw.UM57GdvPwmiSyjQS.GtrHuXUiHxwrtYB1fZW028ib4VmgmjXED7hVzjss71MqAVxs_g03jOU6bpOkJaqadAK7seSuQhxLTvibxjkS_d0OA7_2JpMx1FzqF_xwqrxdtb0SLoY54hocFMlzJhqtZjXg46_DnZQLsX4nuYFjfWIIJRZE2DCuxBMm-oJSzoTExuWFqV1x8KUzaZVrTfNAcsB3-3nPj8XWwaMCJGYmRWNscNmFwXOX86wj8TYHtlR8S94UT3J7r31GFcGaYf-Fo8QgHHLdjEfXEVG5aGFLli0ROlpZY3vekIuMacqwWqODFOfmkdF5yEqM1rPjR8c5rhB0ki14jbqaBA3aZvD0g18ogYkuW4txR458hAYxMUyjfUT6mLUAO1wZzq__OWC3weX6mB5krX4tj5elXU3VFbdOmEIBjmVoZPHoJw0Ef-ix1L4fPad5ygoLOhTw4M4g55EdeOFCJ6VEydnpP3t3SbCbu5cW9NnooBo6yij1DjvQJ8oXzbymY-GmsB5rB_ulP0TqyF44yNuEvppaVqhmTr6oHWtflg7JoJLb2PozduTIlVyY5vei-QCCJgiqmf-NN6Fw2vQKKA3Tad5xRXuaPACBGbYzEiV6pAOZOSupihkhGVbQnOwtG9ru6S85Un1ammoKxi8Se9q3VeukfrcuFQneupxZrmRznafaAiL6TBOGKRrt8snLBMoEe7cKBHV_-Eo8M5Tqa0wXGVaL39XWEXP_1KdeKziNxrB92pK76EIRnbMrl2Z2a1-zU2ZD9wPujePb58r4G4AxBGJIw5uhnp6dNoE7iSLJoZk6zP4sEdYf3IVUU_EtmZYrWrcmK5cehlxekeVwv3FsTSdlmjUtINglCbW2GYEpdsmFmIiXAy5L-PyC4gO-ae6iL0DRkyj2QmlJIB-ehSTysH38KwrwYoJmj-IO6U6o6nwGiob5YnZEvnYPI5L-lvggG8DpqmPy5SAoW_ooU4efJqIR8OzvSm84kwyhnebn1-7nbOvlge00bm423etSPDvHoveB_YbSD6yPYuup7EihmgtMGhM4UrnyPrU8L9j-8LPHJpCrtaehOgWNRpbZ0Guv00VQ-QhuilAXkx-rBrK7b4ystmZqmOnKlZn2p_Yt4rV0-8P-2kwLffRFDATCvHkXdLj2n-EHAJWlR8MNVLyROjkpE9dLUzoaJqqTrZmScXBB490wMB3qFWVlM9TZWArJOb7d7fhmJuZqGmfKd1yR6bLd7MV9NZfw5zhck-zJ0WxJM7WsevdTfcyQrRnikAgLg0jOmiVgyyIvKHYBO2sfjU6DLA.FMngFJXAelYFJVIcJQhzaw',
    'csrf-token': '7AY0kRWe-0bwSkar_mbox_TcnteQBEN2Icr0',
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

# ... (Previous code remains the same)

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
        dbInfo = r.json()["dbInfo"][0]
        return dbInfo  # Add this line to return the dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)

# ... (Rest of the code remains the same)


csv_input_path = "/Users/shariquerahi/Downloads/Bill_Generation_Date_4Th.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CARD_STATE_out.csv"

data = pd.read_csv(csv_input_path, usecols=['actor_id'])
card_results = []

def append_to_results(actor_id, dbinfo):
    row = []
    row.append(dbinfo.get('card_state'))
    row.append(dbinfo.get('actor_id'))
    card_results.append(row)

count = 0
try:
    for actor_id in data['actor_id']:
        try:
            print("Attempting to get card creation request details for actor_id:", actor_id)
            dbinfo = getCardCreationRequest(actor_id)
            append_to_results(actor_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", actor_id, e)
            append_to_results(actor_id, {})
        time.sleep(1)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['card_state', 'actor_id'])
df.to_csv(csv_output_path, index=False)