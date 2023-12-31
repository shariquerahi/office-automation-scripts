import requests
import time
import pandas as pd

headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_csrf=r6oa06-B0jCXBWhiA5Z-JPjd; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTA2Njc2NTUsImV4cCI6MTY5MDY3MTI1NSwiaWF0IjoxNjkwNjY3NjU1LCJqdGkiOiI1Yjk0Y2JjMS00ZWIyLTQwMTgtODcxOS1hODA1YTZiNGI4NzMiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.a67rRIKAFuJcarzcvuXGl4sBNoibaajPNdrQ_Ipkcqr71jda-yKejqwj6C30DO2hHmnAPW1NWekt5m--ES2ObO1mrf4zpCA9au5-W_VDWgE_TAdBq4WZskaxwAkV_AS-oHYOphEBJQ2GGeTJoD-pNOyg4JO1LFyXFq20xablOyBsT2DCOsHKGRfc7O78kyY_IkYLz97H9zwl1W-SIuLscNFVuPtqv1N2wMEMTVC53pNHsoNc91220zSs52UVgPr_kwuvvGfBxOPc94yjspO80jeeGi14xC1LuBNPaQqIPcII5xG0fUANrZNmZdmPxw8MJIxHtMbXMtTCNIxJT9IyfQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiNkNxd3lzZUFMT0ZaMG01QVJmSFM2dyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiWWJTdE5CdkdPa1BDMkhzZEVsWDN2WVRtV1hvMUdZODJTSzNid280elhNX3J4WURkcjJMMFVDMmIzbU9PYVVBSTVaeVJrZ3FpejFUWU5tdlBTNUpQX29UeXpEMVEyTHhCT2xrWmwwQWpIT1BZSnB4VEliMWRJTVhSYTFaUjZ0UWpVQnlYOUVRejlLcmtGby10MThyUDFyN2tCdDdFYjVBTnMzeFk5Ukc0c0hzIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5MDY2NzY1NSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTA2NzEyNTUsImlhdCI6MTY5MDY2NzY1NSwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.Vq6beFcKwaqU0XUqywyP7DlTNQGXsoUrIWl5WTK-LwRMUZBQz59sQImWo-1i889KIh3bx6MugK6OU6yS0-aJrwnAPZj-9CbPq51yat9-9HuAYPs4LdUiQ6SlBEtsUpSXzxfP_LNZHqMa4SOjIze85MSQEs_GG4AiTOLGRIaud85SFL3JPi9vXg7RmjmiXL4v4H03wlDWPqn1uMiIT73wk55YkMLz4p3RBMHbb-VvQwf99d7G3voDfpYA1km7MU9k3jW1PPmiOHgpGTn0VUxQsTKsHJYTNt9-kQYgfXYqYJskIKDy6BYAXlU2c4sm8okitMZKCbrKJzNX7hpkw84gKQ; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.L07g7SJqRXuGubxAwEBlOkLyAixc5JGLCRTrIEYP8hJHS_iVrbS8aKyNNmqLDz8y27T4MgNeO9rBDn7ikAgVF5ovvWNwvnz2rpcTJQM9mLs2s-GhYoQw4OPQ46LhMf4pk18N5yKgbGSSBM6IacK1C7IX0I5GWcGTLWiyNQSj4kkvUjZdVc3c3sjeM2soWVEg2nZ7BK4Z4-0f0zjTHAu25gP59j3Gasftm6ZXcf_HXr8lqWstetlzGs30-pi2j-5tcn9oKVP4ydAzbQH7BrVwMA2jXu4v2CMdU1mLjNfU9JfDk1X9nqW2rVOGkFJljc4SqBfsrHq1PVn3rd_4gpfx5Q.fUt1Osrj2uEpviEw.FXw26DQmKh1nkUzV3ZLjLix88GyiJGmutZDQgvoeNhsAQ9aNoST7yMIjn_NsG7si3wmDz7cvPPf6ussI7MSd5ZpNphH7bTJeT2pKQMuZvPduhyk7aYEvlpgpeSHjf556aCyJQ0hyy3kqO2cufpgM8d8f75YGttcMqD1rcQutlNYUsDndy2gtL0dActklukjPMlDXllKUiuB-9s312JPmC-3Zj3wE3rPPmzjp48_k4HxFj5929r5XRcpSKwVZr_Uqq67Gskn2Ic-NRpXF6I_sg86V6728HOLhjbnGBjfEh8yrtOJjMVF6OhI-ChyYDIVhkVnVrvT4UxeoVhBmfW6w780Q3wWFtpLSEcFdSavDjZRtxEdLyF_KoA440TC4VzfVRJKgU82ppiNlJ620cx34qdJAvrpiTx67OT21XyhLboCGCAk38vlzjaN0vo1RGwLuxov38W3lGSWVjRk4Kdbw1MVIUTwK2UVJQLF0I2aWWhhF1fVXnl3G_DPY9MBYNc4qkoprol5rmrz2S0Ck-XB9QBJtmhuzNl_v_sutSqIghQVK6CWQ9HN1pgP3ZEI2C2KMakTW42AHQuqnJw57rhph2VbkJ47qR81syBep6MhFy0CvG2kZ6uWQ7scbwXcbZLrYRyD1fxDe64soqRv3bOEF8O1ONVAg3qM_BG1S5oOKo-U8nfKTbsSTqagsPe7XsUbrQYUx1OalVsm6PP34v32ChixVkh1eW9O0rHd2bKN5p12ht7gLuX-YHHiNH03z710N4iofA0R1CM-abGXcata5HgqImzR6Yf75F5rApvd9CUuwrZOxswOdGyVq7FBQI1bxrfDsHu4CMXFOTm_dXHAGtLd9LL_X74esa3ylMUhQDnyAQBRYTx2jZBGFQ7kJ3hKCCNMdIxWzWh3bBuDYklsuvBgOW3JqoHsvNFpwKkMn4p-TGW3z0-0SnPzMP4V_0jsmOecVMhc9IpKl0pFca3fzSlYjJ4e5fKRiyGBuf55GzDEonjsmVjETW9zNIszAFP9EUyjVKEwynatcGkj2pKNdK2hZsIwIsYbwM2FRaEW6mgrZObFRsvTR-Ab_gWcFpZpzdZPA04P0VohYgyR_wXVSNnte8EnlbHb8cx8eoOae76dx_uF_ozyGIJqDVYpt4PScyipUNp954bIj2vtk4X2-ntnSroedulJFykWj6KdjXAaGkoKZTzn86BKgA1N-p0CGBUw5m7kuvY63NV94xtDnkVjoAQ1Fgg3_wfbK3evp9blrVbJj6WZon4pSOQIKrh0D5LL3SiDFdN5x913yAw.ICAktke685KnhmuYTJINbQ',
    'csrf-token': 'GZvyvTq3-AUWeH94Rccwyz0zxhtlfEME_qNA',
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

def get_card_info(actor_id):
    url = f"https://sherlock.epifi.in/api/v1/db-states/info"
    params = {
        'service': 'CARD',
        'entity': 'CARDS_FOR_ACTOR',
        'options': f'[{{"name": "actor_id", "value": "{actor_id}", "type": 1}}]',
        'monorailId': '1',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["dbInfo"][0] if "dbInfo" in response.json() else None

def get_ticket_info(ticket_id):
    url = f"https://sherlock.epifi.in/api/v1/ticket-summary/{ticket_id}"
    response = requests.get(url)
    response.raise_for_status()
    ticket_info = response.json().get("ticketInfo", {})
    return ticket_info.get("actorId"), ticket_info.get("status")

csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/act.csv"
csv_output_path = "/Users/shariquerahi/Downloads/output_ACS.csv"

data = pd.read_csv(csv_input_path, usecols=['TICKET'])
combined_results = []

for ticket_id in data['TICKET']:
    try:
        actor_id, status = get_ticket_info(ticket_id)
        db_info = get_card_info(actor_id) if actor_id else None
        print(f"Ticket ID: {ticket_id}, Actor ID: {actor_id}, Status: {status}, Card Info: {db_info}")
    except Exception as e:
        print(f"Exception when processing Ticket ID: {ticket_id}, Error: {e}")
        actor_id, status, db_info = None, None, None

    combined_results.append([ticket_id, actor_id, status, db_info])
    time.sleep(3)

df = pd.DataFrame(combined_results, columns=['ticket_id', 'actor_id', 'status', 'card_creation_info'])
print("DataFrame before saving to CSV:")
print(df)
df.to_csv(csv_output_path, index=False)
