import requests
import time
import pandas as pd

def force_trigger_recon(card_request_stage_id):
    url = "https://sherlock.epifi.in/api/v1/dev-actions/execute"
    body = {
        "monorailId": "1",
        "parameters": [

            {
                "name": "card_request_stage_id",
                "value": str(card_request_stage_id),
                "type": 1,
            },
            {
                "name": "updated_card_request_stage_status",
                "value": "CARD_REQUEST_STAGE_STATUS_IN_PROGRESS",
                "type": 5,
            },
            {
                "name": "reason",
                "value": "Resetting work flow",
                "type": 100,
            },
        ],
        "action": "CREDIT_CARD_UPDATE_CARD_REQUEST_STAGE_STATUS"
    }
    
    headers = {
        "Cookie": "_csrf=OiXhHgGRUoZ6YC2eo-ULlujE; auth_version=v2; single_ticket_creation_flow=true; access_level=DEVELOPER; access_token=eyJraWQiOiJOR3JNMnViMFVaTlBSYUQ4MlV5REx3RFdcL1ExRjB2MDhzVWlIb1J4TE9mcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViY2NmYi0zMmY1LTQyNzktYmZhNy1jNzA1Zjg5YTRmZmYiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aC0xX2ZoU24zN0Zkc19Hb29nbGUiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3MzI1bTBsYWRpOWIzbmE4MWhuOGN1czNqYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2OTU3NDE0NzEsImV4cCI6MTY5NTc0NTA3MSwiaWF0IjoxNjk1NzQxNDcxLCJqdGkiOiI0MGViM2U3Mi00ZjY4LTQ3NzQtYjI1Ni1iZGMxMjZmMjQ3YTgiLCJ1c2VybmFtZSI6Imdvb2dsZV8xMDc3NTAzNjg5NjU1OTk5ODUyODAifQ.Yb2a-4rpAutuOczxDXPo6tKWDaYaUVha6-7YgNp9QQ20eEwpk1o1tOg8T4nVnEAz9v-vRUCcc-O4t8A_tSfdh3yYAFsJ4iHtXWX6clJec69yx-Kvu1A_1--jAPHIy0ZDjctvnO6R7bvPlqRMnB5i6GBRJTy7FGKuzwdRzisOytTcCMsLAKj11lRcByJoy8R2EAIBASKF9VDYFwHPKWrAGEE1f5YAeFV7uN-R9mcUKGELKJIv9ENC2YHrPXBLc6lv9wl5yO0Wkef4XyVf6aunPQh-dMTbvX78bxPWZDuLlTXY-dnR1uVF6X4tJDdr-QzI5b_dKjHBRXpY3c7wsVEs-A; id_token=eyJraWQiOiJVSVVIS0hFcmJVeWpQTFkxS1oxeUhYWHhIcWszUkxqQW1qYlpWeVdweGp3PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiWFVIVU5RbC1Ha2VicHd1YWFYblBpUSIsInN1YiI6ImIzNWJjY2ZiLTMyZjUtNDI3OS1iZmE3LWM3MDVmODlhNGZmZiIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfZmhTbjM3RmRzX0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV9maFNuMzdGZHMiLCJjb2duaXRvOnVzZXJuYW1lIjoiZ29vZ2xlXzEwNzc1MDM2ODk2NTU5OTk4NTI4MCIsImF1ZCI6IjczMjVtMGxhZGk5YjNuYTgxaG44Y3VzM2pjIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA3NzUwMzY4OTY1NTk5OTg1MjgwIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY4MzE5MDAxNDk3NyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTU3NDE0NzEsIm5hbWUiOiJTaGFyaXF1ZSBSYWhpIiwiZXhwIjoxNjk1NzQ1MDcxLCJpYXQiOjE2OTU3NDE0NzEsImVtYWlsIjoic2hhcmlxdWVAZXBpZmkuY29tIn0.IKih_21HfQj7J47OTA4DpChMitccmEvkoGEe8NjPOFvf2oA89MX0EjYw-iS5byWGtn_xK6QGsJ5TRi_kEiJ-MGaLMWOzEeP1l4j2cKApO8wNGzqtx5-J95xyTeTpw4pRV0tQ4UtLxlyQ6v44MUFqnSeyfEdOPFAavJg2NlHnaBXWsMtQZWV6w29PpXKnNvb82v9Kbceou0Bjb-bDRW_kTUbldcsnhu6hEcA67LveJ0JIcdiCY0pFput2QZtAYsk9SAmMWPvObkvaeqwydPgiqLo_iVc3M093XpIjW2pUSeDMJkDlI4NndtnoZr4NzRrtqjjYGaUKeESSkpOd1FS7RA; refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.hrfrQA36GUorysmqjEK9EH1iv2rHAKh-INNOOolY-guwM9DDxL8rQsplRy-Ar4yP5ZOLIVjV_S8dCEjL5QYQMehZy4KPDC_k3pNZfYmtFD017mVFFlA4HoU5bTDHvTYFo77b4gCZnahj7cWzjpogjqbIM4mJ89XD6EEzqaHCaE_j3Y6YhS10o4nmNigHiPz_qARLvke04vvpaKoSBa4XhegpkdOC7lJ-drLXsX3G_QzgCSZ-BcKS0FGD29TfK2VG6ECbXptLFRAvRDG1cYC8ZJcjTXTF0D8SOEB5N4AdvHJZssx2d9q1ggk0GfR_7_HoMKkdwPO3N4J1bVLYMRqsAQ.gUfDV9DhebL6muN7.58oTBMc5LpGGmcgH4Av7oYfAQYKj-yg3TR4Sraq8qTgXBYv-hbrk_HCrYNjDJH5rGhmcr-L0PN7NrYeZEA_CA9OrKXCEh_7r5xT4Y8eaCnzd2hWH3cFWHPSnVK9mZTD84uK6g8-Yp9By_8Sgb860obLlHHTOsSuqxEVOMgR7SV6HFmNfjmFki-_46PFljH8NlASeISgVmf3Etp9HYNURsTAfxTC1ZsogHstQfVkEW-C0kJd19JkEK9rJIVbafKS9xodqWpGqLDK7AXY_-lK1H79BVuuU9TB15XDrhU4LnzTXITJTYE-3cRVFWOPqFi4yMu_q-_-dwABUHhOk6fVR2L0m79oD1Hqa60js3EqX3HZ1yl5QzHijkNRq6WZC1pNWSuUL8yqPwJ2bby6AqXSdISOtXBkPRPn_pSJSacWOCQdJXXlKTQlVHYlr0Dzxp94L2QJCN4g-K9DmXuWIFUJDBsuvvq1zT1ZEFySIJZepKJdTXDq_KIpQvyY9ISIcQi8y3cSr7SwvcsgTyUlhMNKXb2l5dbocDV34r20Qm0fTvjphdT65plhXDw4jdb6iNj6RN5yRFXHGTdipC1Bg69b6Xkcw6ziKmpCiMynMvnde05Xx9RBI9vBBx3sS9_wrErQvtKe8xXHtQvmRXY3Ev01ZhHpMNqEJZxiWgxceaf4PlTIt_H8GucZxlC_WRAXfww3pm0sdHwb_zupoNy1tyQuyscclJ1KbSN0JBmcaYOb4PxTolKd3DSi55HJLSBU0JfaIEd0TZLrJIbRYIEbpeWfahFDj49oFsvp7tUjbIEXlnY39kh4-hWPzDQLj5PbUs1HEXohsJPy2oopE1KK12tFumZFNQWIDlqpJ-Kia4b0NovcoBJYx9DnZp3J5mjegiTZLNxBd7sygi5fLtmlqGtkNYUiQ12aJsuX_S5LNY9YWWWqBGD1vTJzk8ir0OqEMBTujyZ4BBtZZBx09dtcj7-KavcR-D5I7sDgBYpfgknv8o4dF1sw2c3JX8omUMiaK_NiWEld5bnlOhkiv5PoxP-J3ZgG1p7dm9uiDhYYVNgLZcNJwhZImyJnA03iCPr5YZz-oav-OKhTf4nkH9z4n0EpBWaf-R7OI6rpoCD7fhI-FaHmxKcGvrtlU2aAAOFHr71XP1bqhpP_JRNzxidJotOikZY0I3SMmDdsAQy2T3XmX_zDBjOJwify2cfNK57JsIWXpwhEoSRWfvaXT0TM0_TI6ClYjavsrRonl-3yQceZNPgNtJ_Jok62bc4mguWOvAHxnhJujdlPnc1pvopxN4w.dp_hpnVhkwkYmfXJw4BrCg",
        "Host": "sherlock.epifi.in",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "csrf-token": "njPZ54Im-YEDJIZ3ECALCEsr-ckDi4rZsDZk",
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

csv_name = "/Users/shariquerahi/Downloads/input_dev_action.csv"
data = pd.read_csv(csv_name, usecols=['card_request_stage_id'])

try:
    for i in range(len(data)):
        card_request_stage_id = data.loc[i, 'card_request_stage_id']
        print("Attempting to trigger force recon for card_request_stage_id:", card_request_stage_id)
        status = force_trigger_recon(card_request_stage_id)
        print("Status:", status)
        print("-----------------------")
        time.sleep(7)

except Exception as e:
    print("Exception:", str(e))

