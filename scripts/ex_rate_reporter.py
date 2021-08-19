#!/usr/bin/env python3
import os
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from requests.api import get


# Send payload to IFTTT Webhook
def post_ifttt_webhook(val1, val2='', val3=''):
    event_id = 'test'
    ifttt_key = 'dLimi8qLNsDkDak0L_8TTz'
    payload = {"value1": val1, "value2": val2, "value3": val3}
    url = "https://maker.ifttt.com/trigger/" + event_id + "/with/key/" + ifttt_key
    try:
        response = requests.post(url, data=payload)
    except Exception as e:
        print("Failed to post payload to ifttt webhook:", e.args)
        return None

    return response


# Get Google Spreadsheet
def get_worksheet():
    prjdir = os.path.dirname(__file__)
    ACCESS_KEY_JSON = prjdir + "/credentials/finance-info-321309-964efabe11ed.json"
    SPREAD_SHEET_KEY = "1d_yUNISenm8Xz0Y9nOBrrhR4wACTGhWkKp1tvd2zEAc"
    credentials = ServiceAccountCredentials.from_json_keyfile_name(ACCESS_KEY_JSON, [
                                                                   'https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])
    try:
        worksheet = gspread.authorize(
            credentials).open_by_key(SPREAD_SHEET_KEY).sheet1
    except Exception as e:
        print("Error: failed to get a gspread worksheet")
        return None

    return worksheet


def run():
    worksheet = get_worksheet()
    if worksheet is None:
        exit(1)

    data = worksheet.get_all_values()
    dictData = dict(data)

    ret = post_ifttt_webhook('USDJPY', dictData['USDJPY'])
    if ret is not None:
        print('Successfully sent a payload')


if __name__ == "__main__":
    run()
    print('DONE')
