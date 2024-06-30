import requests
import datetime as dt

"""
ISS LOCATION
# get the endpoint
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=url)
response.raise_for_status()

data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (float(latitude), float(longitude))
print(iss_position)
"""

"""
Sunrise

"""

MY_LAT = 51.587351
MY_LNG = -0.127758

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

SUNRISE_URL = "https://api.sunrise-sunset.org/json"
response = requests.get(SUNRISE_URL, params=params)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = dt.datetime.now()
time_now_hr = time_now.hour

cleaned_sunrise = sunrise.split("T")[1].split("+")[0].split(":")[0]
cleaned_sunset = sunset.split("T")[1].split("+")[0].split(":")[0]

print(time_now_hr)
