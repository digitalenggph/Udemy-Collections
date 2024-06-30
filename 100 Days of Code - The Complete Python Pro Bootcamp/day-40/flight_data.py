import pandas as pd


class FlightData:
    def __init__(self, flight_data_json: dict):
        self.json = flight_data_json
        self.get_flight_df()

    def get_iata(self):
        iata_list = [key for key in self.json]
        return iata_list

    def get_flight_df(self):
        flight_data_df = [
            [iata, year_mon,
             flight['content']['outboundLeg']['localDepartureDate'],  # departureDate
             flight['content']['outboundLeg']['originAirport']['name'],  # originAirport
             flight['content']['outboundLeg']['destinationAirport']['name'],  # destinationAirport
             flight['content']['rawPrice']]  # price

            for iata in self.get_iata()  # first level
            for year_mon in self.json[iata]  # second level
            for flight in self.json[iata][year_mon]['data']['flightQuotes']['results']  # fifth level
        ]

        df = pd.DataFrame(flight_data_df)
        df.columns = ['iataCode', 'yearMon', 'localDepartureDate', 'originAirport', 'destinationAirport', 'price']

        return df
