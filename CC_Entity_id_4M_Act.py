import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=r6oa06-B0jCXBWhiA5Z-JPjd; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.n-6VmCgylhQk4mTxHUPUpqAXe-DotM_3sMtZnY87AZu5kGy0rToCp4Bmrhp5hzw85-2K9kfT87JAAFpy8xBeehhK360WSZU4Mg3jfS4NONO5WZ4Q_L_Bwka_W7xzr2rFEqfE74oS-zfWJdr8fCWBQEO4wAQwrZsGb3CmCG6O4UqkZGMqFtWEic8qW11-n3RZGH5ZXprNK-HTmjA3UZcpESlwa7DhfY8W0FTGL6XPMvj2bXJ4BiClk-gIWRoztkTbr23Sfl40b9Sywar8WRiNe_C5SWz2UXaeaFMQ38bEyUjLE156UOPPH6fx_pcIi1tMIOHLo5ML4wH9M5egiKvuEg.KYodjzhRrQGP01ry.tg2dPH6JQ_-tEx7QUyYQRRRLIo4I1_x3Z4G-uFi0kyozfvBXIob9V_NpVxEk6bhbcGdn4Dk_6U5rg-TacE6aqkyrLd5nXz74H0N1Rm0ldKqZyNUfzqCXGwm_SaTzY3Ef3I5JRo8qvOhw5XLyEJqtHoRhEz4dPE-xm093yPWtCv8E-kLoJp530FkUnqwvyHYA-Lh40VkJKYvgqIxir0ycbIAX-oKELKKERZ63zGg_i7Koivv1fHcB9eO6ey86YDVaSeITawuoxY027jn8uupI12XmlMAVoMxrghfYSqsz_53lkKAUW8k_W4YZUZVM0phbMCeiXwnid1tqnEswQZk1DK0AL-WDMUIa_qvl30DVhT7VIe3a3C8vTOIYKgJ_g8h5Cs5sk4HI4AX9JN5YoeqevH2VosA6HHPvJUqsYS4av6kKrR08uDWgRsomXesN7t7hGzh5RsQe8BQxCq0m9qQUMTw15YHQR7XjpuQ8tpmmiYa6vovUqOWJmk8wTL3WoCePsp3RQEAJDz4niweoBpDmtI9w-SsUPXJG0XfyND6QzFq2BBiOxnMGUBW8QZjI1uRtW0OyQ445tlue5FWUsZIod4i3h5QBTMQ761aNyKOP3iZG7Lyadoova7jmL2On-GEDtULbnO-NnROW8lthdB-PiGHDDnwiYqQgDyS0fWysrWDSJLTh_HG8pfZWUKfy7Sj5DTdaLbArv7ID0Ww1bvw2kZB_Qs3BO4wZn_e7kCbKkIkmITNG4mh-T9CxT1iZRz4EGwxznB8wNP7bU_YiBIPY-zT-2sxV8gaOjGYR3uPRPIjMjyp1LB-px-YFM4TfBJVTaEuuilT4yUPxyz6A_OyMXFH1Ea05MN6vAQkyyPUxsNlRngc_p77bOQIuqszaT72IVd3GfuQv4XmTHbh2GnpmNNGw-sXlYQ9LhByPNVbrbKuPxxfDEMYChICyIp9Lujis5Al1lTw23Phlk7ElKMWiACriXNn7gzjVQ0fVsNHoEqRjzi6ucFYkIPDOnVDtVmR2r0mCbd1y3HGzpIciHVZa1as7vhdV1ACi3YKWGqaUBNhM79Rc5bCXGPIUp0-26BuToWnDXQpK07WtxS64gJNmhrSSTpe7WtupWpxC3hIzrisH6bqhGWH2JHKfuBik2uJLPhMqoEFeZpzsv_kFLU5BqLw4Ytsf0l41417L3UiWyUzzjvk7z491RoMweuuCxkXt7FTplYhewuAqFMEZEhg9UBpXmzoMziE0ZGWpbVsMaYvTZDxkH4IC_lGowXUS4EZfMIdD9vwFCA291ABIIQ.32MjIzJuUkSn68fyBn38Hw; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTAyOTM0NTcsImV4cCI6MTY5MDM4MzIxOSwiaWF0IjoxNjkwMzc5NjE5LCJqdGkiOiIwMThhYTg0YS0yYjY1LTQ1NDktYjVjOS04MDJmYjliNTU3ZmQiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.dbGq3MGaqdLtPDOYRvQgOSIvYCce-8YS8dRDorF3uqas_4mn14IAGlcddMGD4V9JSyih6TVhfCxtfQdjtpMdAxVxk3-qOKdHGkvcrMcky4LbQIoAhAI8r0vPhHNkMEa_JB8UnpFFFd1fdOz9gpg_ptLncyGaf_rBEN0kD65Y9Sh5-mHFffPeydm1oqRYXWmXlGLJQ50taqSb6c_42edEnaZevCXU7N8ng_8I1oTHYHmpAm_-UjLNaE-qXcPsSv1fXF0hBnxf1NxGcnVMNiMNsrsN4JxYJN7M-BXzWntBdQgck1jV-Tn_kPf-jyR0P_7-p2TiQIHK0Edg3YSrRoeOSw; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiNFU1Z0l5Qy1pUDgtRFZwa3U4Ti05dyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTAyOTM0NTcsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkwMzgzMjE5LCJpYXQiOjE2OTAzNzk2MTksImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.JPD23-vlB7v5AvACAHcNjw6gmrfta4gH9Uc-EP2J3f4WwnAAMtIsFtXy8pD-TZlrpg6cNr7tSiPhr2mCrAUTUQdLT7BlO1p5ZY--iyqCKfSL64v4j1q2MAZ05oJGAV8t13JQRQwjWzw4VNHZ11yGE4wvQc7OpPB3XZ-CMpDnWGG4p24pN2gayyCmlBayCseFRlQOC-su1N_vNWbyZ2ySSjYM27xgph-Fm_ZVj86dIJ495CzWhMs9Xgtp-8w2Pil5hagMy2PTwEBeSL8eW2DfdXXHdqtt_ppHIsQUrxGSjZzCWkRV1gMO5v-48kVZXZAVnWc6kgBFrSy74E6uVzG0zA',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'gMf6sS9A-ijK6YgRvru6VOPzUL7zNnE95qgw',
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
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/vend_identifier.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/entity_id_output.csv"

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