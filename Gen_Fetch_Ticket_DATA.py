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
    'cookie': '_csrf=JoyDhRGIWlX_sqFGAZym7OIP; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODk3Nzg2ODAsImV4cCI6MTY4OTc4MjI4MCwiaWF0IjoxNjg5Nzc4NjgwLCJqdGkiOiIyZTQ2OTUxZi03ZGI5LTQ1ZTktYWMyOC1mNGJiYmQzMzZlYTUiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.l3f7Nt0GkTZ68CvTkVWJqdaj4CoxyL55RjGKPHqlxgaQh5MqPAUkumSa_UJYRg3MVGDAl4U-3iTg2GSBmq6w_K6k39WUBy24xFXA9L236w_1OYZYH_ynLeupEJCP0quqVYRDmO0d4pkPcqj4SJeA9GiBDOdDygxfrKH3zrsrcfsi7QRfs65RRc3c7EQNdwOR_9bry7hx7Q26kgLBSODmSasdgy1GubUqwVVMW8pFNkIhZfx6NxMpsCJgAS1DwkEGvTJFuXoSHC2v50XfOcKqDBtGGd21RkE5KfMsvVbb8V-isf1mk5DDnsaPBOVxyDi6qbfVTZwzqkuv1_f1jj2fQA; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiMkl4a1dDZVRzeXdudVhpQ0xYYl9JUSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoiSkltYTc1OWY4YzdpSkw3aWpXTzBoazlyOElraElQRDc0WWw2LWpOa0sydnlkMlFrNUVjMHE1WWxmZEk0WXhIX0IxMzJkNFVHUHc4X0tiYW9lU3hlVWlwU2xtLXMzRG8wWGg5R29HeVViVUtOTEUxWnNNQklJQkllSjM5aUx0bmZqQXl0eVR3NjJvY3E1QlFNOFlPYWxxWUFyVlRQd3dRWUNuS0N1TW1iT2R3IiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4OTc3ODY4MCwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2ODk3ODIyODAsImlhdCI6MTY4OTc3ODY4MCwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.peTNSChiQaS6bKVDbOY-hq5InGBlnkiH3nkI-VBVgWlk1TZvdHrtj05iPbDoiiVTiUuURf_lyiM_YsHhbkQolMkgHToAXe3QGmkyFSEOZDLAxhvGtPnL4wCbUDrcXzw9PaAo6l84JwFb4UQUjjhSKTQlywDt5RQwORueZJHbGgjpnSPEDuUu898Q_NshaFOL9X-W04_yMY7oYAB3Bz_d_HSDPbhaXnHKXKIO2HUUPen5fWGoT3DawbxDtneVB_pGLD3xwjVn6p87x2jNMF1WuyyffKbmzj_dkaG1gA1rMxa2VWIL6PnBzaKnL6siCpPVBndhWtSMLkOBv1THFure5g; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.RFBAmjxxqqeVJD-nNbtt3AqKuAZYgYjsgt0pSeqeMjFObQxphvwLyWx3EDB0lEt05ht6BYHEna1tWwDa4dXhchjiXI2Jp4-wT-YG3qui1qdPcFRlcyOxuSEcp8ro8JN5lpNhOC5zXB8MFNFsuQFGjypW4qwwJ9JUuXglZ9ftSjY_XVuxJpMX-qrD5xNEHtkB-YNGS7ZmLIojbbhq5fltxqKwsHsDqGBdsRhIDWe8E9Dhbyb4WdWpg19-YW5HO6_OItH8Zt5aX2YC3ZkiVQnTpd_ZXaOaNlkYonVDZJL2FzLfKFWXxNSO9Fgzr0CdF-CAIUQbU26LNPHhSuEGhgcTAw.MrGSdoxKXG6ICMPf.7y4Avy8PexpHQKb36g5PgGDDnIVf7nrB1QMV14XsV7WYmm4b07z4Mpu6ZJy9D5MRCYdviCTROyCjK-eEkVuqJG5JirtmM_NVzp0vRiDdU6h3iOcSwItVSXFxxeexvRMWlTm7TJRaiczaeHjGQHyDihJ_aGmPtnSKPQf7L5ToejPMikIqTxdgxjM5xIhf66RECSlsfIvNkKxQHZICY8LpRhCPFzdRdbGdAzX32ipnxqJHScjOJxiMfKvsnp1vxp6HWku8w3Z97oP8UKLNQ4ir7tkSOTz1NmWKjIETynuRPvaPaUMg1qKtrAoky1S941xLB59yYBI6dobr0egrHtLzFyKutvDgb4ylfakPHZ8HB8Nx7FOJQ_Yvrzk_s144mvy4iXhcUkjjWlkkcDzzxTuD86S4L48mrsBPvURA2jPXA5LhOf-T5J1SDzMcF2dZ0qKvZslz4erbqtkUZKBP_ARpRtm8zk3nDGtlGpTOGDtSdU0wOFha4NQ44eBhpNGHYls4Hth-Jhbfj5UCBsRM-otfBKahqzRFSLOqjiyOU5XuIP6yI79uFztzo20jYjJ-Y9b-OC-P0fJOTWSyGy0xiRSkDum-0j39HzdB9w2M5WaxwkL3V-ItOpihcjGN5FXfdOEC0GJ8k9cWH5dhKcBK1ufSJ_cCxHcr7Mve-SJkScaTlajhRqsRjuelN9GDU-YNpZvZkT_qsb8mDmdRM-CqsY5wSTakapgHaKWYc-_L3uHBHBxvvDO-8jFAjT4rfHYP3N26V14cK_kBmyfguCIH914qlxdVDKet86y1OkGuP1-6RmEa0BzGA-Mddp4KbIU0a6DoOhsRiLzt_vyn4p-6k0dJPOr5LXtkxZeAD8amaTX_O2D_9SWocQx_-8aBlHg0XVfDEYLYIboyL1CgTsiFSOKOiTc_y1pROFma20-Qri6UeB1eHSIjg_smZZLU2ZKWv3zL4Cpx8QtbAdKkw-8WLEP2IvYOwl-M2w7GAw6YnZJqKFOEmknBxfv9UsUsG_SGy0H0jHPGTDdvI7e9dsv_G4T0a8oqUJxRhsTIlAI2MPUSSr0zb1uChtfIzEAoHg19fJLHigZf6ogLQ5G97hbhX1rUAnl7zXuXFTUkr5MNgDBe5-R9RqpqptlTnMc6VwGvbbqU0g0Dx2PvrWOLHxqA9zhG8NwlQ16t-SRoW8u8emvKx81MfOrsB_PvV8UWiV9ETsuOtZYgYJwAmr59WrTmStyEWwIDLW9bPJbjtr1Uz-ogHICtkIblYjaYiUdnAEz9xlvV5jc_6SJHK5tF9X2ihA.Zdr42zod6pytuDQ6A3GlbA',
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