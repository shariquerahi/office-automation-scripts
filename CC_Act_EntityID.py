import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=JoyDhRGIWlX_sqFGAZym7OIP; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.RFBAmjxxqqeVJD-nNbtt3AqKuAZYgYjsgt0pSeqeMjFObQxphvwLyWx3EDB0lEt05ht6BYHEna1tWwDa4dXhchjiXI2Jp4-wT-YG3qui1qdPcFRlcyOxuSEcp8ro8JN5lpNhOC5zXB8MFNFsuQFGjypW4qwwJ9JUuXglZ9ftSjY_XVuxJpMX-qrD5xNEHtkB-YNGS7ZmLIojbbhq5fltxqKwsHsDqGBdsRhIDWe8E9Dhbyb4WdWpg19-YW5HO6_OItH8Zt5aX2YC3ZkiVQnTpd_ZXaOaNlkYonVDZJL2FzLfKFWXxNSO9Fgzr0CdF-CAIUQbU26LNPHhSuEGhgcTAw.MrGSdoxKXG6ICMPf.7y4Avy8PexpHQKb36g5PgGDDnIVf7nrB1QMV14XsV7WYmm4b07z4Mpu6ZJy9D5MRCYdviCTROyCjK-eEkVuqJG5JirtmM_NVzp0vRiDdU6h3iOcSwItVSXFxxeexvRMWlTm7TJRaiczaeHjGQHyDihJ_aGmPtnSKPQf7L5ToejPMikIqTxdgxjM5xIhf66RECSlsfIvNkKxQHZICY8LpRhCPFzdRdbGdAzX32ipnxqJHScjOJxiMfKvsnp1vxp6HWku8w3Z97oP8UKLNQ4ir7tkSOTz1NmWKjIETynuRPvaPaUMg1qKtrAoky1S941xLB59yYBI6dobr0egrHtLzFyKutvDgb4ylfakPHZ8HB8Nx7FOJQ_Yvrzk_s144mvy4iXhcUkjjWlkkcDzzxTuD86S4L48mrsBPvURA2jPXA5LhOf-T5J1SDzMcF2dZ0qKvZslz4erbqtkUZKBP_ARpRtm8zk3nDGtlGpTOGDtSdU0wOFha4NQ44eBhpNGHYls4Hth-Jhbfj5UCBsRM-otfBKahqzRFSLOqjiyOU5XuIP6yI79uFztzo20jYjJ-Y9b-OC-P0fJOTWSyGy0xiRSkDum-0j39HzdB9w2M5WaxwkL3V-ItOpihcjGN5FXfdOEC0GJ8k9cWH5dhKcBK1ufSJ_cCxHcr7Mve-SJkScaTlajhRqsRjuelN9GDU-YNpZvZkT_qsb8mDmdRM-CqsY5wSTakapgHaKWYc-_L3uHBHBxvvDO-8jFAjT4rfHYP3N26V14cK_kBmyfguCIH914qlxdVDKet86y1OkGuP1-6RmEa0BzGA-Mddp4KbIU0a6DoOhsRiLzt_vyn4p-6k0dJPOr5LXtkxZeAD8amaTX_O2D_9SWocQx_-8aBlHg0XVfDEYLYIboyL1CgTsiFSOKOiTc_y1pROFma20-Qri6UeB1eHSIjg_smZZLU2ZKWv3zL4Cpx8QtbAdKkw-8WLEP2IvYOwl-M2w7GAw6YnZJqKFOEmknBxfv9UsUsG_SGy0H0jHPGTDdvI7e9dsv_G4T0a8oqUJxRhsTIlAI2MPUSSr0zb1uChtfIzEAoHg19fJLHigZf6ogLQ5G97hbhX1rUAnl7zXuXFTUkr5MNgDBe5-R9RqpqptlTnMc6VwGvbbqU0g0Dx2PvrWOLHxqA9zhG8NwlQ16t-SRoW8u8emvKx81MfOrsB_PvV8UWiV9ETsuOtZYgYJwAmr59WrTmStyEWwIDLW9bPJbjtr1Uz-ogHICtkIblYjaYiUdnAEz9xlvV5jc_6SJHK5tF9X2ihA.Zdr42zod6pytuDQ6A3GlbA; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODk3Nzg2ODAsImV4cCI6MTY4OTg1ODkxNywiaWF0IjoxNjg5ODU1MzE3LCJqdGkiOiI0Y2EwOWU3NC1jZDg0LTQ2NGQtOGI5Mi1hOWQ1ZDQzYTE3ZTkiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.Q2XQyU_cJWAv-3P_jcnXM0Ybju3GDRfAT2-Ji_HjAXhEem9CObDi3whC4E0r3e4jaH2AE4XxJNm4Vur21NtcigU2LCg1Gx7yu_TicooOL9NEpT8MaDrVwNE5w2Yhd0LB7LxxV8MDQnDW5hQg9_fK-CVJ4Bk3AAx_VU4mCEJGxORJkSGOshU2mwariF31QoEiZLuHv88pyk3vjuvlkhoU4N8zcO8lGMFZMTzJsH4mKV-cIqJLpZnHQcvhtpYCZlmeTT3pLLJBSKfcTRcPd9foLEhNd4RGgCEopy05jsHy1rdxJbzVXj-nayX00xD463Q_Ga5pReueXW189VSuF3mrTQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiUzUweUdQeW8xRTVSUHkzNWxnYUp1QSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODk3Nzg2ODAsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjg5ODU4OTE3LCJpYXQiOjE2ODk4NTUzMTcsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.kdNrBDQXOy20U461BghDE8y4Ynusk5Hmt1XMcvULjVKr7EB9FAFG_7_jjY-Bn1muDd5oPe-EijNDcVv0iBHu4aAZwGnRsqcv6O_D9BEcB6beiQM75fzIbf7TC177r-F4z8kN7lioOvhNvUXa9ePePOUVHf_VUReaOyOK8LiJHvmdgEUsrTklSsDIl1ichabAWToBjzcShvjp0J4mLlCaBcEYz8uNvT1XahVBBQ4niK31bhmCsw9j7sEFm8BoRhmwdwCb6JBJMvgmPGrLrYIqPorKNOn7ooOFhlR9TAKQ4BNXQuEgpJ0SVQ6SOmiT11lOz3puJGlgLWjOOEuAaZIZYA',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'NvOuX7UJ-r_Fj7IUvfSGI7i2L6W9kZsRqP4I',
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
        'entity': 'CREDIT_ACCOUNT',
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

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Downloads/output_vendor_identifier.csv"
csv_output_path = "/Users/shariquerahi/Downloads/Reference_id_output.csv"

# Read the CSV data with 'actor_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(vendor_identifier, actor_id, dbinfo):
    if dbinfo:
        reference_id = dbinfo.get('reference_id')
    else:
        reference_id= 'N/A'

    row = [vendor_identifier, actor_id,reference_id]
    card_results.append(row)
    print(f"Appended row: {row}")


# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        actor_id = row['actor_id']
        ticket_value = row['vendor_identifier']
        try:
            print("Attempting to get card creation request details for actor_id:", actor_id)
            dbinfo = getCardCreationRequest(actor_id)
            print(f"API Response for {actor_id}: {dbinfo}")
            append_to_results(ticket_value, actor_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", actor_id, e)
            append_to_results(ticket_value, actor_id, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['vendor_identifier', 'actor_id', 'reference_id'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)