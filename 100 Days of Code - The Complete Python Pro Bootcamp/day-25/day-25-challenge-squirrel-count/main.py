import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
output_data = data.groupby('Primary Fur Color')['Primary Fur Color'].count()

# create column names
columns = ['COUNT']

# create dataframe from output_data
output_data_df = pd.DataFrame(output_data)
output_data_df.columns = columns

# sets index column as a separate column
df = output_data_df.reset_index()

# saves new csv file from df
df.to_csv("squirrel_count.csv")

"""
SOURCE:
https://stackoverflow.com/questions/56360610/sum-column-based-on-another-column-in-pandas-dataframe
"""
