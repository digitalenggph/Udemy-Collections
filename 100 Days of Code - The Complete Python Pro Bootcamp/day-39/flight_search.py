import os
import requests

# ----------------------FLIGHT SEARCH DETAILS----------------------#
ENDPOINT_HOST = "sky-scanner3.p.rapidapi.com"
API_KEY = os.environ.get("ENV_RAPIDAPI_KEY")
# -----------------------------------------------------------------#

endpoint_auto_complete = f"https://{ENDPOINT_HOST}/flights/auto-complete"
endpoint_one_way = f"https://{ENDPOINT_HOST}/flights/search-one-way"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": ENDPOINT_HOST,
}


class FlightSearch:
    def __init__(self):
        self.endpoint_iata = endpoint_auto_complete
        self.endpoint_one_way = endpoint_one_way

    def iata_code(self, city):
        querystring = {
            "query": city,
            "placeType": "CITY",
        }

        request = requests.get(url=self.endpoint_iata,
                               params=querystring,
                               headers=headers)
        request.raise_for_status()
        response = request.json()
        iata = response['data'][0]['presentation']['skyId']
        return iata

    def search_flights(self, year_month, origin, destination):
        querystring = {
            "fromEntityId": origin,
            "toEntityId": destination,
            "wholeMonthDepart": year_month
        }

        request = requests.get(url=self.endpoint_one_way,
                               params=querystring,
                               headers=headers)
        request.raise_for_status()
        flights = request.json()
        return flights

