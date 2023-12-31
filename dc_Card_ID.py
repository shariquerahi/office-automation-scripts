import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=1CFrv1Y1GtyOX4vk94HcWpt3; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODk0MTI4ODksImV4cCI6MTY4OTQxNjQ4OSwiaWF0IjoxNjg5NDEyODg5LCJqdGkiOiI0NGFiMjU4Zi0xZmFiLTQ0MTMtODIxNy1mODI1Y2E2N2U4YTgiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.hA3Qma_jBihSHk6zBiUhpHTfJEdgG9_Vz0ETzA4lmFrcAf58rl7WGFfpJHYRSTxoLIc-xkm662jf6zvJbWzghwzdyNy6_jq2Eh6vBrJncqqKy5uD5aWN2DnOehTbhzlO0Aq6et4MJ64no3nTp7wLHfLpjZ-TrQOG1Dw4nL_H7QSlT5qqBNLIKDoPpHebDhfXwcLpkadd_yYr1_hq5GBRZnbAK823lYBGbr-nOnNL0xhMkyeO1aHyewPtShWoLfSgnPYI3n3S41bHhUPXaijitySz_9oXuTXJYZxK3lfB9LOjLNhbTt-FhEgH3x5vaNnEDw6gqOpdAPHZgHCmJKsV3A; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoib0pmZFU5NkRqdmZqWEpxSDRvTERIQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiQlA2WE51ZVBuLTkxYW45aTJjUmlnMVRQc3A2S2d4X2owSUdtZUNCb1NHcTVEMEZ0enpBazRzLXJtbUQzRTYyMEc4YkJpSGU4WlZOeXgzdXZ1T0FpT3h0NXhnc0JmZmRlT1pLZ2V3c0ZsWWNMUHVBRzByMV92ZXQtOG1zdjhheDRyUjl6dHJMWDlLb2hVV2tCdC1lVHJYZHNKZkZuR3A5QWNySGkyNVBNSmx3IiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4OTQxMjg4OSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2ODk0MTY0ODksImlhdCI6MTY4OTQxMjg4OSwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.pyoH4gVwYRYDRPY1BbAJLftLLf5Msmu3QGU5aDLt8_cnV1z3nOQX8PINKUZpirAn1r-Y-SGPlL4jzmeXOs8E8o28OgayjPZaBJtBBX7AVvzy-nKJYx09u3VA5TvllxVipAB5slTpCE3unh95zLYRVXuVAOm-0L8Nwp7HjMU9fHNIIMF2ox7km5Vo0Gu5cifyLKIT0Gtmnis941taaSkCSyLJVvXD7vMU1FLm2QVE24heLmEaILpqjmQ9MmUc3aTGoJDa7J96H35FkXvyPeHiL_HHnn7JeIOQ1bdH9vS5EDeZ_I8iWu-YegZ5tUJDYjivJSjBGdOtYnEv25zbhi48Dw; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.sDGbldN4jTaJ4e6J0oK_LTxbB_P9yQhy_BzktDsz2aQqT1cxsHxHWh93V8JInamycaN6IOAYXoy2spelwradDpjv-3bT8a9oZOG1XlE70zsUMa3Q-31L2xfszBA1vPF-wnkltSgD0oTGUZndmUXCdyFMze1VIQQh0GADGooXmHXJhEiY7oqK06vwsrPRJxBHbktpm5tipRIG-UeZRhqv2hTQe5xYZubC1hyruJt59rc7ncCXvq5emtwP_ebSUED9gKhAQwrs-ai4s7d5Jl0ocY3cjEujlFBAN9p9GpMSiitGpgfMfrV8JP8ESWNJnEnCOWguTEuejPFzoeSN_3RaNA.hQfwlXuEMO1QRxZv.j5ZS4K34N95mirjB245myixtWpozPwlGRhyJE6PgHZOD2cQYmw-l4KdDE6uRnAo126cgN4Zk3sx7cDM0u3HKZFgJ0_0ybxD7anBYbomTMnNym98yPZZVVORxby0EwY0Ob7w-e9JMTynKgabohtr9-TPaC1f-jR1TvjBbC0HyaQlwy1SyY9g40h6pruD5il_2-22Ww26b43oufA6dLX0gSNjfh6274yWkpc-nXPyCmldBjSpndA_fA6MFlUns3ahBj8L_6dKMZuqyHIuMCicbL7Z_Ovst-5fAQQaPsO8fSezZO_cNPVel7dCE9I8fAwQWyWiqXtWqi1IIQxIF8lMsU-GeHeWXav_LLc-uYlnS8SbERSwnZOtDuEiwwo--vrS1_rsCEkWGKrWnzy1z4-p4bU_kvqlriOhKFxFkmlFieUVeSOtbbv_z9iybBD8Za7Zlhoh_dh9_mTeqXC0Os_GNbEGP3P6BhOCIJDHZ6y-YN925EU9zVPejZWnDg_0Ed2b3Ss1hJvP7QmTNH81aQKzMBXNvKFfmsnNGPklXshdABpcvtPUT-JkFoEDzb2tXSRlpAncwDvfC4PoC1WbJz21x1UETpepiHpnCjVt7pgxvOgcUvHRKm7N-ACzHQfAgpMsfQO6UPM2UOn-GAb2YU3vLXsNXBaTngyy3XomwlLtxN-eYIx1zXB4AY6A8icxPU4SY5lxeRXqwtOHOKFg7Q4yZXu73OeTTOgTMACQCJsGildPbo8Fa1l3m0gxwcfwr9Ymxji-1h_dfUehMMj1vPL_JlNc2xm8kSNmIhNuOyJGGKC9YeeiCTuqHK2TyGphSeaF8jQAr2_spWhDGWi11EKZsUV15wxg3f2JUpsXIIdg-j5ObzdKQ-wxI9gdSfx2T4rKxHq-M9CKGLBcljVaSJqj_CqomPo9nihGJ31Xz3VuHp3dHwH5gukUp03ubpyIqm3SFXUHLUjnPMuu5qxsZPsZrVZX_VTq3aJ6f52lZlbSJktU5NgNU31iP_QKOjnhz5P6lDwswN9_663mxIfqlb3ckk-m-dTkgOOBjgHqKAZL48NDG3GjSx_aUleDV6-vh-IM78SAw1_gWXe9Ul8XEc3axTeHXa2ceOQRUanx7niPdVj_xLCkhgitSK3BCNGN0nlo7zlEcz842AgJNnmKiLufGauRKpL_Vooihq96XVG3PECOIVUQZ4mSsm78nYDDgBnLwx-SMLWDaqmv_zzVGRqZ2uX-PT_lvhPZ26nZUqklKppbLs5ZSYi8iitaZAMR4ufPIoj1iUCsH_D8VreBjVg.6Y-9Vd_9-sO17dgMVrFCrg; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'xkXA9l7O-pD9kQPmcm3OrVRIJmVMYnU1tKbw',
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
        'service': 'CARD',
        'entity': 'CARDS_FOR_ACTOR',
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


csv_input_path = "/Users/shariquerahi/Desktop/Git/Input_File/Actor_id.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Output_file/Output_card_id.csv"

data = pd.read_csv(csv_input_path, usecols=['actor_id'])
card_results = []

def append_to_results(actor_id, dbinfo):
    row = []
    row.append(dbinfo.get('card_id'))
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
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['cardId', 'actor_id'])
df.to_csv(csv_output_path, index=False)
