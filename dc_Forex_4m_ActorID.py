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
    'cookie': '_csrf=1cR1y558WixaY3txelf4ls8i; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTUxOTE3NjUsImV4cCI6MTY5NTE5NTM2NSwiaWF0IjoxNjk1MTkxNzY2LCJqdGkiOiIwNjMyMzM3Mi03OGQxLTQ0ZGMtOThhNy04N2VkMDI4NTA1NTAiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.FMS8rU0R7wbdSr2oN6wqoLm7qA9stp52Xz-J9BRD_27pA1ISeFXnLw8SVtzi5xJSm8lYgGIR9vrLKRp4B-1MCEkBQ9xG2PpaaDl9_DOAccKO2Ks3mqydP9YJO-VBQNQXw69rs264pD2TbOH_vK9sApoukiz_X0QoDuDRZncUEIXYzlWwN7rf1dfub6zSBFMMFfpTYd88TnLQ7xFbOCD3xj3-hMhAQojG2JqQVzdlAl1lG8u360xcioOf6pviVoVQJpVEsBvrgvzy8VVrKqk87rxe5Yvv80FDJ3kGXdCfaXhAkrvmXLlPO3wkIN2IC-Fbd_76MVr7ZUTW1Wn1LfartA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoicjBCSndfUVluTmxJTlo0VnJFdVJpdyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiZk93U1dwWHlwOFV4ZWpTT2tJV0RiZjRNYVpfd0lpT2N1NFFaOWdpaVMteEdCUVl0QVBqeTJTb2pGcUJQeEZSczVPaXV3dUJCNGdXQXB6OWVuNVhMRDFNeUZsTkhmVlpvQzhRUXJ3Y0VSc3JzR2plQmt2NkdRWlJQdjQ1bVUwUmxnbk9TYTVpaE41V3VGLTk4aFp2X0JNdmxjWGtOaG1SQ3lvYU5MQ2U5LW9FIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5NTE5MTc2NSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2OTUxOTUzNjUsImlhdCI6MTY5NTE5MTc2NiwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.KDH9BpijkM7zL3meZ5Z-RZzRvsq4tmxTcLtHnyY6LzRL59RdahQQeF3uPkyCfO0rs9J8nhZfM39WqlThduTg8PGVxUlagK6d0w8EfvTr9oyh7k5L73jYu6Oe1WtTULv2MsJ3bLBHlqe6tNieqsdShQaFc7epS4YsaMiVwRNlCZ166MG3KQE9x-Kk6CWQQESGizciTyHDowXNlh7QIjkrrd_mAnzw8LThJt4lVaQgtVR6qGX89avjDieNk2M5JIHTCi9hPN0EjXoQ28tUZh01F9guRvzuiOw3dmI5Ct4i4aUGpfvbjcY3GrCrSJCxhR21CxRG1hHpYveSKy71ZmJ4HQ; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.BZvDCaDB9cF4GEss8iiH_a0AfrdZ8fTW-rMxCfUtdnevlRsdzjCUuF85qNilXJEZD4vrlZWG-ieIQs6ez9Bi-KPwwhNOjPUqYainu0hqiEtB1445HPjupfK_ops9dcs12ZSiMsPOLT_cHrPqRmCT8t8meTTvUOwAiJDsooJhQbg1s0OxaEtgfapt4CzCXGQfBgvPk7YgdkfffE_69jqNijFacnb9xMhLxerDolA0dL-OlKHxBLxVn6v1tKbEyaxHSGyIlg3V4jvHZZe3d52DVOKVbVAEY0o9d8xPoSWjomVU55MW_htCDxard05P3yyCcH5CTF6Y2cnIC-mlQC9H9w.D0vA0M-ts_CICqFm.qdxQ-dAmbGxnSE8uSSfYUVR6HUURWlK-uF89BdwnWGgAwfgxHARtWVkDRrisp7cP1PrCKocMqnKtQNVtqPDSNOxaj5Q-YYuBTVL2U7xTnlte_qLcl8abH_gNyHoPI44DfS_gvsdhjAil3OxmOh6J7kKBCeNwQBjZUphQW0SYOC5cGvd2Pc1-O1kx5gHeRl92TjddPfURL2i4R9ut7QN3nvZMx3R5o6BljdSDBoPRX-1P6Qg9tBj83Z2DlxG7tLPIJpCXrUmGySY_T89pEeKs-WWCSEsoJU1bxnkf-jfI4t9tlZVVp0dDXQ8AobfmMcnFAc-8z85cJRCY0lJLmjU5UhD3NpNZXoRjYDqfMxgDP9FxOPporXfb7KnUvJSKNVbn8DQlwN8O-8s8efqpiVKVOgSP3lS1UqFbOtWtY0tGb5YZrMeC4zDn2y1PlOzaa02Rj45eyJ6FRMaGhjdwTnbminER9oCcDaGb2qPACMOKcKrUlyJ0oqEwjpyG7yUFPqDtID4HhCuaazoLg_TW3yETUhfgUwiYMsFSeD917z5UTPp20rvGz9w9TZQjueFfcFtaKWBmBMcq2Nr1cYfJSGPdpF7bOYCf9CxTsA9043R9wK28sIT6loPZLMyKdDysUbu5OPTL7fnMFDBm0ohgcnfnEF8zdytDjeD7zZZnY02-zcWM7TvsUrPBOjqQebuZqzCIk_YhiV0XoQ8XxGdE1et1girVUEZBN4CDl-btHBRZypR-y-mbQTSIQmg0UxQVGWy-kcJVwEeYg66vDYo4CYVnehxBdYclUi-9ZAxX8JA0jkbe2frjJDjUCi8ZIPGAoQSPz2P1avsLPr6oe_c6S6mkVims8eajHVCCGpdbe7sJjyF37zLHFXxGaOFBaPJ5Jcf1eMIRpcW3AM9iyIU3u1EGXFgguY2lOzypfIW4WFQpklXTJ3qgZTXR3-LNmopYRyjAzCsBBWL6w9fEHYqn1rc8NhAxf5fVL1XRC1QMGr-pMokw-ksq7g9smLwslRoV6Xl7TNnyV3Bhu7tzRRKkG6ksph1jshJUC0J59Pl0EyCTs0Ta_VGCHSelRiyFL3jSw35x6GqUMmT9d4-Jeh8D1tj8tfsnQh7hBdLS3luMAXcw9Bg33BySCkPdVarxT_st2DioSC2ajIJrYcmBnRer4P72YuCWxXe9Z4hrMr76FKgqGPdOLuqqnZqkVT13cz2VlwjWIMpUMqSL0Yi_kjblA1yylJnt0yDZeU8Cg9hYIhsvg8LzIUCYeV3gKsNwlD3Yd13s1Y3LtU0P7_-xstMUgA.kS92x4xUanNsWbFC1F6Mrg',
    'csrf-token': 'QQ8dSc6T-2Il5Au_MJqIS4j-2SfkPCieRI9g',
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


# ... (Your imports and headers are the same)

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
        'entity': 'DC_FOREX_TXN_REFUND',
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

def append_to_results(dbinfo_list, actor_id):
    for dbinfo in dbinfo_list:
        if isinstance(dbinfo, dict):
            txn_id = dbinfo.get('txn_id', 'N/A')
            txn_time = dbinfo.get('txn_time', 'N/A')
            txn_time_user_tier = dbinfo.get('txn_time_user_tier', 'N/A')
            total_txn_amount = dbinfo.get('total_txn_amount', {}).get('units', 'N/A')
            refund_status = dbinfo.get('refund_status', 'N/A')
            #refund_amount = dbinfo.get('refund_amount', {}).get('units', 'N/A')
            refund_info = dbinfo.get('refund_amount', {})
            if refund_info:
                refund_amount = refund_info.get('units', 'N/A')
            else:
                refund_amount = 'N/A'
            forexChargeAmount = json.dumps(dbinfo.get('forex_charges_info', {}))
            created_at = dbinfo.get('created_at', 'N/A')
            updated_at = dbinfo.get('updated_at', 'N/A')
        else:
            print(f"API response not as expected for actor ID {actor_id}: {dbinfo}")
            txn_id, txn_time, txn_time_user_tier, total_txn_amount, refund_status, refund_amount, forexChargeAmount, created_at, updated_at = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'

        row = [actor_id, txn_id, txn_time, txn_time_user_tier, total_txn_amount,
               refund_status, refund_amount, forexChargeAmount, created_at, updated_at]
        card_results.append(row)



# Your CSV input and output paths
csv_input_path = "/Users/shariquerahi/Desktop/Git/Python_Script/input_actor.csv"
csv_output_path = "/Users/shariquerahi/Desktop/Git/Python_Script/output_forex_AC211001JpyVnZEJRu2hC92R8cGBzQ==.csv"

data = pd.read_csv(csv_input_path, usecols=['actor_id'])
card_results = []

# Loop through actor IDs and retrieve information
count = 0
try:
    for actor_id in data['actor_id']:
        try:
            print("Attempting to get card creation request details for actor ID:", actor_id)
            db_info = getCardCreationRequest(actor_id)
            append_to_results(db_info, actor_id)
        except Exception as e:
            print("Exception when processing actor ID:", actor_id, e)
        time.sleep(4)
        count += 1
    print("Completed")
except Exception as e:
    print('Exception at count:', count, e)

# Write results to output CSV file
df = pd.DataFrame(card_results, columns=['actor_id','txn_id', 'txn_time', 'txn_time_user_tier','total_txn_amount','refund_status', 'refund_amount','forexChargeAmount', 'created_at','updated_at'])
df.to_csv(csv_output_path, index=False)

# Print completion message
print("Completed!")
