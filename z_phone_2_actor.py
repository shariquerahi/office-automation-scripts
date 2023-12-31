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
        'cookies':'_csrf=gZo5m4G9uOuyaQZVDG_2ky-A; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODY2Mzk0NzUsImV4cCI6MTY4NjY0MzA3NSwiaWF0IjoxNjg2NjM5NDc1LCJqdGkiOiI5NjVjMDRhMy00MzI3LTQ4NzItODlmNi0zNmUyMGY5M2FhZmEiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.cICJ2Codft5YmLrjhZNNq4rOCO49AgJTVgjYGv39IaN9ANF5H_56Lf_BL_QY5EplZCkqHimw5753rci6tavbh0pJwE_W3EFhLtqhnK2P21Z_FxeHVzTMton428zwcJaZqMn4m-UwFvI8F8W530H9Vv3KYAbK-y7yzEeih5Gp5lRdvawJ8fJwQLYw-AKtL_Qw9jL4XNjQ45kMCML2pApCjBzYIvn9NFVoSoiYNccAmK_NDwnJIIuiRhZAaJ7y6nK34YySSDyX93znyDtmAtoiC2zsOusnG2FZ1cg4U9mlyr7uOyOt6ucBgX789DsXuBIgW52Bk8AFqa9MtvUqRhOQDQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoib2Ztc0MyX2hvamVpSHhGeGUwcUUxQSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsIm5vbmNlIjoidjlZQjNvdlp4VWhfazBlTTZUdEZ3UkdQSzMxNmx3ekxuUHJlV3BVd3JNVnVhT3J6a2xZTy1YcG1OTXBsWXNsTlBDNjNUS0RTNjR0cWZWbHN4M0N5R3NzOUotRVJyak0tYjVkN3dwZVFvR3did0hTVlAwTXMxNHI1Z29DWW9kdGtRVFA3OE4zWjNNb2FPRWVpbEZDckdhVGMxemlHeHh5TmtJY0V5NHBlNVFnIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc3NTAzNjg5NjU1OTk5ODUyODAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjgzMTkwMDE0OTc3In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4NjYzOTQ3NSwibmFtZSI6IlNoYXJpcXVlIFJhaGkiLCJleHAiOjE2ODY2NDMwNzUsImlhdCI6MTY4NjYzOTQ3NSwiZW1haWwiOiJzaGFyaXF1ZUBlcGlmaS5jb20ifQ.KINbRRYgfP8V8l7U2zUFobp8LmE-2jdSwyE_jVq_BVFEbUN29BtOPbefXvqHe_JTuGQ1JtYNeJJWhWdF8gjHmDKnsmvMYwORUGvjMD_lz3XEwLOri2SEnJQg4UCfLDUMJmWd3YTXvBGrcgpuoeX14Gb0TV6s4Q5emg9JWP28klXW1Hscerr0FnFEo4d5BTUxF54GLfYTb2PcFQ2Xj9arOriYQ_lwUGJU3kmmeIEToN4MvFM3trHs1c5tY85cw8GvipCwI1_x6ombw8YMoQuTbHlfEMwP3Cdi0fW84-xEV0P6ybpIioxAXgfQWAWLwUmIaaB04YufUGKP6e6GcpB9sQ; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.Yy_qvqX8a7PUafQ6r1mff53E4B0Duf0GH8NnN2edBuxmHaLKD54C9HtSS-rerT9cSpucSO5TPNaxOhmtpUc1FRLXrRcR1aABTdYtvw6XoDE8Gav1gdf1j94yFaMaSc2cqHQaidVomXpB-ET8o9dqFRN1w7IhA-V-Svm6zDHsDMHR-NNmpR7Askd9ix7GoHTcJamkVC14zCfsTyKnSA2QpySAGdV4LCUIpEypIvr-eDCvdU1gn2dkhw5T3l391uN4M7putMfkJXkWmTL6T7X0D1hTYcyL3bTDtrq_8S5Itclv4W34lHWNPEPnRVz5zplierN8Jf7GuzCmjFDxd5FXUQ.vSdH8tr37Bwhwkue.qBdyKCI6NV6G8RFUsOo9c9_yFwO-_VFSq224LcHy13ORpMq-fw2BcWKHj0jVRIo6adbXC3u1yQjas_97oJPOJzwELh2YJRvs2zE2I-yMWW6YCRsri5Kz1c0I31PhkoiRHgaOHDnNcK7DdPEFETwFtIKKQ_OtXNoq6A9aGDJ13qtWpIBwrWN9rNWabFAmJyq6vjPWAfdmzTadjuMi2TQp_BqDB-lqI_5mJzEpLsZGyc061kpiCWtfy3MEtUMEXMu_rXHCjmNRTeBBkNjVIhyvXEIKPi_0RFNLsTkIHLHuV2uMFn2fJhfgKE4uaTzHNFoBI7GMfUQgjavKrS5AmfwncFcd9UyQhtabS0Mn38_iAr6dL2GV6GYI96Cwk3vbE2w_tkrmNOr3FlliqcfyPlOGSj7uCbpde-4ezPmWNZLgVUoPa6dQTHO76P5Cst556QVMPwa5CSNHE5bYpROjY5Xq53_kbuKaTOZTXIBmyO7BSWArlON31dP9Mr1QDN_qcqCNeIbq__wBYq_0ZR1XxNdFxcN6iPs7CjgtPDVBSRJk3zuDqaJaK3yGxlnt9FT2wa7MCrOC-wz1VYsgLe_e4Q4kJncqdBlpgaeTV554TTM0fEXNhlzhh6lubmev4r17kxeh0ok4DwlPzplbbq_8sbLcytQflDPVJEuFhkMJe0e0YV_OrzcshRzYJ1RFZDXnKQ1v6tqxgitKaKRvepvzNWaKUR5jjHeoEgeQ-EmD_wLcYBQPanGhXUO_CuvFU8pmhHLK9zQpS1J_QrpmIiPRH0A6yCjIVzT9qie46gcC1dsqaW6056X7W353oOyJGb1FhUfRYt0FslEE-i7nxcwJw15COLWx8G4fMe-lWOKVMGwXT_0h2BbwDgFL1YhiIxPm8iUZrq_IZqnhbLSCaE4AQTKhgr58Ixq-df7nY4phufAPITk8U6eMAs0rxYCl3wJpeGNqe1oXuQq2dXrbFp95t3K1eVMmmoYui_OyExelqnnC3Q9cavKR_2D1ZJIY7KWj9GiEuRx3ofRGUAEWkkzPD7FJVBn4OBs18Z05woWBUTvhngBmxa_sM823Hqe8Zibh1p0IHrGIUs6bVmEynEN3jZeDyaokj3hlfU-krOVhz2gLQqYsq01o9TdzAJVdtCk2Tokd_dXPRnFHDwDJQqSjBavx3NUS_AGOT7lmUFteg1ec0vP0_3KTkNUsr9oHT2OSpB-nxjDQRYnxddE59JudO75g1vdyOGVBwdk_Ax4bvyLb1tkH2LnZsnYIJNTQ82xCJNbIdfID5yLtDbpmYMtzTg.Wf8onxzU_XuacNGG5DfBxg',
        'Host': 'sherlock.epifi.in',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'csrf-token': 'EgE3U07a-q20LlWTPKUpFRldXv6c9bxoazbQ',
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

def getPhonenumberFromActor(actor_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'actor_id',
                    'value': str(base64.urlsafe_b64encode(actor_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'USER',
        'entity':   'USER',
        'options':  json_dump,
        'monorailId':'1',
    }
    r = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=100)
    print("executing kyc &phnumber")
    try:
        dbInfo = r.json()["dbInfo"]
        #print("GETTING NUMBER")
        custid= str(dbInfo.get("user").get("customerInfos")[0].get("id"))
        #kyclevel = str(dbInfo.get("user").get("customerInfos")[0].get("kycLevel"))
        return custid
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
def getActorFromPhnumber(phno):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'phone_number',
                    'value': str(base64.urlsafe_b64encode(phno.encode("utf-8")), "utf-8"),
                    'type': 8,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'ACTOR',
        'entity':   'USER_ENTITY',
        'options':  json_dump,
        'monorailId':'1',
    }
    r = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=100)
    print("executing kyc &phnumber")
    try:
        dbInfo = r.json()["dbInfo"]
        #print("GETTING NUMBER")
        Actorid= str(dbInfo.get("Actor").get("id"))
        #kyclevel = str(dbInfo.get("user").get("customerInfos")[0].get("kycLevel"))
        return Actorid
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
deposit_results = []
def append_to_deposit_results(MfOrderId,actorid,phno):
    row = []
    #CreatedAt=int(datetime.fromtimestamp(CreatedAt))
    row.append(MfOrderId)
    row.append(actorid)
    row.append(phno)
csv_name = "/Users/shariquerahi/Downloads/Phone_number - Sheet1.csv"
data = pd.read_csv(csv_name, usecols=['orderid'])
count = 0
i = 0
try:
    for i in range(len(data.orderid)):
        try:
            print("Attempting to get deposit details for row", i)
            MfOrderId = data.orderid[i]
            actorid=getActorFromPhnumber(MfOrderId)
            time.sleep(1)
            print(actorid)
            custid=getPhonenumberFromActor(actorid)
            time.sleep(1)
            print(custid)
           # time.sleep(1)
            append_to_deposit_results(actorid,custid,MfOrderId)
        except Exception as e:
            print("Exception when processing request --> ", MfOrderId, e)
            #append_to_deposit_results(id,)
        count+=1
except Exception as e:
    print('exception at count: row : e', count, i, e)
#print('TWO')
df = pd.DataFrame(deposit_results, columns=['actorid','custid','phone number'])
df.to_csv('/Users/shariquerahi/Desktop/Git/Sharique-Git_Repo/output.csv')











    
    