import requests
from pprint import pprint
from collections import defaultdict
import sys
import locale
import json
import base64
import time
import pandas as pd
cookies = {
}
headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '',
    'csrf-token': 'VDaRWccx-saqZrtzFeP7bOasoANvewEyrdlo',
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
def getTicketDetails(ticketid):
    url = f'https://sherlock.epifi.in/api/v1/ticket-summary/{ticketid}'
    r = requests.get(url, headers=headers,cookies=cookies)
    try:
       time.sleep(3)
       ticketInfo=r.json()["ticketInfo"]
       return ticketInfo.get("actorId"),ticketInfo.get("status")
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
ticket_results = []
def append_to_deposit_results(ticket,ActorId,status):
    row = []
    row.append(ticket)
    row.append(ActorId)
    row.append(status)
    ticket_results.append(row)
csv_name = "/Users/shariquerahi/Downloads/ticketid.csv"
data = pd.read_csv(csv_name, usecols=['TICKET'])
count = 0
i = 0
try:
    for i in range(len(data.TICKET)):
        try:
            ticket = data.TICKET[i]
            print("Attempting to get ticket-info for ticket",ticket," for row",i)
            ActorId,status=getTicketDetails(ticket)
            time.sleep(1)
            append_to_deposit_results(ticket,ActorId,status)
        except Exception as e:
            print("Exception while geting ticket-info for ticket --> ", ticket,e)
            append_to_deposit_results(ticket,'','Exception')
        time.sleep(2)
    print("completed")
except Exception as e:
    print('exception at count: row : ', i, e)
df = pd.DataFrame(ticket_results, columns=['ticket','ActorId','status'])
df.to_csv('/Users/shariquerahi/Downloads/output_ticket.csv')
