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
        'Cookie': '_csrf=h3-h1tAOa2bmd2aEWfNIceMR; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4NGRhYzJlOC0yMTE2LTRkZDMtOWNkOC1hNzZmZDA4Y2NiOWIiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODcyMzc5MjEsImV4cCI6MTY4NzI0MTUyMSwiaWF0IjoxNjg3MjM3OTIxLCJqdGkiOiIwY2E3ZjEyZS0xM2MxLTQ3NjQtYTA3NC1hNTFiYWMyOTBkZjQiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDQwNjMwNzgwNDMyNTgxMzI3ODAifQ.ElK399Jm8bTLGjms4mySTdkHY4F1QowrqqV2bJqel-iDYH9gvdUTnJcxWuOUENrKAS5HhfIqQZxL-St82vlrXmxTAZATbkgCNz3XUEXw8KGDO9EOJuyFyj_lldWdkirRi1i9R04JKWMEGtXGbDtRqjAyEW58mpGRV39rP7yuyOskQ9Ew0ZXw3Kv5NdM58lCxziHaSjoQUj5XD6VtWZt56rduPxnvau0SeiE7b980EdprWtZyUX3kpJcExi887GInidly6jITWOT6iq12EFKltCQqCmEVZVwsR9MLIu5OYL26_xzvEs74DDfUwhGzwX894UGW-jmNcTabis4p8QGrKQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiOFJIaFVMUjZMXzh5TE5CTllYdzdidyIsInN1YiI6Ijg0ZGFjMmU4LTIxMTYtNGRkMy05Y2Q4LWE3NmZkMDhjY2I5YiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNDA2MzA3ODA0MzI1ODEzMjc4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA0MDYzMDc4MDQzMjU4MTMyNzgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY1OTk1NDYyNzc2MiJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODcyMzc5MjEsIm5hbWUiOiJBc2h3aW4gS29uYWplIiwiZXhwIjoxNjg3MjQxNTIxLCJpYXQiOjE2ODcyMzc5MjEsImVtYWlsIjoiYXNod2luQGVwaWZpLmNvbSJ9.OXOn1eT0xJCeGxm926M1TEIhe5PlY8QIbGNyxPlKTBomebe8GR2JUsNZRD6IQX67jput7XHtqcTbBdSFWbXtqHsy4Cqv4qhHGUxjcMvH_ha9ft28XUWIU7V4Z2AhTKBGuT50tDZyvI_k1bYby8acoacC3-TtgvraI0e5fLSMXR5flFIW3z0Z2d7Pl_G3vajqu8N5AoePX4Ddu-dcKTF4H1yVyAq7WNUUeE08La1Rqrl7bfHG71VXYV8pxtcXYvX5LokPxCX4eROQoDqHyop00GFNKbMF2azQjwh2Fppp2eCVHNq54wQbeEh8hvLRjFEvyXFrmh_Bf1qFTp3N-d9mBg; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.tZrxuTEBNJQS0jnkBtmgE-oiwiuDY9BLjsCoErEdd4DlNJTZMYEs1nun55X9L_zogAUIeh-08wUpQ-Jk00Nqf8G5nUFDeBF09lyvmRc42Hlpe1e1WoF_owNyQzL2FrW1PKrmZY47JgYXYkukXrhLn6S9wcmiJszYqrO9d3GbmfIiNJgW_NPiTupbGsDNgDEcUPQKuu4n2ljLyBMKWLcKncib7X7SscsAjEsm1mJR6_8nIahdHMKpBwEjP07DV7aLYmna_uXGp8ryXHq4Vq8HxPi_7RfYQFritgmOsc8E2PT6vXSaWjuHpL1GIM_A3Dtbiei_l_grcYfG3CDlfnvaqQ.gdMk9wYrRmJL92Wb.JkuNMfN5cv8znErKlhyT6kSuY1WXi59Kb2VQFGJES3Dl695DF4MK6QGEW3ekRc-ERmU7oo4xCQ-TkASdE5PZpNy8G75v8a4dRS-U-xVXJF-nFhVcjQktlG3MC7DKayQW8Ll6iKPihrnDtnaPKEbKEbMfey5GxI5071JQ8x8xrLbf3VB2p2dCkOLFSiDBrcfPZfFMePAcyQ4tS2-Bj0x4c70WvonycfBwEpUPCgyRL-NzDJTUwXFbm5YdQD1JhPSso6UEh0Ucol2kNlj_JAkAWkiGquxvQ0NkGpKFAtMOaZqEDIK998SfNBDPl3TpNGGCqwoweF6F8iz10F2ihGPKt2-k8dJ-OqQgx5gv2mqdSOx_dCgPTZSAK4atxpeYiq0KRAP3eO8is0No_7q0ljPJQdsI9hUBVpj7-UQ0TecpUmcxUYwp23P5RZnAyA3fY7Q8F1FdlZFaBfL4wkyuw0GgBjq5ihD7LScwJCxrSeLdO2lLYOKkGf9OE1ZunYeyFdui6XJnnjAORG8lKG5UV6i_CwzDwEbNdGiUBnJ79yF2e10cNBuYqRWVj7rdEgo_PkxTIn89ufiFoXufNQosPBk0cZRpkSNuUsP3KK43eksxUMsD3DksjSpzqgE6uG4nago9r4KTnldk_n3i0JoDh3O8F-pMkT_J5pyFgzN_pPXqmx0vM37kpFxe0u3nmlnsFjsgXjrKPsMRlC_kNB648maObImDALNrnvEesaxPgFR0Iu1LWz01HVnVVQmbrsePuoMtstxcqxRTxC0s5lXUiX2_tP96ULHZ-tro78z2Xr-EJpDkIVbSM6EaWKzmGVsGmN9oLQaJWbaJuRrzwMIy7xF3eaEHaZOSJy_JMotjDeNlpcouWv0sl5E652uLgnH4XRAu_mHsHr5U7hYkS0XEQVRxkADuQl2JK9zuJGbAOhOVaV3qhNNpqpl_RWb6Y8XERPd9u0hwqRltgnnaV_mez_ov_bLW5RbtBA2zAHigoMg7a6vqd3JSzX7mJxGSbWXaqu_eCBg2ImFX5f3jptDLqxxkwk5S3jy3os5tzGzAQN3dzwYCHwJKtqMR9gArvdKZB2rNOIfdG3NqL87MZMBsXIBxVE_i4dtG2pU7M4nNMznD5msRxWG-dU8LgJmzk0Y4JwFLNCUhAMBuw1P1l8K0NqTGwBwU93y4_DkA2I29dEsY_P5z4oXD2RF6nRS-XVw7O4ebyDlkt1SxDB8CvhodqBrrobgvy9Jt1KHHRNzmUTEAn8JjQGf6kpDEMDbv4eVH96EKorgtisMDNAMt1JjXkA.cnZOv-09xBsHoA7r2T4_rA',
        'Host': 'sherlock.epifi.in',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'csrf-token': 'bDVQQoVe-DCB3WsAfj_OU3X3xV5VEaf5UKtQ',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Language': 'en',
    }

def getEntityId(actor_id):
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
        'service':  'ACTOR',
        'entity':   'USER_ENTITY',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    entity_id = ''
    try:
        dbInfo = r.json()["dbInfo"]
        # print('Entity Id --> '+dbInfo["Actor"].get("entity_id"))
        entity_id = dbInfo["Actor"].get("entity_id")
        return entity_id
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
    finally:
        return entity_id
    
def getToActorId(req_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'req_id',
                    'value': str(base64.urlsafe_b64encode(req_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'ORDER',
        'entity':   'ORDER_WITH_TXN',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        order = dbInfo["order"]
        toActorId = order.get("toActorId")
        # print('To Actor Id is --> '+toActorId)
        return toActorId
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

def getFromActorId(req_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'req_id',
                    'value': str(base64.urlsafe_b64encode(req_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'ORDER',
        'entity':   'ORDER_WITH_TXN',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        order = dbInfo["order"]
        fromActorId = order.get("fromActorId")
        return fromActorId
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
        
def getFromActorIdUsingOrderId(order_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'order_id',
                    'value': str(base64.urlsafe_b64encode(order_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'ORDER',
        'entity':   'ORDER_WITH_TXN',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        order = dbInfo["order"]
        fromActorId = order.get("fromActorId")
        # print('fromActorId --> '+fromActorId)
        return fromActorId
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

def getToActorIdUsingOrderId(order_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'order_id',
                    'value': str(base64.urlsafe_b64encode(order_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'ORDER',
        'entity':   'ORDER_WITH_TXN',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        order = dbInfo["order"]
        toActorId = order.get("toActorId")
        # print('fromActorId --> '+fromActorId)
        return toActorId
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

def getActualAccountNumber(actor_id):
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
        'service':  'PAYMENT_INSTRUMENT',
        'entity':   'PAYMENT_INSTRUMENT',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        i = 0
        dbInfo = r.json()["dbInfo"]
        for x in dbInfo:
            op = ''
            type = str(x.get("Type")) == 'BANK_ACCOUNT'
            # For PI block where "Type": "CREDIT_CARD" -> "Identifier": null and hence the null check before we fetch
            if (x.get("Identifier") != None):
                identifier = x.get("Identifier")
                if (len(identifier) != 0):
                    ac = identifier.get("account_type")
                    if ((str(ac) == 'SAVINGS') and type):
                        print('INSIDE FOR LOOP --> '+str(x))
                        print('Account number --> ',x.get("Identifier").get("actual_account_number"))
                        # print('============================')
                        op = str(x.get("Identifier").get("actual_account_number"))
                        return op
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

def getConstraintsDetails(primary_account_holder):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'primary_account_holder',
                    'value': str(base64.urlsafe_b64encode(primary_account_holder.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'SAVINGS',
        'entity':   'SAVINGS_ACCOUNT',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    try:
        dbInfo = r.json()["dbInfo"]
        constraints = dbInfo["constraints"]
        acc_id = dbInfo["id"]
        # print('Constraints details --> ',constraints)
        # print('acc_id --> ',acc_id)
        # print('===========')
        if constraints != None:
            return str(constraints), acc_id
        else:
            return 'NA', acc_id
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
    
def getReconDetails(account_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'account_id',
                    'value': str(base64.urlsafe_b64encode(account_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    params  = {
        'service':  'ORDER',
        'entity':   'SAVING_LEDGER_RECON',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, params=params, timeout=100)
    print('r =>',str(r))
    status, lastReconciledAt = 'NA','NA'
    try:
        if (str(r) == '<Response [500]>') :
            print('fdfgfdfgfrf34')
            status = 'NA'
            lastReconciledAt = 'NA'
        elif (r.json()["dbInfo"] != None) :
            dbInfo = r.json()["dbInfo"]
            status = dbInfo.get("status")
            lastReconciledAt = dbInfo.get("lastReconciledAt")
        else :
            print('hdfjhsdfjhbjfhd')
            status = 'NA'
            lastReconciledAt = 'NA'
        return status, str(lastReconciledAt)
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
    finally :
        return status, str(lastReconciledAt)


order_results = []

def append_to_order_results(req_id,actor_id,entity_id,acc_num,constraint_details,acc_id,sync_status,lastReconciledAt):
    row = []
    row.append(req_id)
    row.append(actor_id)
    row.append(entity_id)
    row.append(acc_num)
    row.append(constraint_details)
    row.append(acc_id)
    row.append(sync_status)
    row.append(lastReconciledAt)
    order_results.append(row)

csv_name = "/Users/ashwinkonaje/Downloads/AccountFrozenScript/get_entity_id_from_actor_id.csv"
data = pd.read_csv(csv_name, usecols=['REQ_ID'])

count = 0
i = 0
try:
    for i in range(len(data.REQ_ID)):
        # req_id,actor_id,entity_id,acc_num,constraint_details = ''
        try:
            print('===============================================')
            print("Attempting to get to actor id for row", i)
            req_id = data.REQ_ID[i]
            # FromActorId is not reqyured for add funds collect wf
            actor_id = getFromActorId(req_id)
            # actor_id = getToActorId(req_id)
            # print('actor_id ::: ',actor_id)
            time.sleep(2)
            # actor_id = getFromActorIdUsingOrderId(req_id)
            # print('!!!  getFromActorIdUsingOrderId -->',actor_id)
            entity_id = getEntityId(actor_id)
            print('entity_id ::: ',entity_id)
            time.sleep(2)
            if(len(entity_id) == 0):
                print('entity_id is 0 ')
                actor_id = getToActorId(req_id)
                print('getToActorId ::: ',actor_id)
                # actor_id = getToActorIdUsingOrderId(req_id)
                # print('!!!  getToActorIdUsingOrderId -->',actor_id)
                time.sleep(1)
                entity_id = getEntityId(actor_id)
                time.sleep(1)
            acc_num = getActualAccountNumber(actor_id)
            print('acc_num ::: ',acc_num)
            time.sleep(2)
            constraint_details,acc_id = getConstraintsDetails(entity_id)
            print('constraint_details ::: ',str(constraint_details))
            print('acc_id ::: ',acc_id)
            time.sleep(2)
            sync_status,lastReconciledAt = getReconDetails(acc_id)
            print('sync_status ::: ',sync_status)
            print('lastReconciledAt ::: ',lastReconciledAt)
            time.sleep(2)
            append_to_order_results(req_id,actor_id,entity_id,acc_num,constraint_details,acc_id,sync_status,lastReconciledAt)
        except Exception as e:
            print("Exception when processing request --> ", req_id, e)
        count+=1
        time.sleep(2)

except Exception as e:
    print('exception at count: row : e', count, i, e)

df = pd.DataFrame(order_results, columns=['REQ_ID', 'ACTOR_ID', 'ENTITY_ID', 'ACCOUNT_NUM', 'CONSTRAINT_DETAILS','ACC_ID','SYNC_STATUS','LAST_RECON_AT'])
df.to_csv('/Users/ashwinkonaje/Downloads/AccountFrozenScript/get_entity_id_from_actor_id_OP.csv')