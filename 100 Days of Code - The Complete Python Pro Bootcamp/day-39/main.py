from flight_search import FlightSearch
from data_manager import DataManager

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# TODO 1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
#  International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet
#  include multiple airports, you want the city code (not the airport code see here).

flight_search = FlightSearch()
data_manager = DataManager()

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



# TODO 3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS
#  (or WhatsApp Message) to your own number using the Twilio API.

# TODO 4.The SMS should include the departure airport IATA code, destination airport IATA code,
#  flight price and flight dates.
