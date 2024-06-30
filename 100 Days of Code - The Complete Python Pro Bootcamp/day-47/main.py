import os
import requests
import smtplib
from bs4 import BeautifulSoup

# -------------------------------------------------------SCRAPE------------------------------------------------------- #
PRODUCT_URL = os.environ.get("ENV_PRODUCT_URL")

response = requests.get(url=PRODUCT_URL)
response.raise_for_status()
product_html = response.text

soup = BeautifulSoup(product_html, "html.parser")
print(soup.prettify())

# -----------------------------------------------------GET PRICE----------------------------------------------------- #
price = soup.find_all("span", class_="FirstPrice")
# converts price to integer
price_cleaned = int(price[0].getText()[1:].replace(",", ""))
target_price = 30000

# gets item name
item_name = soup.find_all("h1", class_="Title-pdp-title")
item_name_cleaned = item_name[0].span.getText()

# -----------------------------------------------------SEND NOTIF----------------------------------------------------- #
EMAIL_FROM = os.environ.get("ENV_GMAIL_FROM")
EMAIL_TO = os.environ.get("ENV_GMAIL_TO")
EMAIL_AUTH = os.environ.get("ENV_GMAIL_AUTH")

if price_cleaned <= target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL_FROM, EMAIL_AUTH)
        connection.sendmail(from_addr=EMAIL_FROM,
                            to_addrs=EMAIL_TO,
                            msg="Subject: Item on watchlist now affordable! \n\n"
                                f"You can now get that {item_name_cleaned} for only {price_cleaned}! :) \n"
                                f"What are your waiting for? \n"
                                f"Go to {PRODUCT_URL} and get that stuff!\n\n\n"
                                f"All yours,\n"
                                f"krloves :'>")

# --------------------------------------------------REFERENCE/NOTES-------------------------------------------------- #

"""
header info: https://myhttpheader.com/
header in response.get(): https://stackoverflow.com/questions/30561260/python-change-accept-language-using-requests

amazon link is not working huhu
had to search for different website that can be scraped
had to hide that different website to for security purposes hihi
"""
