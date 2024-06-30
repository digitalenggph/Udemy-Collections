# needs cleaning

# with open("weather_data.csv", mode='r') as weather_data:
#     data = weather_data.readlines()

"""
# Using CSV
import csv

with open("weather_data.csv") as data_file:
    # reads the csv
    data = csv.reader(data_file)

    # skips the header source: https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a
    # -csv-file-using-python
    next(data, None)

    # creates empty list for the temperature
    temperatures = []

    for row in data:
        # index 1 contains the temperature
        temperature = float(row[1])
        temperatures.append(temperature)

    print(temperatures)

"""

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])

