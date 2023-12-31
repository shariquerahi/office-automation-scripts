import requests
from pprint import pprint
from collections import defaultdict
import sys
import locale
import json
import base64
import time
import pandas as pd

headers = {
		'Cookie': '_csrf=kHlfPOnhqdhYAqX1Z4rKu_Zo; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.Pd_p105NxExoyt-QnRkSU_-BNGSUtEUMW-DlO-iCWCtiTAlq0Eu8W3I_WAXYCa916vAE4ID3ViXvmkCBqoBiKwjGWq9o2UD-q4UabVsxqtVr-5AJ3bTuObOLSqQRoIQ-96TDfGkk-EvEd7ppnf4HuOZtfBSCYYeDA5OAAaqwq3bsEz8vuwWrOiaqoAC0nQnpXobR9KnQ3fgkxKp_0FJzVOLaqtARO20qBuyQk0Qx30VA9KW_mqU2y24j3T59cY_pCqpfvJeT0K84hJTinFfoYBR9BfJwylBW03bfT2Wkp8_lFN4jzwLq5n_yzNwu7uPfYMUlT-GA9Q_VdSg7vddn2g.Xg6OZim2otuFsh11.-Y8xYq-UQm87jG8uVydHes5DdXZ6k3w47B9jzZGppP_iAefYxqNk8axy9UvPyXNjIxcAfpeT2jYUA3NG8ysWb2zF24RiB28TZT0jMgWFFMRYl6CSenil0quk11BLgKS1-GVdRb86xc10mSypTesAkH9MDkJmaHLBsm2w4QOrPhWSkmApkrmkoWWyRFh9emWP2tE82VQXxtN4SHZcRGseyecsbotkfz2cqERHTuxxYpg_1bmTHeRsSCZp45wWEtD4_-RKa2qCrMYhsdZG-3Hkp3AqsuFEZyDGi7_XlP9DDgFYoEInkHnEcZsBPsQDWs6M5yhprVmYrJuySx1vk-OaYtivFXuWDwjWOH9_Zc5eypZxPj78aa40ODtFy8H98lCTbo-x9f-Qxa0c3G_hipuF0nMG7axroKhEMGGdzYaZD7WuJV3iRI2r045Cb50PB-hDztzrasqEOUbGOedlz4vDcjdzaBaI0M7IjOOOI1ChtNlgQiAUqPlyRSpTVy8IfZ08otsAObVGVx5wzfb_9j3tE4ceXcBLILoOSK3MfYB0F6bx3IKVLTvtxEiEh0gVT2-PzvnDe55M5Ff-j3onzx24WaWqb6knDJE5UXxF_V8F7EpamoD1VKi697dovxZ48FS70jkIlFDK_ffJdL0HnS8XN58hfTpiuk9XSifANE9I91Q3J_WapLR_hM0mw9WoBwHuYH0fwaEVahINh1EbCA2PEBccifAuC-Y0dju0Gg57hlEWr4nmcuF_-wT2guXeNcz-HN0yFcVZqs64LHJ4pBzQOelSxTyUgMoIjENykUIq3HzUX8AvAgk8W_9mwjnta3JI_pPpx098l0GfiOKEiM_LdpyQ9jHvqajj7XCQt9ue7P30nEiiLvWVhiCz4D1Xwy-Tnqd6xR_ZM2BTzfe4lICRSCcZ6oHg_PIAx87bONCW7dQUAAL2thnTHMNHv1ZuGRTw1PL7dOOwFYBWTS-NwQ_iipa8mjRbdyXUzl-BPVmSKW5LGzatgtArEpgjoyNzySPjsUHWNyt8guYkziU4xsZjGM_vu7Xx7igysg_m_XMxZHRlxFIuUl5DFWSpep9gQM1pZN1QI1bkgDA3_DntAfO7kb5VBplbEkGdrrWjPY-W8u9_p-aWIvwjjIvEK9XyRWlc6PK0H_5v5fTijJkVGt26xBqxWZXzrWjK5IC2KqI78xFMeIVE910obumkWJVdNc_r8ytLQea6O71uxHD9Ug5pFaZaKySmNzt1bheXiF6PjM4NJIP1HLxv4Oy6Js7f1gAskhsUeRKG7dzKapYDiQ.hW9ysTet10sa_3EmCADcEw; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4NGRhYzJlOC0yMTE2LTRkZDMtOWNkOC1hNzZmZDA4Y2NiOWIiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODkwNTM0MzQsImV4cCI6MTY4OTE0MTE4OSwiaWF0IjoxNjg5MTM3NTg5LCJqdGkiOiIyOTBiMTYyMi1mYjRkLTRhMTUtYjg0Yy1hOTYxOTU2MDcxYTAiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDQwNjMwNzgwNDMyNTgxMzI3ODAifQ.YzIHIIUZ3-g_9hlQ9axnja5sXcCUn-9KdtMi7zl_wzcXUusBxZOWUofwiTmJEiA2_FPvwqyQrl23VllnjgsCvWfg6NfuqZ3NvoXHYWipF5Lnu1CuX-MpceCX6SME34d9ezbmYcKVbAjjEFOHrx6XVOLgrL2kFZp4AeFjBuInoygFA_kM17k_R_XhzklOiXMYBKNKjq9qSljgFKiSmRDY1OS6pmaMsTfTtpfjSDNq5FlDEeuL1ELgmii7u-NPPqka_Hjh91lruRwKPKnAtbCcOMgzw2OaHpPg43kaOGl00tTv9KVnSP1asBb2Lba6bUHIl0lRMbjGPgl8ZFSCzpjVGg; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiUDd2NTVWUGlZUVFiTHFLQjJGbGhHZyIsInN1YiI6Ijg0ZGFjMmU4LTIxMTYtNGRkMy05Y2Q4LWE3NmZkMDhjY2I5YiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNDA2MzA3ODA0MzI1ODEzMjc4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA0MDYzMDc4MDQzMjU4MTMyNzgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY1OTk1NDYyNzc2MiJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODkwNTM0MzQsIm5hbWUiOiJBc2h3aW4gS29uYWplIiwiZXhwIjoxNjg5MTQxMTg5LCJpYXQiOjE2ODkxMzc1ODksImVtYWlsIjoiYXNod2luQGVwaWZpLmNvbSJ9.J90cXYQzAcgjG-VH3bgXaXQk9rxkfb19Qp4LlxbKbMlCdEaOjdpSQRRAwa1nxuwSXRa4LlC2VsV48MHSbqBdy_LEBBQIO3kiop2z0IqoQrJ3MXMBr7SXsWJaLw4qDFQ_jRNhRWfKLlHf4B_gZROx7dKp7HkAWBnEEe6DcMAz26TGbhwpFXdMgir1dICz4nUUZZLFL_JvimtKq4pctRI0YDG5P6dffBqqIzc3lWV0OBdG5UW4vtVe2BLgrwm3jVDCaRz8KuOPBbcIDGYvXst7b5HT3nZoKvPWX0sUlyZ4RGwTMjQLb64T0891gdNIz9Qfst2norZg9d-HHBxq8U3nNw',
        'Host': 'sherlock.epifi.in',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'csrf-token': 'q8jRMf1c-VXfKpUCkmCoQjA_1qrxiwFR6E8g',
	  	'Connection': 'keep-alive',
	  	'Content-Type': 'application/json',
	  	'Accept': '*/*',
	  	'Accept-Language': 'en',
	}

def force_trigger_recon(savings_account_id,recon_start_ts,reason):
	url = "https://sherlock.epifi.in/api/v1/dev-actions/execute"
	body = {
				'monorailId': '16066',
				'parameters':
						[
							{
								'name':	'savings-account-id',
								'value': str(savings_account_id),
								'type': 1,
							},
							{
								'name':	'recon-start-ts',
								'value': recon_start_ts,
								'type': 4,
							},
							{
								'name':	'reason',
								'value': str(reason),
								'type': 100,
							},
						],
				'action': 'FORCE_TRIGGER_RECON'
			}
	r = requests.post(url, headers=headers, json=body, timeout=40)
	print('r ::::: ',r)
	try:
		if r.status_code == 200:
			print('status ::::',r.json()["executeInfo"]["savingsLedgerRecon"]["status"]) 
			return "Script:Unknown"
	except Exception as e:
		raise Exception('force process order api call failed', r.status_code, r.text, e)

csv_name = "/Users/ashwinkonaje/Downloads/Scripts/DevActions/ForceTriggerRecon/input.csv"
data = pd.read_csv(csv_name, usecols=['ACCOUNT_ID', 'RECON_FROM', 'REASON'])

count = 0
i = 0
dateSuffix = 'T00:00:00.000Z'
try:
    for i in range(len(data.ACCOUNT_ID)):
        try:
            # print("Attempting to force create VPA for row", i)
            savings_account_id,recon_start_ts,reason = data.ACCOUNT_ID[i],data.RECON_FROM[i]+dateSuffix, data.REASON[i]
            print('savings_account_id :::: ',savings_account_id)
            print('recon_start_ts :::: ',recon_start_ts)
            print('reason :::: ',reason)
            print("Attempting to trigger force recon for account id --> ", savings_account_id)
            force_trigger_recon(savings_account_id,recon_start_ts,reason)
            print('-----------------------')
        except Exception as e:
            print("Exception when force creating VPA for actor id --> ", savings_account_id, e)
        count+=1
        time.sleep(5)

except Exception as e:
    print('exception at count: row : e', count, i, e)
