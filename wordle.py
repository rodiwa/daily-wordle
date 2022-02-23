"""
Simple hack to web-scrape Wordle answere sites and send to slack, telegram twice a day
2PM IST (30 8 * * ? *) and 8PM IST (30 14 * * ? *)
crons are in GMT
"""

import json
import os
import requests
from bs4 import BeautifulSoup

# configure these in env varieables
# WORDLE_ANSWER_SITE_URL
# SLACK_WEBHOOK_URL
# TELEGRAM_GROUP_CHAT_ID
# TELEGRAM_GROUP_CHAT_URL

def main():
    """
    gets wordle for the day and sends to configured groups and channels
    """
    wordle = None
    try:
        wordle = get_wordle_for_today()
        send_to_slack_channel(wordle)
        send_to_telegram_group(wordle)
        print("Wordle of the day sent to slack successfully")
    except Exception as err:
        print(err)
    print(wordle)

def get_site_content(url):
    """
    util function to get content of web site to scrape
    """
    content = ""
    try:
        content = requests.get(url).content
    except Exception as err:
        print(err)
    return content

def get_wordle_for_today():
    """
    web-scrapes wordle of the day from given site
    """
    WORDLE_ANSWER_SITE_URL = os.environ["WORDLE_ANSWER_SITE_URL"]
    wordle_for_today = None
    try:
        content = get_site_content(WORDLE_ANSWER_SITE_URL)
        soup = BeautifulSoup(content, "html5lib")
        header = soup.select("h2[id='0-wordle-answers'] ~ p")
        wordle_for_today = header[0].get_text()
        return wordle_for_today
    except Exception as err:
        print(err)

def send_to_slack_channel(wordle):
    """
    sends wordle to slack channel
    """
    SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
    payload={"text": wordle}
    try:
        requests.post(SLACK_WEBHOOK_URL, json=payload)
    except Exception as err:
        print(err)

def send_to_telegram_group(wordle):
    """
    sends wordle to telegram group
    """
    TELEGRAM_GROUP_CHAT_ID = os.environ["TELEGRAM_GROUP_CHAT_ID"]
    TELEGRAM_GROUP_CHAT_URL = os.environ["TELEGRAM_GROUP_CHAT_URL"]
    try:
        payload = {
            "chat_id": TELEGRAM_GROUP_CHAT_ID,
            "text": wordle
        }
        requests.post(TELEGRAM_GROUP_CHAT_URL, json=payload)
    except Exception as e:
        print(e)

def lambda_handler(event, context):
    main()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Wordle of the day successfully sent to Slack!')
    }


if __name__ == "__main__":
    main()
