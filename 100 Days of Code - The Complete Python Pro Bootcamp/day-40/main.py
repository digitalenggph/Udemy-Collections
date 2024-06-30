import pandas as pd

from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

import datetime as dt

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()


data_sheety = data_manager.get_data()
print(data_sheety)

for data in data_sheety:
    city = data["city"]
    iata_code = data["iataCode"]
    if len(iata_code) == 0:
        iata = flight_search.iata_code(city)
        row_num = data_sheety.index(data) + 2
        data_manager.update_row_iata(row_num, iata)


today = dt.datetime.now()
today_year_mon = today.strftime("%Y-%m")

months_to_get = 3
month_list = [(today + dt.timedelta(days=30 * i)).strftime("%Y-%m") for i in range(months_to_get)]

flight_dict = {}
for data in data_sheety:
    origin = "MNL"
    destination = data["iataCode"]
    flight_dict[destination] = {year_month: flight_search.search_flights(year_month, origin, destination)
                                for year_month in month_list}
    print(flight_dict[destination])

print(flight_dict)


flight_data = FlightData(flight_dict)
flight_data_df = flight_data.get_flight_df()
sheety_df = pd.DataFrame(data_sheety, index=None).drop(columns=['id'])

# join flight_data and sheety_data
flight_sheety_df = flight_data_df.set_index('iataCode').join(sheety_df.set_index('iataCode'))

users_sheety = data_manager.get_users()

for (index, row) in flight_sheety_df.iterrows():
    if row.price <= row.lowestPrice:
        notification_manager.send_notif(city=row.city,
                                        origin=row.originAirport,
                                        destination=row.destinationAirport,
                                        departure_date=row.localDepartureDate,
                                        price=row.price)
        for user in users_sheety:
            firstname = user['firstName']
            lastname = user['lastName']
            email = user['email']
            notification_manager.send_email(firstname, lastname, email,
                                            row.city, row.originAirport, row.destinationAirport,
                                            row.localDepartureDate, row.price)
