import pandas as pd

from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

import datetime as dt


# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# TODO 1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
#  International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet
#  include multiple airports, you want the city code (not the airport code see here).

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

data_sheety = data_manager.get_data()
print(data_sheety)

for data in data_sheety["prices"]:
    city = data["city"]
    iata_code = data["iataCode"]
    if len(iata_code) == 0:
        iata = flight_search.iata_code(city)
        row_num = data_sheety["prices"].index(data) + 2
        data_manager.update_row_iata(row_num, iata)

# TODO 2. Use the Flight Search API to check for the cheapest flights from tomorrow to
#  6 months later for all the cities in the Google Sheet.

today = dt.datetime.now()
today_year_mon = today.strftime("%Y-%m")

months_to_get = 3
month_list = [(today + dt.timedelta(days=30 * i)).strftime("%Y-%m") for i in range(months_to_get)]

# total API calls = 3 (number of months) x 3 (cities) = 9 API CALLS per code run
# Only have 100 API call / month


flight_dict = {}
for data in data_sheety['prices']:
    origin = "MNL"
    destination = data["iataCode"]
    flight_dict[destination] = {year_month: flight_search.search_flights(year_month, origin, destination)
                                for year_month in month_list}

print(flight_dict)

# TODO 3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS
#  (or WhatsApp Message) to your own number using the Twilio API.
#  The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates.

flight_data = FlightData(flight_dict)
flight_data_df = flight_data.get_flight_df()
sheety_df = pd.DataFrame(data_sheety['prices'],
                         index=None).drop(columns=['id'])

# join flight_data and sheety_data
flight_sheety_df = flight_data_df.set_index('iataCode').join(sheety_df.set_index('iataCode'))

for (index, row) in flight_sheety_df.iterrows():
    if row.price <= row.lowestPrice:
        notification_manager.send_notif(city=row.city,
                                        origin=row.originAirport,
                                        destination=row.destinationAirport,
                                        departure_date=row.localDepartureDate,
                                        price=row.price)
