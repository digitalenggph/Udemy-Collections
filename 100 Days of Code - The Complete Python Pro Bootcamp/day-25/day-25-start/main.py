"""
DAY-25-NOTES:

Pandas
    * automatically omits first row and set it as a header
    * documentation: https://pandas.pydata.org/docs/

Series vs. Dataframe
    * Dataframe -> Table (2-dimensional)
    * Series -> Column (1-dimensional) / list

"""


import pandas as pd

data = pd.read_csv("weather_data.csv")

# type check
print("data_type: ", type(data))
print('data["temp"]: \n', data["temp"])

# convert dataframe to dict
data_dict = data.to_dict()
print("data_dict: ", data_dict)

# convert series to list
temp_list = data["temp"].to_list()
print("temp_list: ", temp_list)

# get average temperature
ave_temp = round(sum(temp_list)/len(temp_list), 2)
print("average temperature = ", ave_temp)

# OR

ave_temp_mean = round(data["temp"].mean(), 2)
print("average temperature = ", ave_temp_mean)

# get maximum temperature
max_temp = data["temp"].max()
print("maximum temperature = ", max_temp)

# get data in columns
print(data["condition"])

# OR

print(data.condition)

# get data in rows
print(data[data.day == "Monday"])

# get data in rows with maximum temperature
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)

# Monday temperature to Fahrenheit
print(monday.temp * (9/5) + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
    }

data_dict_df = pd.DataFrame(data_dict)
data_dict_df.to_csv("new_data.csv")


