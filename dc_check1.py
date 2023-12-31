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
    'cookie': '_csrf=Y3ZyWaB54vmuphXsPLufA0wD; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.rZ1nnfh8UGF7jcXUrb_mqOzQ-qy7ZcCefAflvPQON4vBR9SbIffO2OxavzPzPFLpBS5oK080gDLnUP4N0ZFTW2sjgxvWtKubQxcC6LY-hxE7jkkfU_zfn6z9SLwmnnH6f0Umj_rEkJkHL3XF7okPgAE4ijdMy92DRvHd2fnXHgJbKM0u4uIKvqB4dm7SKoHyaaLdKNymO1sHc7cAUDxBqfbYz3udAlfpNS4RJww4bc0d47rn55RhTq90MAuZvOo_By2nzpxu6LdeVGdrN-fFx3NXB955vcjgz47mP2-xUPqAEmZ55h6oxwp2wNkqgg1c_Z06MdslZbyeZExc0fXNMw.sAZRBHdeso6LnJjw.CvfraBLyeMwwUM545cqdeRuD96XTjtNOanZVGcFqAzMRbIUW2tfOQJzM2qXa_j6a3Pk42i-JBhQ2p-u-JHyjwkSS5Ti9McWJxTkRXE6Ig6WHZUdr92EKjgPcL2ZlBrxDTyZM8u99rSZArdGnFtAtrZa83wQPeV34pcgNOKNRu5mRV5Gknxh5QXgIaYgSSFv0ka-ZCJm2EbJK379sOIydj7Eb3bGRxP42kBDfquO-DXOW7JkAVzgfafwUa-pKHkD2KoHQz-CIwMpbTTqtmlSzknLrZ4A8w703kJb78nQ8FarL3rsixebVqIh2-0OyTwj6v11pjMUB3Xcl8oAcU8oBxNCv_wCR_N_-c4KEWrWu6FlPpfbrBi8nHpeb4NraQZG4McpOkio4S0pA4JAhISF38v_quqjuXMQYbj4MOPJYt6pyJUVqMmVx_TzYMNwwQ3bPIxqheKBQ32PIwbZG4X9u5V7-abuYtUxU1e6-DMZnn5gduDwqmKieQ2UBfCgMtZ4S9bby5-AOJWkfsWOB9JpzBdsjx-iqnC9egSxd1nIn6rXwpkh9ZV-N0Ej478bZeyat7RQ21vKbtZhugQCwaKmuFTeBig3X0OdgpsMBgEzesYsDbuiSv5uPMgW2obSC4jMEX8-Vp-HvuZPOn0HHmSkgNvJty4MBHf-IS8FkX9AhnfEDJbCbC8LmLX40VOn4lfAZX41glrwmiTqvqSxGckBwtZOIw7WXHrAhK7xN627euMjLN3KfXqejQWMULdh6ZSRukmOASwOdPgX1W_pHS26h37lr3gzvQQc_LwmgslmtXmJnqvI9bkCCY-wUbFt5O26Ry_uougAEt8WEm5vqSwm5XxhptM7a_Nxr6dhrmsubvDbsSEj4-h4lI3OOMma20L8g9mXYzPkwSso1eoWLUiXHxrX5Ec0UkmB50RiYvUPOMw7FO75x8jeI1bRoTXtfS_MAnHk6y_Eg643OtQx4-CgXj5a9v-Outkrs0kxV8AP0ZFaB4wGmWH2sGjdZiA0CgB-z2V2TA35ZTtpv-Dg4rgWIynrPZRnD3v7tTz9lUe1j61IWKF0GoEP8NXUVxuTAG7buSudfoCsJ1ty1b1GsBIzjya7itVtzHOOi2imK3FfpTyDm0LbhAt5rigT1WP3pQCi29vBNaot2pADPGMGPkB7qFxT-g_UD7FA9E3MJ6X_gl8uyBuoCuiPZLt49tshOhmSivGIaNZZ1_r-6nDdGfzWBc4wNIqGUr2eY2J9YVPAle4HIF_4V6OoLft0jpxG5YU-I3n3Q4hg2H0kJg46pPw.yon0R0yyCSBKaC9y6-zipA; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTA3ODQzNzYsImV4cCI6MTY5MDc5NTIxOCwiaWF0IjoxNjkwNzkxNjE4LCJqdGkiOiIwNDlhN2FmMC0xYmY1LTRlMTctOWNhOC1hMzQ1YmFkM2VkYTUiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.FtmCqcpW9nQeOuBEIL1obRpLXOGP4c0tTRVYh_eKrcFT_B6THNrPgFW0tv2jlEVCvDFgoioGWpkqDp2SdW3mJqq9AdYy1iahypj3yOGeEqJrnm8gEi3-E6r782j3vyS2WSc2gTe_9oQ2lkZAmXu5E5vq2nYOzlVefuxC7ga1_5d8315gPvvMvRnq7HOrDl7r87xaFeahPimLuFzdKZC_53U8PyfcslI2mjSNEbT4zhQDEA2QkQNv5NJMIxygB5A1JinNYiD6UmChYJc3NKfI41ZZSpwZ5PUzP8JLuLnPqQpRu7hghbFc2m26xIMVZQEwIG5dmHG3SHJCzMJsdX73Ww; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiZy02bENoRW9TY2RYU3pTRmNFTFpwQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTA3ODQzNzYsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjkwNzk1MjE4LCJpYXQiOjE2OTA3OTE2MTgsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.CEXjilVddnMtE_EoiFQU2Uro23lJzmI4rjE1KCQblvITkPvXkPWhyjtjwu3IdfBjmLiKSDADDUqzYncr5ledu-TaexLHmJvKrRoH4zGKWeI8RhecvXaFPkFJTshcO-vPSGWM312FUBYdHWoqPk5w1U_5kMKmPVwxfZuODfiwAbs3Pd1mG1-j-AxNDFqQHllzLkt0dhdguifzS4TjckxGeVdSHvo2ysk4Dc7fODcCuj25OHMeLa6zVdKjNjznHJKKhzlFbN5GuYyVAwlj0dFkmjpWbEjKLdeK9esGCvfrVYEzTSYFP1g9Jvxa90jRTiRUl44vJIxBvGhdjwXFcfYSPg',
    'csrf-token': 'D3kxrZ5M-rFZ9efPXAW1LIqxhiOEOgfmjebY',
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



# Append retrieved data to results list
def append_to_results(ticket, actor_id, status, dbinfo):
    if dbinfo:
        card_id = dbinfo.get('card_id')
        state = dbinfo.get('state')
        card_form = dbinfo.get('card_form')
        bank_identifier = dbinfo.get('bank_identifier', 'N/A')
        masked_card_number = dbinfo.get('card_info', {}).get('masked_card_number', 'N/A')
    else:
        card_id, state, card_form, bank_identifier, masked_card_number = None, None, None, 'N/A', 'N/A'

    row = [ticket, actor_id, status, card_id, card_form, bank_identifier, masked_card_number]
    results.append(row)

# Set input and output file paths
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/act.csv"
csv_output_path = "/Users/shariquerahi/Downloads/output_ACS.csv"

# Read the input CSV data
data = pd.read_csv(csv_input_path)

# Initialize results list
results = []

# Loop through ticket IDs and retrieve information
for ticket in data['ticket']:
    print(f"Retrieving information for ticket ID {ticket}...")
    actor_id, status = getTicketDetails(ticket)
    time.sleep(1)
    dbinfo = getCardCreationRequest(actor_id) if actor_id else None
    append_to_results(ticket, actor_id, status, dbinfo)
    time.sleep(2)

# Write results to output CSV file
df = pd.DataFrame(results, columns=['ticket_id', 'actor_id', 'status', 'card_id', 'card_form', 'bank_identifier', 'masked_card_number'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
