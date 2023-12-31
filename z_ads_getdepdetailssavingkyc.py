import requests
from pprint import pprint
from collections import defaultdict
import sys
import locale
import json
import base64
import time
import pandas as pd

print('ONE11')


cookies = {
    '_csrf': '7mmv4JvrZbhpViLPf1hgTrLF',
    'auth_version': 'v2',
    'single_ticket_creation_flow': 'true',
    'access_level': 'DEVELOPER',
    'access_token': 'eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJkYWZlNzc1ZC0wYWQyLTQ0NWUtYjAwMy1kNjU1NWExOWQ1NGEiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2ODg1Mzk0NTEsImV4cCI6MTY4ODU0MzA1MSwiaWF0IjoxNjg4NTM5NDUxLCJqdGkiOiI5N2ZhOTIxYi0xZjY3LTQ4NTUtOTlkYS0yMDVjOTE5MDhjZTEiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc0Nzc5NjM1Mjk4NzIwMzk4NTMifQ.DTbu9LaTiIQE7fXb3Hfsg7kxrCMr9apYz21QcMBdZ2SSRCBjz-QEzW6eAJVVmF86V7ReNf3lwgqTW2z75BbAuDcow9Lf_g4W2SsB7A07k1fN8W_5u_VZogytR5M2fHIoTg-4QI4AB21whnVNaCsn-t-HYVosj0QMZdRS-r8i0o5shUdfL0162sUlEtYqB2mh2ozKV_CI9i5A4N84HkeEZUw4gOnK3FQRNhNQFL3y_7RjpjsT6MJ__GsysRk6_rdOmPIT_9JMkjhayJntWUWV6Zsbc5lHt9MRbdJ_ZzuiVVh-yG8iwqTTAkPb-vSOZVEmSLaDmey9eGDi87JG0b_Yzw',
    'id_token': 'eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoidmZUS2Ztd0t3TDhHNl9lNEV6WlFRUSIsInN1YiI6ImRhZmU3NzVkLTBhZDItNDQ1ZS1iMDAzLWQ2NTU1YTE5ZDU0YSIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzQ3Nzk2MzUyOTg3MjAzOTg1MyIsIm5vbmNlIjoiUTByYTIxVTdPdHlFR1VVRUxqRkFQei1LZmtteWl3OEZPekNwVk5wa1FrUkRhem5INVFZS3AzcVBiS0h1aExEaWxoOFRyajRhbG04dzJaa0RzZW9PdU5felVSRENocGwyRjhFN09udi1pcHRXd1pXRnNGWU96aDE4aDBabEstY2VEbXlZdkNTSlA2eUZOWkFaZHlaSk1uUlNzWmV2dEpKekJEWmRRMldCcXlVIiwiYXVkIjoiNzMyNW0wbGFkaTliM25hODFobjhjdXMzamMiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDc0Nzc5NjM1Mjk4NzIwMzk4NTMiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNjc2NjEyMDk5MTgwIn1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4ODUzOTQ1MSwibmFtZSI6IkFkYXJzaCBBa2tlbmFwYWxsaSIsImV4cCI6MTY4ODU0MzA1MSwiaWF0IjoxNjg4NTM5NDUxLCJlbWFpbCI6ImFkYXJzaEBlcGlmaS5jb20ifQ.r9eyLrXjHbPdgWl-5N1X6x9Zz7_F4QmzRrikQgNoUlh2tGTL6b0_KWj2F1GwqPm1VXdvHYQ588PDJPABvWtQB8VF14hw29vshC3tf2QLcM67702BNHnA0Z8qvtmcw3obXwa1UJIES-VtwUBElcgZ93JdM-sD8jBnKEGYXkP672HhWM3MXJCnMCh7SWFjsqvg8CgcKIYST4TSeCdzKMuXW5mfupMNTda_9vLouvwIVxiQyH4Bl1UsFDh4MEpp-pPSQBdNmdhcTq2nR9EzwX2BvQeywODwyTMX7bJWZrAJIuoXoTaZZdGmBdwKOfKAdNglztoRQOJSTwUe1IaKYqkRZg',
    'refresh_token': 'eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.magRoyi48NisfXtMuj2kIPNUgqjWLvxRNFVSjWtBf7v0GojeoCU2HH4iNGsswWBagdFcK7RMcPSat-P9TaYhik9ZvfOhQTc98Bl1R5ww8gXnliIuSMZ4KwNZdhqjoMcwiIhnP4yAh_uSZXw3BJct7SGsyQhV9WO7kw0kktQoTULwR8eNcmF-knIqDZq5EO9hhYHYHPdemYEe4ab9_4mOwbmewDrhdfX5ZFWCtLW004JtiU1nb3aL-13nEOa6Ezwrt5PXo1VxG8U_UGJuvDZcJU634LPiDtdEnDu-dbqind5N_Kgk0O-SfqlCznQmWzqZ_dAyTXhuUlZruO1QGTdoeg.gyFo5DwtP_uJqTO1.5sYlE3sfrb8begY4avgaSz5jhxOjcULXHwwzjA_JpNdruPAjYUK8wL5XUaBwMZtaT_D5cyKza4l9HxIBioUQ68KfFMUvcZ6vByCz6l8cBF-TkOvUdjf4hRrn8TVidTGqmFdGZBIoWPBEd8PDAoS7NeEhxZuK0nZuKJZcA3agNp0F9mwZAvTaKqbnNNxyvnA2GMwilGcyElxtyoGJ45q4mTkErGmg9CI5-P_1WGf9GXkbT5tMHtHVNB-pDkHfDdTpjiJ98gYF0e4qsZ3lXDyTjkNoEYyVgiquoGvjDoqTaHj_2aLNZ4mwHVjW-lsJcClhQQwOcQSqUMIoQPxZ5bbqQ-Qt295ILDXssIZ-Q7DWpGCQAivshYnaIX6gfdEI9xSHX1etQbgslJCRK6UgEwsdhK6iL6jZP77VwGEgOrfh6Wt_4lm4yzp6Y5UD4Q_8XFz-IXoI6KlPOBge84OfdNQlCnFx6PIdvcCDoFBYNj4Q5DzM9q-AiQLahXP7ohSo3Soqm2cR4ikabLtibkv1ux4guxI9x7gi-3qCgSu7T4MLJIyjTJfPxkk0PWxAQxiJj-onFcf4zbszAIwuPj46afC1ZkE0NOG6ob4uVyxM5dF7ZJmhF0HADhJXoOWXK1nidMjSkZ5QT6ONuGqc0Z222NlUFj3UhceS62c_VsWIsRs5p6dOE0bU7O6QElhCs4sLRKnAe-n8PNgtkJKy2vIiz0QKIZ4ZhuA-L1gPkfZQF8vEmwVoKz_BGtsGLSo_kiLj00cxk7IWqWmj8uAfVjaUCtFrDTyydAP7GOK8-5ztGYm_fBu5p9NqrIyrqBVmBC4wJ-iI_W9IigORMSI6KGGd_GZYZU9r7u6yw0dsV1VL_uvLKASa68xm5cPywdbHuQS63Rwu_oZp1vN1LK-YnPWBG2KueabFmDXAVxj5O1z7u4vjgmQN8qsdSq-PDwMfN0JZcXACyzFazzyaoW9Uv3knYLLjVccD1DkxezEfz66nfF82igYEnd8DUjiCKbaefvnvelRfZ4pjQeJsciLkRUyGWQr5Vh5JaKNRjk8shjUC7-2mOC1JgojR8ClMe0j_pq2kglVq4aiDKdn8GjyIUUTW7o7P8oBdBaEhTfSLnnnnjrMjf46Xd8xRZkG5MwdkLbewb-8amWTAdpUI_dWP4lZ0cUInximqlWHUwjbdx2HvejooIUAKbTA1NrApEfwCKDIzHwF9BZSACIgX1QLe5U_-wSQlo481Zxy7Y6AtIOi4rExuGEb5_dYkBTF3Gn_1kOXQnUM-gw8QPofkNWFBS1MfiA.ScmJOU-zDQr-nRuMoxtb2g',
}



headers = {
    'authority': 'sherlock.epifi.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    # 'cookie': '_csrf=BSRwHour7ODcJU10aYF5GlyR; auth_version=v2; single_ticket_creation_flow=true; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.ZtLVhlle608qgURZf1UrdpMpZqCNT_LwQfUdsKIFO2KFTSToJKz4mCU3iwxXXQsxOddry8HY2nZRm0RTlS2v9lJl9LTRSzlce3mwdx-OJquGy6Xgy8LLQkChSx4z-GjkmmC4aN82rzdC8WyLrjeBSPD7y0HrkpdRwuRmyMypK9kUC4HwkW_h-UYgg-AMg1ih-nPFrbrFbydKn-Ogvn1heh0jxKpwHvHW4cYe_t9OEiEr_lGMkjVV4m9FcdJ_bt1Ndc4VmOZyyjxmrJbS1GFB91HscoeUm8Nbne9LBTLWUu8St424aAU49D0KiVSCwT6LaTiMwOfThcG98Hini-AXyQ.oW1S4ixU752VQzMH.UdCp21XFs6tLDU9rfz06U9-t-tDDQuunxXKn-uK7EXXRxLGI4RCMoth6sYa137UILd4U8UQAMMRwgHyoq9BMeMxdd6sxyJNeuUXkHEFFI624f8GolwPnhOENGMVrhOTeDBwir52uxsItNrYzgmjM1KSULce8LTDL1ykn69T_WOyr0W8FpU5hct6hItT8zE6irzHyPsEBkto8knYuqj1LHoXzWAVO3tOwUq8x1WkRdrnU3tleP9XR2sGD20BtGZndb_hMuU8W-8ZGEyrG1wOdu4ptGj0kYiLPBhRHOaqq131ZMDDIJlIIMMZV74wlqZmNAOltbX-fcx134DetjxG6ErD_SV_HnttbKMHk5EQCREtVzM4oRzYAsD3SBFZ7oVD0mXBWFsHSMNflmoFTTYJYSo5byhYjhU2Kw9Ocm5ByuG4m7Qwkk23-P3IThzVo3AL3TmJeQbxVvAq_wz8Y8jdgn4e9tzoJqijLjU0l7aIsG7H0tb_POkfoY5mmDiSBfT7o4X69V5QVUtm1shsziRBB7q-SkNykrwSeWCKK5_j7256a_iXU7UImr04uBcUaMiobNXa_d5PofYm-DBwp3E0H9wjvP0PJO03AmuP_fDUWrPW8HRH83m1f8qpwPcwN4p7dcBRnG2ymzyn5Zy7SEASSI25Oly6u1L-eZ5vpiJWz15lnLy2zeoVyFezThzn7U1dnM0NYoDjjbAlMhIt2V2buGXolNhoV3OSkwh6v_kRgJ48s32iTOqB1lvTXvoOztJDnU3z1-qlapFKfnpeaREwOSeJbLLnSwmqfU7Zf3V3pscxov1L6vykmM0oLnLUx88WArbVL_y4Xoaq6fGBl0cP3NkErHBfZE_YSUjrhFqDKP_wTiKi9-y-JwslwwJW-PzoUuyWvq8HSIX6j_w5Uve6LnlPhXkPJxlEwHBJ1i0zQcX967XgnAKOf29yDef7erIWr6NqhZ0I5pW1UO5NkvwOWpnJoLVWaZ9uT3UsDkVpArR78RmNKCVXWAXRdLEICrzRJ1MzsmS6WkUozpbawjSuojVq3u66DvJm9gSWikSXXpFXpNwH_mA_-rCsahlBaGfC8m3ohhzt_1-zH0mJjvbhkrvk_72eHJszwG6f29nTgy2rdps-uvWPIPM2prjPXFaWHNKRDZFA0vrJrIglObDuSfRSYpJaziSLjT5RlSlIUfpsiJzTMIXs4_Lwn3r3TTLE6M6ZHRUrx-LYcGliskHONEW1MKezLZ0e1vv3apD5V8rDs_W72oEXNiaGKio--uXDrMKMgiEz1RYS1woL1nQ.4xcAha3brNK10hE9yYtGag; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJkYWZlNzc1ZC0wYWQyLTQ0NWUtYjAwMy1kNjU1NWExOWQ1NGEiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2Nzk4OTk1NTMsImV4cCI6MTY3OTkxMDM3NiwiaWF0IjoxNjc5OTA2Nzc2LCJqdGkiOiJmYzM3YzY0YS0yNDlmLTQ4OTYtYmE2MS0wODMxNmVlYWJiZDkiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc0Nzc5NjM1Mjk4NzIwMzk4NTMifQ.MoQ6h1mRHiJNWJQTYiC1lckoYyTvyHPCKvdp8p2iJNRXaIeqnQ5sJkZiB3Q6Xbebbp3Lpy62mIqgTDxclAisd5CWM9vcHgYa3chfrbX4JEUK5li6kzgd9A28HQg9fqrk_J0NFV8ruyTjEs-8QFYocQQBeHC20vf9RKh_Y0r4PuGsoFtXWrQgGNHcM8-3mUdSIySEqhVm2FICGVnq1aPsjTpzkQkHL4Hp1ZrK6-SHFB5zbeevRIKaD-TK94SumGRIYgS14ShDMzbjVew_KZCvYcpwpWNe7cs-K_WMzyXcXm8oROQ1Vn9AyS-99pAvZ0b8pQZWlhXCF6-mG_5usUejgQ; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiN2ZwR213b0pMZWZwYV95eE9JSExQdyIsInN1YiI6ImRhZmU3NzVkLTBhZDItNDQ1ZS1iMDAzLWQ2NTU1YTE5ZDU0YSIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzQ3Nzk2MzUyOTg3MjAzOTg1MyIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NDc3OTYzNTI5ODcyMDM5ODUzIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY3NjYxMjA5OTE4MCJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2Nzk4OTk1NTMsIm5hbWUiOiJBZGFyc2ggQWtrZW5hcGFsbGkiLCJleHAiOjE2Nzk5MTAzNzYsImlhdCI6MTY3OTkwNjc3NiwiZW1haWwiOiJhZGFyc2hAZXBpZmkuY29tIn0.HJVjTP8dJ9E6l8kzmoFGRu8kD6gXWw9kL6hdMA5a1t7te43J_NcWxe9-OblImoGFKx8VtVImLVRaDXBhbcyP6VSKXFz0J1QMDycwg9_nf_M6SKfTtbh1SHcH1ymxwb4MV2YL8eQ14F_rzIBiUiPhD1kKvC87ctvyP9e1FMY8Dtspgr2wbwC1Rt1jexyMynEJuydmBPW9sSIBE2950Xbq2co0ShNprDQitB4qQeEkyxBGGjbM_jkC0Im16vhvVE4jyF9yT3z9wEhrjXlJAkMVdKZBUH42vCqunvOz8IUxatWEdXUudCxR7u679Sd3iIXUNwHMdThvD8QaMAIslnH71Q; access_level=DEVELOPER',
    'csrf-token': '9ydRPJzh-mnSrhhqOUCLjDqtax9-iOtUo-nQ',
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







def getSingleDepositDetails(actor_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'deposit_id',
                    'value': str(base64.urlsafe_b64encode(actor_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    print('---------------adarsh----')
    params  = {
        'service':  'DEPOSIT',
        'entity':   'SINGLE_DEPOSIT',
        'options':  json_dump,
        'monorailId':'16066',
    }
    
    r = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=100)
    
    # name, actor_id, state, scheme_code, account_number, maturity_date
    try:
        print('---------------adarsheee----')
        dbInfo = r.json()["dbInfo"]
        print("executing deposit")
        Id = str(dbInfo.get("Id"))
        depositnumber = str(dbInfo.get("AccountNumber"))
        maturitydate=str(dbInfo.get("MaturityDate"))
        state = str(dbInfo.get("State"))
        actorid = str(dbInfo.get("ActorId"))



        return Id,depositnumber,maturitydate,state,actorid
            
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
        
    


def getkycPhone(actor_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'actor_id',
                    'value': str(base64.urlsafe_b64encode(actor_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    # print('json dump --> '+json_dump)
    params  = {
        'service':  'USER',
        'entity':   'USER',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=100)
    # name, actor_id, state, scheme_code, account_number, maturity_date
    print("executing kyc &phnumber")
    try:
        dbInfo = r.json()["dbInfo"]
        #print("GETTING NUMBER")

        phnumber= str(dbInfo.get("user").get("profile").get("phoneNumber").get("nationalNumber"))
        kyclevel = str(dbInfo.get("user").get("customerInfos")[0].get("kycLevel"))

            
        # print('Entity Id --> '+dbInfo["Actor"].get("entity_id"))
        return phnumber,kyclevel
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)

    
def getSavingAccountNumber(actor_id):
    print("fi")
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'actor_id',
                    'value': str(base64.urlsafe_b64encode(actor_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    print('executing savings account')
    params  = {
        'service':  'PAYMENT_INSTRUMENT',
        'entity':   'PAYMENT_INSTRUMENT',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=100)
    # print('url --> ',  r.url)
    try:
        op = ''
        dbInfo = r.json()["dbInfo"]
        for x in dbInfo:
            # print('XYZZY --> '+str(x))
            savings = str(x.get("Identifier").get("account_type")) == 'SAVINGS'
            type = str(x.get("Type")) == 'BANK_ACCOUNT'
            if savings and type:
                #print('INSIDE FOR LOOP --> '+str(x))
                #print('Account number --> ',x.get("Identifier").get("actual_account_number"))
                #print('============================')
                op = x.get("Identifier").get("actual_account_number")
        # print('Entity Id --> '+dbInfo["Actor"].get("entity_id"))
        return op,actor_id
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)



def getSavingAccountConst(saving_acc):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    opts = [
                {
                    'name': 'account_no',
                    'value': str(base64.urlsafe_b64encode(saving_acc.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    print('executing SavingsAccount')
    params  = {
        'service':  'SAVINGS',
        'entity':   'SAVINGS_ACCOUNT',
        'options':  json_dump,
        'monorailId':'1',
    }
    
    r = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=100)
    print('executing SavingsAccount')
    try:
        dbInfo = r.json()["dbInfo"]
        Actorid= str(dbInfo.get("actorId"))
        #kyclevel = str(dbInfo.get("user").get("customerInfos")[0].get("kycLevel"))

            
        # print('Entity Id --> '+dbInfo["Actor"].get("entity_id"))
        return Actorid
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)






deposit_results = []

def append_to_deposit_results(Id,depositnumber,maturitydate,state,actorid,savingsaccno,actid):
    row = []
    row.append(Id)
    row.append(depositnumber)
    row.append(maturitydate)
    row.append(state)
    row.append(state)
    row.append(actorid)
    #row.append(schemecode)
    row.append(savingsaccno)
    row.append(actid)
   
    #
    deposit_results.append(row)

csv_name = "/Users/adarshakkenapalli/Downloads/inputfile2 - Sheet1.csv"
data = pd.read_csv(csv_name, usecols=['orderid'])

def orderdetails(actor_id):
    url = "https://sherlock.epifi.in/api/v1/db-states/info"
    print('-------------------')
    opts = [
                {
                    'name': 'order_id',
                    'value': str(base64.urlsafe_b64encode(actor_id.encode("utf-8")), "utf-8"),
                    'type': 1,
                },
            ]
    json_dump = json.dumps(opts, separators=(',', ':'))
    print('-------------------')
    params  = {
        'service':  'ORDER',
        'entity':   'ORDER',
        'options':  json_dump,
        'monorailId':'16066',
    }
    r = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=100)
    # name, actor_id, state, scheme_code, account_number, maturity_date
    try:
        dbInfo = r.json()["dbInfo"]
        print("executing ORDERS")
        return dbInfo["status"],dbInfo["id"],dbInfo["workflow"],dbInfo["externalId"]
    except Exception as e:
        raise Exception('api call failed', r.status_code, r.text, e)
        raise Exception('api call failed', r.status_code, r.text, e)
    
count = 0
i = 0
try:
    for i in range(len(data.orderid)):
        try:
            print("Attempting to get deposit details for row", i)
            deposit_id = data.orderid[i]
            #id, name, actor_id, state, scheme_code, account_number, maturity_date = getSingleDepositDetails(deposit_id)
            #time.sleep(3)
            
            Id,depositnumber,maturitydate,state,actorid = getSingleDepositDetails(deposit_id)
            
            time.sleep(2)
            
            #status,id,workflow,externalId=orderdetails(savingsaccno)
            
            #status,id=orderdetails(deposit_id)
            #
            savingsaccno,actid=getSavingAccountNumber(actorid)
            #time.sleep(2)
            #Actorid=getSavingAccountConst(savingsaccno)
            time.sleep(2)
            #phnumber,kyclevel=getkycPhone(actor_id)
            #time.sleep(3.5)
            print(Id,depositnumber,maturitydate,state,actorid,savingsaccno,actid)
            #print(id, name, actor_id, state, scheme_code, account_number, maturity_date, phnumber)
            append_to_deposit_results(Id,depositnumber,maturitydate,state,actorid,savingsaccno,actid)
            #append_to_deposit_results(depositnumber,maturity,depositid,CreatedAt,state,ActorId,schemecode)
            #print("completed for ",i)
        except Exception as e:
            print("Exception when processing request --> ", e)
            #append_to_deposit_results(id,)
        count+=1

        

except Exception as e:
    print('exception at count: row : e', count, i, e)


#print('TWO')
df = pd.DataFrame(deposit_results, columns=['a','Id','depositnumber','maturitydate','state','actorid','savingsaccno','actid'])
df.to_csv('/Users/adarshakkenapalli/Downloads/outputfile2 - Sheet1.csv')