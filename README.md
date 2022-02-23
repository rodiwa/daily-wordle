# Wordle A Day
This simple hack sends you daily wordles to your phone. Its uses a simple web scraper and some simple integrations to send you messages on Slack and Telegram.

### How to Run this locally
- Bring up your venv to get started.
- Install dependencies. You can use requirements.txt.
- Configure environment variables for the following values
  - WORDLE_ANSWER_SITE_URL - This is the web page you scrape to get your answers. I used [this one](https://gamerjournalist.com/wordle-answers/).
  - SLACK_WEBHOOK_URL - You'll have to create a Slack channel, and on that channel create an (Incoming Webhook) app integration to get its webhook URL.
  - TELEGRAM_GROUP_CHAT_ID, TELEGRAM_GROUP_CHAT_URL - For this, I created a new group on Telegram and set up integrations by creating an app.

### Schedule to run at intervals
- I deployed this code on an AWS Lambda.
- Then I configured a simple Cloudwatch event rule (cron schedule) to run this at regular intervals.

### Versions
Python 3.8.9
pip 22.0.3