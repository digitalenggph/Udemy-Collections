import requests
from twilio.rest import Client

# Burnham Park in Baguio City

URL = "https://api.openweathermap.org/data/2.5/forecast"  # URL for 5-days every 3-hour forecast
api_key = ""
account_sid = ""
auth_token = ""

twilio_num = ""
my_num = ""

params = {
    "lat": 16.412195037471665,
    "lon": 120.59306415679579,
    "cnt": 4,  # number of timestamps, which will be returned in the API response
    "appid": api_key,
}

# cnt: 4 -> gets 12-hour data
# weather data from API starts at 3am
# code will get weather data from 3am to 3pm :D

requests = requests.get(url=URL, params=params)
requests.raise_for_status()

data = requests.json()
weather_data = data["list"]

for weather in weather_data:
    weather_code = weather["weather"][0]["id"]
    if int(weather_code) < 700:
        # send message using twilio
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an umbrella",
                from_=twilio_num,
                to=my_num
            )

        # stop looping once if-statement is true
        break
