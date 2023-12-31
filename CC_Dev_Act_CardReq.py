import requests
import time
import pandas as pd

def force_trigger_recon(card_request_id):
    url = "https://sherlock.epifi.in/api/v1/dev-actions/execute"
    body = {
        "monorailId": "1",
        "parameters": [
            {
                "name": "updated_card_request_status",
                "value": "CARD_REQUEST_STATUS_FAILED",
                "type": 5,
            },
            {
                "name": "card_request_id",
                "value": str(card_request_id),
                "type": 1,
            },
            {
                "name": "reason",
                "value": "Resetting work flow",
                "type": 100,
            },
        ],
        "action": "CREDIT_CARD_UPDATE_CARD_REQUEST_STATUS"
    }
    
    headers = {
        "Cookie": "_csrf=0ZXBTbjxwujz6naKa8cHrLfA; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.f0WYRJijh6ThWWtP0g0mfw8qcp8hHN2X5pnypWEp5et8cZ4S27KMoA7A-w78hmi_amKmyi9JcD2c4mx6O6tWFeEvlGnWzB23yZe6x4Ko8mJS99JsOKng4ombC0Uz72L5SFXynmH0OTqagEU976B_V4DspeUpYVfwtsaA1xRArSG9PinfDmbj17uqbxp0FjED_-8UvmivAwKS7jpX2bShYX3tcQdC2owxqAbJHOP4JXtedIURZW3Mjd5fiwopnQdYlpzo_I48DRO2h7SpmNnKBU6N3R5VO2909QlEEHA9r88PDfjDFDKPIJTk54AS45idExAwLl2ARSWMf6iB14zKgQ.831NPok2sg633kI_.PO-vCFlxNBDfYibqP2TqqIOQi5INR4JJiuYc0FmrUhEbG_QV10DDGQJEUDSeMFOzSrql95Ys2vDAqeFs_CyGkFAiWXBDbeT7ws6rvzvXxaf6LDcXmfJPJBjAkUf2UBAuzGQQ4XGyjct-xeDCP5pywSUXIwlFx9Lrivl0Nsfdm4O7k3iUAaNHA9j84PJZKp6FX8oYyQ1NjCck0_x8CNp6neHf7NBTIi3BtmCrHt2dvkFiCQyBWQIATes4xFc_crPIDD4BdBRrGMdUlLmK96wDzh8S1wgYYdxfc2wHgz9_XzQ98zL6DGoyPqHPBuyN25S3-swO73QYCM3AELIbLBybpuxvrESTPd-EgP7vISVuOFhGEyKLI3GSx7UFyTtuTyqukxBXK9JWHYx_3bPRr77AURKRBQN8wQXDFv6VHyujSvUTAUCrzE1F5tfkaNlLZY4e9TgrVeZICm30_oo93Z0qfmX_DrtP7Ng1Rv4beJZDnFSvh5p7-s1deTdvNZbjLmz89EmswTwHKE-lSnXN4AHC6OUw6-_CkVkmCkKIWHur17z1LXxWTCvaFaxgNqkoIGauB-iD2I8NXD7KpBY2tpEmSxWHZy3UPGAk_MajDGBCy7oa-Kozt9zFheoyI3a66vrHX12dFETurtODNnwsaa3ytTwHxWI7oSJ9onhJR84PvVggctNKHaqio67BC1hHT8oEgIIEFU1TyvC9m1_Ko6bMMipH1zwIKgvTXUjQ8RXObMLrNi6epeDorJ_3rLwky5KmP97q0WQ2HRT1DNv6NwY-cAjsW84xkeA0vzLV05plOh128dI1SIpoJsDybT1-XaMjp422XAX_REMppj--ngDS7bXpZLSrzwVfkQqN1Ld4vesEH_1z6p6hGRQE_X_UiLjd8lakD_rwdqKVizAxk3PNzgCwaRspHkPYQgP3C2o7LSdy2GN90xxEUCblhVhJORLXrl6ul0qtVsRqPf29Gs9G3bqmbFcLaSmYBXXLFx6hDUBMgvk2-Md2Klki3IMFT4k4DrtM_z7Ta_aZjOPWOJqjVFD6j3J7BcwcSeCfaHv9LL1iMhLsVULzQ6TTN1WmPaAEznO7PnrdVarOuuNGxH-S4EYKT9Kl0wFYyFSlCy2eZUSKDQAcDTsGVDvrTYIwjvZ6JrXQ68Pb67ON052iKwwOZCAy0YVOVjlq3m5AQLRvNA1xrreGEw4gnUs6nuNgLzBH0S2jZgB7dlvqUN_aVp12q9zbWI8ciAuSnHcD6h5UYwY27Cgci7e2sUEaGRi35CFYdvLCTLx-vQ620o-GHA.7kufzKEhHt2nSjpk6KhIvQ; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE3MDI4NzIzMDksImV4cCI6MTcwMjg5MDM3MiwiaWF0IjoxNzAyODg2NzcyLCJqdGkiOiI2NmUyYjQzMi03OThjLTRhMzEtYmIxZC1lNjZlZDYzY2FlNDgiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.YKKUjBliYvHZoOkPZjBWpyTl5mMMZIGU-rxDjo0ygpbizhfWMM0FkWMVp6qzQk337ygmQdPdetoBqvt-z4yw6IvwMTTsV3p1tgAoAea2sQ8IcZWzV804wP9JCSeXbqxDJ5NphYRGta7wp7HSnNJ-FgCNhycNqu0MQC00q0zx5LmrPtfEeL1_WxXFHho4wrRjhbHZNR3BucOP-8fcClPTXrwSECeBP_lFhDxYmt5sbID6iKQmXmTcsuZ3DFhMqz74lDucoagqLMCi4kEaG96-ZCYAFE9I8Kd2eBOHTKz-3_2WLQruc5sEBbPXi1VoHAWmc12oGncOIV4G3zNxlm3H6w; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoick1yVGNfa2lVOEZmdU5uS1VHRzlnZyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3MDI4NzIzMDksIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNzAyODkwMzcyLCJpYXQiOjE3MDI4ODY3NzIsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.evltOzp30xxWuldhQEPkltDc-h4gOUhi5T-trxsfYHOsFjSYvQWvlfnWJfRiHzxvp1sSAnQx3Mh_US1SqbXONv76GHz5cFrJoQQISjfokb2iuRMYU3t4OnrAK-4UmTNJnPEet271mZ1TVqaX8CIlbfNe6NPDI-BBJVCfpwxmQgSGdcGHV5V4co7j9Jmrw6jvzeXryHAFBK7L2bBUtCYW7SRLDu7uFl_H5ibDuiPPC-eGzhDgb0mGcJHw1zZ4APAriV8amj7mm9VB_ik2iv_uOSRepiLU72dex2DJswo3gArLSBtNGL2NmBEb49dvLByKknM7jQulkfjx5rGG5ylVQw",
        "Host": "sherlock.epifi.in",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "csrf-token": "yrVFgLDg-KfJlouAOEqkZt7tG6ooGtjQ3ZKU",
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

csv_name = "/Users/shariquerahi/Desktop/Git/Python_Script/CC_PythonScript/card_request_id.csv"
data = pd.read_csv(csv_name, usecols=['card_request_id'])

try:
    for i in range(len(data)):
        card_request_id = data.loc[i, 'card_request_id']
        print("Attempting to trigger force recon for card id:", card_request_id)
        status = force_trigger_recon(card_request_id)
        print("Status:", status)
        print("-----------------------")
        time.sleep(7)

except Exception as e:
    print("Exception:", str(e))

