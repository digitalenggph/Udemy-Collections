import os, json
import pandas as pd
import numpy as np
from custom_pd_display import *
from datetime import datetime, timedelta

# goal: put timestamp to points
bus_schedule_conso = os.getenv("BUS_SCHEDULE_CONSO")
schedule_df = pd.read_csv(bus_schedule_conso)
print(schedule_df.columns)
print(schedule_df.head())
exit()

# points along route is every meter
csv_source = os.getenv("POINT_SOURCE")
csv_source_df = pd.read_csv(csv_source)

# sort by direction and distance
csv_source_df.sort_values(["direction", "distance"], inplace=True)
print(csv_source_df.head())
print(csv_source_df.columns)

# set arbitrary details for the timestamp
arbitrary_date = datetime(2025, 1, 24)
arbitrary_speed = 5.55 #m/s or ~20 kph
time_to_add = 1 / arbitrary_speed  # add a certain time per meter -> the distance of each points
load_unload_time = 5 * 60 # 5 minutes -> seconds

# add 5 minutes for loading and unloading in each station
csv_source_df["timedelta"] = csv_source_df.apply(lambda x: time_to_add if pd.isna(x["station"])
                                                 else time_to_add + load_unload_time,
                                                 axis=1)

csv_source_df["cum_time"] = csv_source_df.groupby("direction")["timedelta"].cumsum()
csv_source_df["timestamp"] = csv_source_df.apply(lambda x: arbitrary_date + timedelta(seconds=x["cum_time"]), axis=1)

# create illusion of bus staying in place
bus_at_station = csv_source_df[~csv_source_df.station.isna()] #filters points for station


for idx, row in bus_at_station.iterrows():
    for delta_time in np.linspace(0, load_unload_time, 1000): # 300 seconds/1000
        new_row = row.copy()
        new_row.station = "temp"
        new_row.timestamp = new_row.timestamp - timedelta(seconds=delta_time)
        temp_df = pd.DataFrame([new_row])
        csv_source_df = pd.concat([csv_source_df, temp_df], ignore_index=True)


print(csv_source_df[csv_source_df["direction"]=="southbound"].sort_values(by='distance')[["timedelta", "station", "timestamp"]].head(20))
print(csv_source_df[csv_source_df["direction"]=="southbound"].sort_values(by='distance')[["distance", "timedelta", "station", "timestamp"]].tail(20))

# save csv
POINT_DESTINATION_DIR = os.getenv("POINT_DESTINATION")
destination_path = os.path.join(POINT_DESTINATION_DIR, "bus_schedule.csv")
# csv_source_df.to_csv(destination_path, index=False)













