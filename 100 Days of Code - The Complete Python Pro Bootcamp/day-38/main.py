import os
import requests
import datetime as dt

# -----------------GET ENVIRONMENT VARIABLES-----------------#
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
USERNAME_SHEETY = os.environ.get("SHEETY_USERNAME")
AUTH_SHEETY = os.environ.get("SHEETY_AUTH")

# ----------------------GET API DETAILS----------------------#
url_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

# --------------------GET EXERCISE STATS---------------------#
query = input("So what'd you do today? ")

params = {
    "query": query,
    "weight_kg": 55,
    "height_cm": 155,
    "age": 27
}

stats = requests.post(url=url_nutritionix, json=params, headers=headers)
stats.raise_for_status()

response = stats.json()

# ----------SAVE DATA TO GOOGLE SHEETS VIA SHEETY-----------#
project_name = "krlovesWorkouts"
sheet_name = "workouts"

url_sheety = f"https://api.sheety.co/{USERNAME_SHEETY}/{project_name}/{sheet_name}"
headers_sheety = {
    "Authorization": f"Basic {AUTH_SHEETY}"
}


date_now = dt.datetime.now().strftime("%d/%m/%Y")
time_now = dt.datetime.now().strftime("%X")

for exercise in response["exercises"]:
    add_entries_params = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    add_entries = requests.post(url=url_sheety, json=add_entries_params, headers=headers_sheety)
    add_entries.raise_for_status()

    print(add_entries.text)
