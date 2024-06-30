import os
import requests

# ----------------------SHEETY DETAILS----------------------#
USERNAME_SHEETY = os.environ.get("ENV_SHEETY_USERNAME")
BEARER_TOKEN = os.environ.get("ENV_SHEETY_BEARER_TOKEN")
ENDPOINT = "https://api.sheety.co"
PROJECT_NAME = "krlovesFlightdeals"
SHEET_NAME = "prices"
# ----------------------------------------------------------#

url_flight_deals = f"{ENDPOINT}/{USERNAME_SHEETY}/{PROJECT_NAME}/{SHEET_NAME}"

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = url_flight_deals

    def get_data(self):
        request = requests.get(url=self.endpoint,
                               headers=headers)
        request.raise_for_status()
        response = request.json()

        return response

    def update_row_iata(self, index, iata):
        body = {
            "price": {
                "iataCode": iata
            }
        }
        request = requests.put(url=f"{self.endpoint}/{str(index)}",
                               json=body,
                               headers=headers)
        response = request.json()
        return response

