import requests
import time
import pandas as pd

def force_trigger_recon(card_id, reason):
    url = "https://sherlock.epifi.in/api/v1/dev-actions/execute"
    body = {
        "monorailId": "1",
        "parameters": [
            {
                "name": "card_id",
                'value': str(card_id),
                "type": 1,
            },
            {
                "name": "reason",
                "value": str(reason),
                "type": 100,
            },
        ],
        "action": "FORCE_CARD_CREATION_ENQUIRY"
    }
    
    headers = {
        "Cookie": "_csrf=0ZXBTbjxwujz6naKa8cHrLfA; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.uw2vzz5hOhzfQ5xa1NqxCAuvm25fvCotpyej4VTl1JilxghVyI4jplnTlOgBpDC2xhYXq9QzznPrk2BHGGBx0r2vRdRvZPWtom_mMZ1VyMH1diyUSYkpPS1jLcW4wnaVnOs7FM83tyq5tdtJKju-2K2UsJTUxpe59ph03n0Imk8dZhmnq817C8nHSLPZcbWV_sEw_2tc2kmwXyOajJaFhEO4xEwDavMEzpTI6Qe82gkcfn-8wBavHnmGmEmEk6Qu4mkXSMD5hT4tgRBCwsYmSfzuKhW6GgZgU87EXbF96X7Sx-6PbYhNAhbC7EMKTTbzUWK8uEEOVgAR9iKMPH2qDQ.9_3Wd6mIAs3VBRwx.evJLMRnlgabaPtoflXv1kNMFYp9E6iBy04TFodJJu9lKyVjUjzwAzSFzwpD5FEB-VNcLnZl-VvU8dk4dW70WWFVE8UzH5RDasb5o1SIrW_QWYNfbAh0P5VBbvLFhtX1GSewSZoevurueVmSOFgX_MckflrYmg6AKa2NakWRg0tFf5VLM8gmZwPdR8KYeJdYJnO7GOssFN1O-5nAIUW-G-TIZmKylpij3J7oZfsRZXl9jrbei-hZLq96pJAuEL2QCb8wco1gL6z6I49mjr_o8_IDkXGn3ATY8CW8GGJA1977gD8lftnijfZ0Y27dDFxGDq7fEMIiTcFFN7vbqP_Gb6XlgulT_w5zQFokLD8dIfotWp5nIhverO6wHWS5QhWCMYi7Yhkr_0pu5UT1_N6-PJo2zBwBugguxDivjrNI_EJttkA72wz3WolUzkySVmobn_qJFuMPGMKzSHydy2l-aS0O4dJandAhWyyQMP71bjc6INgpQgzi23kOmxGNWxSgGPxKHyrGi7358EsjPjntoJfEK3wJFeq9tbD0YRvvHo5gHbR92eVzi2wkDLNznVo6VjZveYV6KxrLbBP71KtdFtBwKlBc97QxstcLR8txPcuQHaclXaID27sdcF4PEjg_iIRj_k1l_YL4QauUJiIIIbJh3wSURLg2uA9jEDb2PAlbdbYgPGvG_mIvcgZw8RktlLu3OAIEDlLMS4TQlJea7A3nsTq5XGPMvaNgsl0OQz25maWc4uuhrfqsarUzWUc9ysB29PGpVWXUk9uxSn5F35tjtUbfj523agHy7hh5rylqdXQOfrYeR3Z9v3kMWdJBa1L48jb5xBPsXRqT6TTAnwlGfDor4AxTx_ITrufJ9Ueg6tsFxjIljqgxLa2jOxHkAca10y0lqcHgKzl-CqjtVMbskdxSgglERLDq_f_g_bzEqRC_PDSHR-xSWmaGLT-DeufNJND7dcZrH3ExjN2BMtoFJFh8uETJitHmXUAqNmgNN2droXPEr1E9hWETJjg-NU56b7Jub40TFM9qr4vghCFfFdUOVgWFSx7ifegPOA5Oj_-eDAc-0YDflSXkblAaNqxT-SUPL6rZwf3ebA5mHXRXWpP-FtN9gYeNPUo78BeC2lN_94OkLrvpG-ktkDkZche9RDlzyKUC-4D0OJkhNUdEViIsoNVQ2X7SL2x0kc2vK9NDGrhgv3uBhS2vS9qsH8ZDqgx-3fpjoyOUaQYxn1qArUFytWvjVwNlhACk0uIE01ADkeLs7WAvgcdfVfSCH765YpqlDU_pungJCyQ.zf-ZDZuDMXrsflqukpZNAA; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE3MDI2MzYxNjMsImV4cCI6MTcwMjY0Njk4NSwiaWF0IjoxNzAyNjQzMzg1LCJqdGkiOiI4ZWRhOGJjMS0wMTJmLTQyODgtYTVkZi03YWIzZWM1MDcyOTIiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.n5Wlh635pgS6yinLWg99LFlPDdXL1OgZapLNMr6xJbjDpE-EJIoW_DhsbZKMZaVuzOQ5Jl_cHyUzxLjgdYwtImKkzNKl5bAUQeUca27eMCDALrWBOR2jjkAIaVUCrVwpVZnYG0vs6t-eyJ5wepEQPs79GtjD6dVwXxA9fozMVwYcRcQrUvyxupSGFODgk5zas_UkEOeBOEnEKSx42fRty7goVpqGL7JeZTaCC0mK4tBFWScCNbMbZU3m_AsthfRnK1NZ7BkibJijCKIcraLVqRCRF65bBYQel385wpOMeuCY3Tp0cz0z3FOvYodtbmY5da59uk7Refgn1twRgnr85w; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiTjhpUFV0cDV0Yjd0ajFzSDdRVGFOZyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3MDI2MzYxNjMsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNzAyNjQ2OTg1LCJpYXQiOjE3MDI2NDMzODUsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.Uma2QlFW7W4VdCNzntRkjTO0Hu_Hm5vYt0AU4b7zPcpAw4Dwecqlb5QCk2XFGPfsl0VBggrAmw1ED_gGneK1PDz5quOT3maU45UqCQqhx79AN7zagjpJFPOQnoitdVLX9ueM8kcoLYw7rVajAzX3FeVVydIQoVR6ZuSDfiH0pcqK_JEocUQWLHD4UrSHc0bY1XcFIejcsv8ovqrdzZ030kdHPiMv2dLWIqDyttP4N2x4RDw2GJl2TZUMgYqbH5sgNDWHSWWFVIL1Opj67PZycWJ6Ydvebpe61XHtzNfYfF0lkR44Qv4Pwsy4bXa95zaKJ4PWBvQeS4N8dL91avzJsQ",
        "Host": "sherlock.epifi.in",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "csrf-token": "6MwZyt1E-7x5gmYX4lE9pjBW60EUS5grhGcw",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Language": "en",
    }
    
    try:
        response = requests.post(url, headers=headers, json=body, timeout=40)
        if response.status_code == 200:
            return response.json()["executeInfo"]["status"]["short_message"]
        else:
            print("API call failed with status code:", response.status_code)
    except Exception as e:
        print("Exception:", e)
    
    return "Script:Unknown"

csv_name = "/Users/shariquerahi/Downloads/disbursal_stuck_users_list_report_2023-12-07.csv"
data = pd.read_csv(csv_name, usecols=['card_id', 'REASON'])

try:
    for i in range(len(data)):
        card_id, reason = data.loc[i, 'card_id'], data.loc[i, 'REASON']
        print("Attempting to trigger force recon for card id:", card_id)
        status = force_trigger_recon(card_id, reason)
        print("Status:", status)
        print("-----------------------")
        time.sleep(8)

except Exception as e:
    print("Exception:", e)
