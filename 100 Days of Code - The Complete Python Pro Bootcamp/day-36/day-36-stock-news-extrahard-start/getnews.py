import requests
import datetime as dt


date_now = dt.datetime.now()
date_yesterday = date_now - datetime.timedelta(days=1)

URL = ""
API_KEY = ""
COMPANY_NAME = "Tesla Inc"

params = {
    "q": COMPANY_NAME,
    "from": date_yesterday.strftime("%Y-%m-%d"),
    "to": date_now.strftime("%Y-%m-%d"),
    "language": "en",
    "sortBy": "popularity",
    "apiKey": API_KEY
}

requests = requests.get(url=URL, params=params)
requests.raise_for_status()

get_news_data = requests.json()["articles"]
