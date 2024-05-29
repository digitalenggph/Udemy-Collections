import os
import requests

# ----------------------FLIGHT SEARCH DETAILS----------------------#
ENDPOINT_HOST = "sky-scanner3.p.rapidapi.com"
API_KEY = os.environ.get("ENV_RAPIDAPI_KEY")
# -----------------------------------------------------------------#

endpoint_auto_complete = f"https://{ENDPOINT_HOST}/flights/auto-complete"
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": ENDPOINT_HOST,
}


class FlightSearch:
    def __init__(self):
        self.endpoint = endpoint_auto_complete

    def iata_code(self, city):
        querystring = {
            "query": city,
            "placeType": "CITY",
        }

        request = requests.get(url=self.endpoint,
                               params=querystring,
                               headers=headers)
        request.raise_for_status()
        response = request.json()
        iata = response['data'][0]['presentation']['skyId']
        return iata

    def search_flight(self):
        pass

# -------------------TEST IF CLASS WORKS-------------------#
# trial = FlightSearch("Amsterdam")
# print(trial.iata_code())
