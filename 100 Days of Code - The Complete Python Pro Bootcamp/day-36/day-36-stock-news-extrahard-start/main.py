from alphavantage import alphavantage_data
from getnews import get_news_data
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_price_data = alphavantage_data["Time Series (Daily)"]

last_two_date = []
for key in stock_price_data:
    last_two_date.append({key: stock_price_data[key]})
    if len(last_two_date) == 2:
        break

latest_data = list(last_two_date[0].items())[0]
earlier_data = list(last_two_date[1].items())[0]

delta_price = round(((float(latest_data[1]["4. close"]) - float(earlier_data[1]["4. close"])) /
                     float(earlier_data[1]["4. close"])) * 100, 2)

if abs(delta_price) >= 5:
    print(f"Change in price is: {delta_price}%. Here's some news.")
else:
    print(f"Nope, change in price is {delta_price}%. No news for you.")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

top_three_news = [news for news in get_news_data]

if len(top_three_news) > 3:
    top_three_news = top_three_news[:3]

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
if delta_price >= 0:
    icon = "▼"
else:
    icon = "▲"

account_sid = ""
auth_token = ""
_from = ""
_to = ""

if abs(delta_price) >= 5:
    for item in top_three_news:
        body_message = (f"{STOCK}: {icon}{abs(delta_price)}% \n "
                        f"Headline: {item["title"]} \n"
                        f"Brief: {item["description"]}")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body_message,
            from_=_from,
            to=_to
        )
        print(message.status)

# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
