import requests
from pprint import pprint
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
    'Cookie':'_csrf=TNdJQTHZ3DOahNkolmDWJm-k; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.ZwtfPA6H4ufVrbPxSHNEZ89j3VgvAdd5bhIV4ewWykKltqxav11ihx66qhvyz5X8cNz-4uy3JE6-U35UTLcktPxzDFy258QndzAzYUf0rapKWAyRyxwRwvrfTbtsggx5Vlq1xccgAtXt2IbQ443axIk6mckpMsK4qdLkeAgVAvj8iJYpXxdRgyaOtnI2CBpwwdbWGhoGu4-gBpbwbXTeBZv_Ah4H7fhDDV5VdvPhXPweLSHM47fq8JQXX4s9fj_yFqJn8CVhlPWf8YyZnnNHUjWsVxgeHuuWwZ2N2Cv5SHQPOnVY7zajKeNL7bcY8R91OqaKFAaUFhTx2_N4H0TAag.H8VJ-chk7G0ztXrv.ZtE0RPyd9CUo-qpwyFP-t6tHwpVZq3ylwfVG5J-Faf2AccnaagKG-Wq5HzAt675o_kVmYtlQ6P7nFoD_8VhA_9j377VDFRBWF4uPlse8lUogWEGzHhEXiW0JPqxWY9d2Nke4Tj36146w7geFpLYCLGeMYgiiyS9qW9AghCIXS_onWrd61x9mOhBwyrTncvHHHNytozsocMQkiEb1j_vgFNmS8Ql80SKahI6KFHKLx8mKDtwB5Bu4OZffBlSDXjvhUeh2eOiOXQOjgw_ig2n1BiKFNs3-UYKUnm7Nx_Gp6bTtOC_ZqqgF4fmvfnrz2ZIryWdbNbVas8WWd_e54wQDNFeGAzNC6fAkQ9-mmI_FrLH81_7_WzI5PQh7GJj3YROBG-4FjnPW04buazfwKZgbfc9xOuao3ztfFCPY2yTKKvq6lzWZzjmFCn-Y0O8pXDBP67_Q9H5fUi74-SoNyNrM013AsHDi5pg73AHT-y3BDENLqaLN-zBZbHDpqkJZgM7tMQ9UmpuUCGGmUEPXZV1ZkFcFdduX_WMukRrm2fgOd-DvNUsKlf9jb-mf-gyLhRkmVaIHw6CIeXxk8he2C4hv2KHtcdRkUnGOHLRIYbTbjxWYl5BuMbgDLyn-m0ko8vQP74ao1xEjxX4w2Z68Jsj5uMeKlQZV7qyvcnjI-o4kYHQ1425SrEYuVZqiYqhQHDFXi8FBCIU5SAp2j542ozspT8gfYLXsBKUpqqNaDU1lRHuvpiSzOi6KKurhFbz5aXIIEgQVGF2QCdqACkPaP3_EPk5BmiDtyYpP8sTT5rZRXRA0XIDmu9F6jc2IWXmjxcjqNS7YdzkwC80rB0ZF5Y8P3U5dqKysybN6EGmODDl2_XVtasrIJHu7YByTy2Lwb6U_6pfs5dSIrWx-zAcqhX5L0wiYBLRplR1TyJXVSaY4EyZGFz4vuP9CMfrAd7f1C8ydqnPkowkWIIW5QyZxqZ_QuNJ0GeXIsfYxPDNOm60LiLSipRF6EWMbEEvKyO0Fv9uABRLyXb6lUb5EP5wmCrO0jCSu3XmtVsQOP_N9NIhYqjFW-FpxpRJlmHAL0jDSjJQ5rdXVY0sM8SK89HuCkJgmcKMnXRPJ5l7njkQp6yazID8BL1cV5f1k-KpI8_SSMGFrePlIIrv36BU7-NDQ1LwL-9zvrX6SKAdbP9ZBfXL6IMsrFpZWuIWUiPmAJ-d6_YbPARQ6-4aMfK6_ce25Ym1E9CUWVrnoTvIRHSeeQfwVMGLMcEjAtn0o3X63g1Fo1PmKWomA6R3sw1u4l0RA1w.H6lEHsNOwUoQYBashmjeyg; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTIxMTIxMTksImV4cCI6MTY5MjE3MTQ3NSwiaWF0IjoxNjkyMTY3ODc1LCJqdGkiOiI3NDcwZTMyOC00ZmQ2LTQ3YTgtODJkMy1iZWVlNjQ2YjQ5MTQiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.Jgmh2DbzmgkhPe6T0zunzXVIM0DjFd3gfjkyvoYAGg6oq4DttXblm68yDRO0tNJhhA4kdvO7-nWK3eLTMH_F5cvP2hP08Rv9lj9gWLXx2r8SU-tNhPqpTbz0YjC-j01UnC3vDV-mqZRIwKK3PCuz45bzPf8QWMjF-xuqJnWCuFzBtnyhlhPQLWGppjUaperIHH4AIOu6_4yz3vDPEFW8M1U_4Lo434EZLfvAjsu1IQG77yn3Ox5r59iGckU5NbgVSJMTWLlJE4RhVn8lDaMvOrFtx0SCFqXCl-6VwRt8JQ5-aVu7zHGXaZU898PohSgAe32A7oL538CHuzYEtorToA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoieUxiT1RaaEtXcGtNZkFMR3pqYTFhQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTIxMTIxMTksIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkyMTcxNDc1LCJpYXQiOjE2OTIxNjc4NzUsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.dn_W83RJNyZl4IZIz8FAlWle-jHRk9oujUyyDLQeoVorfg1S7JLIEtPuxSr8Xy1EcOlSUZHkJGe5OR_cZws0rNEzE9ag0iKsunLEOqKlDyNFqnxCv10Jlw0oa7hzqeudr7TkYlP4PzxVnZRrOAczcZ2jX792HgYMx7awGY7EX9pCweOdyBW55jok3u9HF9GDNCJcZO3Z9ILXEibRsOYcdBvdUeomgcJ7I5dUX20xd2rHlSjoGBs9HuiI4AFH7hYDtmM9Ypti0biKpzKyFJknegJL5nEnnIDbz3M0Ue-612lUL0R6Aaxu4gPw4JX8wKSaj1F15_VsYjK4sjN91A04mQ',
    'Host': 'sherlock.epifi.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'csrf-token': 'k3a1vAxE-K_Px3zSBi9JBVNRuqEMMOwbTHKc',
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

def getCardCreationRequest(credit_account_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
        {
            'name': 'credit_account_id',
            'value': str(base64.urlsafe_b64encode(credit_account_id.encode("utf-8")), "utf-8"),
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
        raise Exception(f'API call failed for credit_account_id: {credit_account_id}. Error: {re}')
    except (KeyError, IndexError) as ke:
        raise Exception(f'Error parsing API response for credit_account_id: {credit_account_id}. Error: {ke}')

# Update the input CSV path here
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/account_id.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/OUTPUT_ENT.csv"

# Read the CSV data with 'credit_account_id' and 'ticket' columns
data = pd.read_csv(csv_input_path)

card_results = []

def append_to_results(credit_account_id, dbinfo):
    if dbinfo:
        reference_id = dbinfo.get('reference_id')
    else:
        reference_id= 'N/A'

    row = [credit_account_id,reference_id]
    card_results.append(row)
    print(f"Appended row: {row}")


# ... (Previous code remains the same)

count = 0
try:
    for index, row in data.iterrows():
        credit_account_id = row['credit_account_id']
        try:
            print("Attempting to get card creation request details for credit_account_id:", credit_account_id)
            dbinfo = getCardCreationRequest(credit_account_id)
            print(f"API Response for {credit_account_id}: {dbinfo}")
            append_to_results(credit_account_id, dbinfo)
        except Exception as e:
            print("Exception when processing card ID:", credit_account_id, e)
            append_to_results(credit_account_id, None)
        time.sleep(3)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

print("Card results:", card_results)

# Add the following print statement to check the DataFrame before saving to CSV
df = pd.DataFrame(card_results, columns=['credit_account_id', 'reference_id'])
print("DataFrame before saving to CSV:")
print(df)

df.to_csv(csv_output_path, index=False)