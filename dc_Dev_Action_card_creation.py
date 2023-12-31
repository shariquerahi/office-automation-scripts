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
		'Cookie': '_csrf=kHlfPOnhqdhYAqX1Z4rKu_Zo; auth_version=v2;',
        'Host': 'sherlock.epifi.in',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'csrf-token': 'q8jRMf1c-VXfKpUCkmCoQjA_1qrxiwFR6E8g',
	  	'Connection': 'keep-alive',
	  	'Content-Type': 'application/json',
	  	'Accept': '*/*',
	  	'Accept-Language': 'en',
	}

def FORCE_CARD_CREATION_ENQUIRY(card_id,reason):
	url = "https://sherlock.epifi.in/api/v1/dev-actions/execute"
	body = {
				'monorailId': '1',
				'parameters':
						[
							{
								'name':	'card_id',
								'value': str(card_id),
								'type': 1,
							},
							{
								'name':	'reason',
								'value': str(reason),
								'type': 100,
							},
						],
				'action': 'FORCE_CARD_CREATION_ENQUIRY'
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
data = pd.read_csv(csv_name, usecols=['card_id', 'REASON'])

count = 0
i = 0
dateSuffix = 'T00:00:00.000Z'
try:
    for i in range(len(data.card_id)):
        try:
            # print("Attempting to force create VPA for row", i)
            card_id,reason = data.card_id[i], data.REASON[i]
            print('card_id :::: ',card_id)
            print('reason :::: ',reason)
            print("Attempting to trigger force recon for account id --> ", card_id)
            FORCE_CARD_CREATION_ENQUIRY(card_id,reason)
            print('-----------------------')
        except Exception as e:
            print("Exception when force creating VPA for actor id --> ", card_id, e)
        count+=1
        time.sleep(5)

except Exception as e:
    print('exception at count: row : e', count, i, e)
