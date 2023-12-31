import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=5N5WmuOmRpoZfGc5EHp-A-C1; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTEwNDQ3MDksImV4cCI6MTY5MTA0ODMwOSwiaWF0IjoxNjkxMDQ0NzA5LCJqdGkiOiJhMDE2ZjBkMS1iMjljLTQzNjQtODYwNi0xNmM5ZTNkMzFlNTYiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.OiM8dzcxGcyM0s9Wjzoi5mnNg1sfx5cOC9uF1Bx168r3tgWpy1oa5xu9h9ubRpXnfo8eJjVUShn3-9uOcmtwvMM94k8l7sNs4qXbu5bKP8b3qSgbazwdl02biJP4zKOO-Z7_ph1m0pI8nGO3tvZfiVPToCHMM-D_HKwLI7TfzjqexhhHdHx9T4GLu4J0zG9tr75SI7rGas5xUKq43EwsQnPVOMjQkSwW-fWoa_0FmN-5tARWmt15BbZaHbfOrvqT4gvotASltv_2vW7WtjqJsp2ISijCuFvQ_IfzD6lbuFri6q76reqX_QCueyGgAPfOQfiYdkl2KuQkJuq9RezAwA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiQnk3SHBBRFFPVjFfa2xXZEE5S0dPUSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiRDZ1TGxyejlMSTR2T2ZxQlpEUkdIUTQ1MXlTV2djZ1FvSG5Oc25UNFZxTjBydnl0UDNQRlpBX1ZpazI0Vi05TUFiQWkxNHNsc04wZmZ1YUxxMGZyM3NVcTNVQVpyZXpvNTdvbDliRUtnYUNjUnpndzlneXd4Q3VKRTZZRThHc3kwd250aXFPMFpNclZpTk1hUHdNRVhWQjZETDNZVnZtR2loYXdkRnd2czlNIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5MTA0NDcwOSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTEwNDgzMDksImlhdCI6MTY5MTA0NDcwOSwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.laEU7IVSx6dipge6OfVyxQfORUfiOxnlDs_CZ1z1SIZ72massRTHzLkQ0Co4kwoCebxIiL07jHHZIbaz4f6N1wQlvtpuubxV6ykxLlQHiMaLOonoCnhktVhiXJeoEW4-ZCUWo-C535YlVUL7R8ppHvyYYgYUZhoMcNNORaAdblfcqyfR7jYYhttKTfeqWmayFJOUOATLPxg9p23pExJidazL0eq_ZH5T_uyJwfNo3ccPrcT3jOWzbqzUj1JtLbvwOqE66qHmEsZ9_yk131IVehkSxTp3NaOg7hT5RSO7osyCNFB3wFMPQIQS6u4ko9qksTlS06iVo11qKkEwm-Y6TA; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.M8qddCEO5VocnKwzduXxvwjiOz6iWmyWegbusbuh6LcqpXbrn0G7E7zuhUDxl-VuCWOixzm5CyXokxD-ieSfZTKgh1awH6v1pCBjubDXn4Rqw6PxmcDUna0ub0iLpOr8JpRumVmfWwKa9FNKIZA3Lwqb8AxvEzHqAJDsScXSqctnbeyur3h2qJjCl0Ejg1Xo3f5ccT8uKauyblruE8uN5mqJg4xLtK0LhngZ9dq4mwc2fe8nISCog-eO9eJiPNwsDKfaoJ9mHDKOnRi0AFeXRuW0Evs7vgREq8hSzwhGtb3YYLJ0o06A_uNEwMmBsK5jnyMmWW0f1Rg8D8jV3EFgrw.dKhPKnUTgv6ZbYnD.CrcqOt20teo6oji7hbQqeOdbLOv4wBVIRkMO0tTVsxR_M7xgVaWyNFfkU2yNGRv_MCw-25mFkcp4OIYO0wr62DI_DXUoUTNcFqFRY1r0Yn-kuwYCYlcCyKpoHRLWhzAZ-sfLU3Sa5E0N0iA4nBHqGXSOCZCE_TM97jszlC8Z812XDroVs1nvfEItpwWl5xly9oe4jbUjPf9e94pHJLySrlB5VNxYxvG3xO9HTj77WttWxPeSRG3rB40DSnPlQdO6VEWZM2XYTsTtAOJ7JS6j2KX2pKjOy6c0tQIJknM8s5EcEGTGQ54_cIIjRxy8t3QuEssg0mHtLN0uxMW07D8M68Nl4AdKDI7-JvJGwtk1gMDXVKK8_PqtEDEy2g8fR07V3Zgp7y0qesK29AEszUr3sLx_xktgOD-NFlI9emGZch8LfuqSX2kC-1u9yYux43rTs5K8Tj77XlrsqyZOGvVZjKF9CGeb2FAz9UCkexxpouOiVYZIBZ0i-eazUsbcxFMVpiWnGsNjed3oR95VKDbWEkK6QLlGc_R6C9ENKqsLICJv1AUeOID3X9rawmCSHzf4faVeY_rOEt_0MAJlUwcaeX0ujgE1uq-dJZLpbpXiSZ12VTpIhrI4St5FDN0eOsk4MTKbVmHu6vwezdFndxUnxMKKb78GXxiHICEaGqQ6m_aSNggfhmgwBBhhHc631RFT20RUU0g8ooLtMwaPQ1mh3YIYPj-WqpzGT9aY2lHqtPXhK7DkfhJh20C0tJeuLLC2cT70VMV-DETUTcKPRWXlTM39TfF6EfEjgrFyEkTooJCDEsVotU3n9ai9ifs_OKS8ZI2SZ3XRIKQnuMXsE9y6tIZEcKrQcyj9qo-gDsyhkdvH5Rf5HEUwTqEitXpGVFAo9RLXaOUxDlzX92su74y7RzSkBsedPsvBYtjmproR_2PidKVCN3SBgtwAjG_Zn98qdOCpj5WA_gKDrK8vhbqj2RzpK2g63tKbXJ79OouL4bRoSJ7HnhaHq8B8E3-FUGlKI6Dk8a5r2kUivEFHKLYWVJXKPpk5tPbneET5-40-RMXDgda29G9i9rFX7KQoabSFWeVBCVTcKp7Vue0enKWBZbfcC_-Uqb5koybQN013HtOAcCynt_ug0630ys92mcquUdLmkEtGLxH9DHEeOUkXUTuBd5B2WSkyxvh2n2kxjcMIKqD1_hkdLjr37zu4ZCWmZ7CWGQBkpwFJ-VCkh2w7XoAQ_T1QZrDLfzBPmiEh2mxEKL_dArtnfAylwOt4upM4NRkhRaHT1lO-IbKByA.XuWep53N4R2rNXPfbt2MCQ',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'BMB6dqEn-PPFAFV_0gF-DKrDrZHxOKEbMT8w',
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
        'monorailId': '1',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        if dbInfo:
            return dbInfo
    except Exception as e:
        raise Exception('API call failed', r.status_code, r.text, e)

csv_input_path = "/Users/shariquerahi/Downloads/card_id.csv"
csv_output_path = "/Users/shariquerahi/Downloads/output_Updated.csv"

data = pd.read_csv(csv_input_path, usecols=['card_id'])
card_results = []

def append_to_results(card_id, db_info):
    row = []
    row.append(db_info.get('cardId'))
    row.append(db_info.get('failureResponseReason'))
    row.append(db_info.get('createdAt'))
    row.append(db_info.get('state'))
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
        time.sleep(1)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

df = pd.DataFrame(card_results, columns=['cardId','failureResponseReason','createdAt', 'state'])
df.to_csv(csv_output_path, index=False)