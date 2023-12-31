import json
import base64
import requests
import csv
import time
import re


url = "https://sherlock.epifi.in/api/v1/db-states/info"
devActionUrl = "https://sherlock.epifi.in/api/v1/dev-actions/execute"

# with open('cookie.txt') as f:
#     cookie = str(f.readlines())
#     print(cookie)

headers = {
    'cookie':'_csrf=NJJbDBnbwsQ57k2ESmyGrVdc; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.SKkZ-Ec-EurkoeqDwOujHH7hCYhriDYhc88XiHFoxIPvr1ag8MyaQGB_bqDIqr7EvubnEeOjOjz0SR1iyNKkq96gCiJ4MaskMDQ4MRV9Otw7Yvb6G21QgFarqYUelrHmorsChm1tOlLDXoP-LdjxZdtExIwcUGFKQ1ZY5u9RpWytkJbyNl2929c9gFymsCi7Z7C_7u--d_-LrVz3lc3XcBXadV6dUtI79ySEvmWaDFKgkUEWz6kzJnNsGbZnmJUJi-dw8NNPJqhXiv05sShOfD_8JEMaKD477JBo0DC82YkDC-tVYvZcrekr7ukOlRp1NJUIpuFpWBfwpYIQMpWq7w.Q2B7_BfMgYLRAkha.E9La5Kqgi7D-yK6vELytVxgF509FMBhBtSCC42DECUBD0ZnuVtDI3FZnXaTuthOPhYdcJo9qOL2bDkOrqPRdMqvdPnhhsUF8ePBpGGvcerOWLqUbPfsA00ON7JIRj7rkX1G6hxWSHT9UJaqAwFWzl9XhId_Aig8z6DfcVEXsoqWZ7cCJ5hbWEutBOziNpPTCYMHkcrswbDI-ZOT79SNM8R0Ix6e2q9l35uY8dU-62WEdEAZqhPWb2IQtgrlfhGyH3Gbe1rsTmJcLC5n_MRLsd9YzAKKsD2ok1uxoE-AhnAs7P6EkBrvX_22iir6zPMPpMvtaXf4h2TmeRi-T5qzLM5yfE8Tpnx8umhHdmvElBbOmVL7hsjgnH0VvgsoWyOiyJyBsr4v4UHoraxOfV5-hOteuxrjCqJki_VuugLPJTZhncLFJpKkNNqmKNZxr0E3Weh75Y_A2YT6ZNNTDeZmPrbW2dARMgxDgJOiYges4VYWkIJjXxtw7PgLjDwq7F3e8xPlSISBX3dgReA4u1i-aPN-AObxZeCPTIo4dBtPFrg97UvqazsNzwxCPdxw__RQxBxVhpJQwYxjX-yCpUKqYXCLB4UnO4qhSTCpxGOBGBhh0YXlA15nCFCcBr1Y5Av-m5WKYhvifD7dUrzAdQZlrDz9JejVVP5gCsZ_XEe4ngcQKh3DUnF_7qm0iC8G_4vu9hFq_zjONtfexWukIx_K7MVLumw3dIf5MjdQfFGBULZvvO1hiPmaPs2EdWufPODZiwFpP3aKVEPSdiYNQsN565QAdDY6UBXHWoi4kh5QLtBi-UAyHsIAg2iEMr977xu8rlrmEczLIeZV2p-YJRw0a1BZ67wdTNXI7L6sCfmpPgHHL7ZN8WF7NGDIO3Iz7HmaraEddzCScPWp4khL8fRtSmXmQNW_7sIrnp5NoWlWfc8MvPcalOlfco5-2ToKipPK4TltSBj_UjzJDp7zkJ-Hrf7RLfJ1TPE8wiagFu7ZlkeOl6802JyPS_vbJeltCma1ylV_Waos4fq4HRfkvbCkxDKM0Pt_iMEEfEAgFLUpi74mlCVJLvKWnyUqwAuD0btuRrbcnDHw1m5Chs3dkj5Q2MQ3Fs9CCmDSaMFPLjOUL7SVEKg-n_SkBaLuzYBg0_uPUNVPdUdVFxSNrn0ynWGa2uveRO9bjuo5Eu3wMvqGfUPg6zdqamHxID-PgDlbfMFsw9lpldZsOc6YP-PuL2euilfOVXErXFFR76dP76lRjU8qUZixptqTAklAp6MV8IbdVOCCL0T12oYsIW58fEw.3s8WxZlhOFoNH20cUp0c8Q; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODU2MTU2MzIsImV4cCI6MTY4NTYzMDExMiwiaWF0IjoxNjg1NjI2NTEyLCJqdGkiOiI1YzA0Zjg3NC0wMmU2LTQxZmYtYTQ4Ny04ZWJmOTc4NDUyZTkiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.i9I5GefR2ofr47ZrHF-pyCTWx0naw7GWqBFe9tgk4Jh4sjmhCbgVeu9gufRbfeDLWIW11nd-9uf_Vk3wxJocukYDt8CVusDlBkclH6_byVA2JiS2H95o0JNEEIUE2dAHKE-ZAPtYiJWCcntYe9lx8A_NvxgRjMViW3nTaxF8wFBk0Ht9ExsFaO1OB8tCeYRqva79NGgG89wTfFOavIf0aWfXvKOYOCGSzSrFvTTKV4HZ3zz7n1n8i3dcGDOpJuveyGHIvkUAF51MWFUg0DZem_DLzRxj5uv6txmiKvJXcw8Kb1YR9N2PObDkSMrtyblef_Vh_on7k-nbEGgVQOBznQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoieEhuVElSMDk0Y1k2OGFFNElyYlE3dyIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODU2MTU2MzIsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjg1NjMwMTEyLCJpYXQiOjE2ODU2MjY1MTIsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.cfH4AIBE63eFNeyFt4dU1uzU7A7Q8oVmEeg8vAdmdWeyzEq_PXxlGR5baL9WddXfF0JvnmMAMZ3trpYl5Yhd5q_flW1RS3FZx-AGl8-gBA-KL9Y6ITpI5WmQKFzVCbcqDDCHX6S97spTr0WlFPcmu30PXJv_DPdIi7Q_55DdIGpuge0w-4-H8dl1RS0ByWZvkTDMzb1ddRMCvAGOKyRELV956aUunWPiWVXyN0iidExNwbadPTjZdeRW9GtZHZazfITJ2lh9gNMrBPnbDZn_pmQcxwMrFuGqUBZZf7oGH9C6vu7HLr8xP6u4XPPntdMl3Hsjf4plXS15FsO5Dbtegg',
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="24", "Google Chrome";v="107", "Chromium";v="107"',
    'csrf-token': '2Mr7gc6d-LHYKK8if4yaXJnsf6EidT8VBr3M',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.121 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en',
}

def writeFile(list):
    writeFile = open('cardsforactor.csv','w')
    csvWriter = csv.writer(writeFile)
    csvWriter.writerows(list)
    writeFile.close()

def cardforactor(actorId):
    b64userid = base64.b64encode(actorId.encode('ascii')).decode("utf-8")
    opts = f'[{{"name":"actor_id","value":"{b64userid}","type":1}}]'
    params = {
        'service': 'CARD',
        'entity': 'CARDS_FOR_ACTOR',
        'monorailId': '19078',
        'options': opts
    }
    res = requests.get(url, headers=headers, params=params)
    if res.status_code != 200:
        print("Got Response ",res.status_code," for ",actorId)
        return
    res = res.json()
    list = res['dbInfo']
    a = 'state'
    # print(list)
    for i in list:

        if i['state'] == 'CREATED' or i['state'] == 'ACTIVATED' or i['state'] == 'SUSPENDED' or i['state'] == 'INITIATED':
            return (i['actor_id'],i['card_id'],i['state'],i['card_form'])
            # print(i['actor_id'],i['card_id'],i['state'],i['card_form'])

        elif i['state'] == 'BLOCKED':
            return (i['actor_id'],i['card_id'],i['state'],i['card_form'])
            # print(i['actor_id'],i['card_id'],i['state'],i['card_form'])

with open('actors.txt') as f:
    content = f.readlines()
actors = [x.strip() for x in content]
# print(actors)
outputList = list()

currentCount = 0
for x in actors:

    try:
        state = cardforactor(x)
        print(state)
    except Exception as e:
        print('Could not get card details for',x, e)
        # print(state)
        continue
    currentCount += 1
    print("Processed", currentCount, "Actors")
    outputList.append(( state))
    time.sleep(1)

writeFile(outputList)