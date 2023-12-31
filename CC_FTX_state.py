import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=5N5WmuOmRpoZfGc5EHp-A-C1; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.TYALdsWwhm0bJ55qRO8dKio8S1_ObuBGkp2NAQa_WZDc_hCEu2uqQ8wS_VgmpgCl2-datBmzJIepWBSQmf4OrIZlSYwBBB6KtjGumiuG37h2G2-Ia2eZ66p1-RymctG28ya9R9_mIGarhmJ7Aj1Yzw-_mZEhZ1SosapJ11Bv0c8kYjXrQt9HzE9FxrwSvnbRtZNbQOAktHKdaXfbr0pTxB1hGxvgXzwihBz-v9BfKQ5xJ1-MFmeLrd4pmpGBrNG-d2uj7Iq5bS-KeFH3ZLflrfq-rE0S6VM708kMvQ-Qdqfnk-enZeAcV5mXbf_3dEno3xi0WmgOPmhvP01Hg4NvmA.6QQRLKqu5dbugkUJ.FbZAKd6ZovjksKjb9vSlsZzY_3T-gkQS1uUTWVHPLttSTXhxQpYYwwZSduuK6YpVdEfKa-4G6mtZVxJchBlJdmrBexHqDVwFXiJX8ZKxX6gFR__QQnEEjUvyyqn6cATQtewacC-f6azbnRLEeWyi4qdbt8Kmld9l4jJYfIGUAbEFhMG9fSodPR82GnwZ7_gXIFwB2UdvWqLAnGaDNO7lHR9pe4MR6qMu_qN4fsqPIKclq-k7dXvBebaYLZGiDbsz91FC_yNNQwd30ljPElLYCK9o7HGFglHV6i5E0FOiURJpnR2g9jl7Xd33wZLcP7qEItjP8BDWfiWyeQUMgpkHdZyxMdsgnjztKJOrEkZKn5zWPN_skzBk5cQsv35JSMgBVT8rGWlWsp5tRkBJ0q2QlE-0wSkqp1eafEQ1wkVGC4STVMVtoarjgEzXqd2S6q5HArSP8vOqgqmFi1LplghNeruov6k1g68aRwLGGRglStbIscWZv1Tlijr7YsXimUJ4RUnBj5tE8C57hs-1WSMhHdkiJZGfK1dPJ9j862sKj7NKeihx4GyatJ99Osr0Vol_9IR-sp57kgFREp0xMIplYfBaIg1qau2cJv14vHzXUJkr_mZMfBolIGybSThlUAkNJJLI464U_3XkkwtBg9sbK6uJcy0PTw18_niTBMXrFPI3RWMQhdiiGIlIKdLnbrcUwexRj4_U_P0N_nLe8yGW_6Mrm-OPGVU6anyazUtRJGw5YlSofg0Vc7EnBnjnsIvYqwYhMSlDQZX4xOOloxHnDbP6lOAZu0XdYftz_FLPfZcqs_6wbtdO2rE4isP4sCz-JUno4WocjZiXKiLV4SCkUc3xI6sPXRTQuWsw7TYm5vnfu1QskbyRSPKUGuL1ov7_REI1X5DozCj2Tpj4tJqFH9A8CVTxGM3M4QCxKb4K_X30Ma1XqhmXDC4VlWy5-ElLSJED-t2UbzLDgGahngmhBWI_TVlY5w4McLwzgzpDXNMLnRLfOptHaSdWzI4TJC50OT0orI3u8jx1615o0OZA3emR_FOKPZhojK0cm-WltaCkD6w8Imzmv6b8DufQF5D55E3kQsKRy_9Rfded94d9kiE0F4V9TzETi5nebmhNUPcjAxtSaGpyKzr67S8cEq-8Tij15WwOckqUTn-RC5WUeT0mug491UrGyC0_4uIGtTV2sHLGDajJFZrREZBjMNFMHpQ1iuZcM_YfrvzmDZGFruvC7f-bhrYA_tRICvk23CI7uAtK-2d-TNmSjxQg2Dh5-bJkzEUBRGrGl9oDnA.saFW3CgBe6AUW_7hX-DIzw; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTA4NzM5MDcsImV4cCI6MTY5MDg4NDc2MSwiaWF0IjoxNjkwODgxMTYyLCJqdGkiOiI5YjE4ODM2My0yYmI0LTQ1ZDQtYjZkNy1lNTUwMDhhN2RiMjciLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.j6_QkCWZlAd0Ay0bmIpf_Csq37blMMomW_zx7Cvu5kfsx2u2pk8kZGAOfqv_dZvIt9BK8Q5MfGg5hrCaExCiXrJKqV-BmlM6EdgnpzqKF2jaM--a_DHHMn9xvtERK0NxJAx-OXFAZLR0S88c7vZkZ4yEa8st61M2OXEaDVEXQ5lRAZ_a2qdgy2DwZ9qh6KjpBgh6kN1mNyBzAPLk3092BTlc5DjLTH5UTOIV57TH5NRptqzWBztw_jVYXtGpNx4gpWRNCZt9okpo2j0lgklejb1Ag9YPTxBIHpvhnyQF596a_XTMaG-hQewKl9aSSeAKCMoGa6D6TMDovTtCB2IJaw; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiVGVNZGVLWW5kZEpNVS05VWk3Zk1aQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTA4NzM5MDcsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkwODg0NzYxLCJpYXQiOjE2OTA4ODExNjIsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.dUUAeNhOVlVAPEwsf4kHECQyioDWE0-QRYo9Xqfm6gkryE02a7OQD-2MLSTeAl72OYruijGtbsfzfWIup9CewVuItDAIsSkGJDe3DSMB2tRHUBkOtG_YExYFf53m7bxMsrtuQutCOpdG_Iig-hnhNx2JYWRSO0YF2RXD1fgQ_qVzHpkd7AAKT-Njtdzc_eWFinVFjH-CqXSwZgBSPi3azsHoMYG4a8yh7znX35ZHACzx3fPE4g8ftwsn7DwC_-Bxi42OrodE6RDVQ95V8FyGmjaHAfcsFjEsWfIuGOFsBX_daCTgpYRMIO1qP8VGbkn_wvkoaOZwyKVGtzKVM-6PbQ',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'BIXV0OYJ-fPLyCDzQh5y7cwhGarBLEOuKg2w',
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
        raise Exception(f'API call failed for card_id: {card_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for card_id: {card_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Downloads/Card_id_physical.csv"
csv_output_path = "/Users/shariquerahi/Downloads/ouput_card_disp.csv"

# Read the CSV data with 'actor_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(ticket, card_id, dbinfo):
    if dbinfo:
        fund_transfer_client_req_id = dbinfo.get('fund_transfer_client_req_id', 'N/A')
        state = dbinfo.get('state', 'N/A')
    else:
        fund_transfer_client_req_id, state= 'N/A', 'N/A'

    row = [ticket,card_id,fund_transfer_client_req_id, state]
    card_results.append(row)
    print(f"Appended row: {row}")

# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        card_id = row['card_id']
        ticket_value = row['ticket']
        try:
            print("Attempting to get card creation request details for card_id:", card_id)
            dbinfo = getCardCreationRequest(card_id)
            print(f"API Response for {card_id}: {dbinfo}")
            append_to_results(ticket_value, card_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", card_id, e)
            append_to_results(ticket_value, card_id, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['ticket', 'card_id','fund_transfer_client_req_id','state'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)

