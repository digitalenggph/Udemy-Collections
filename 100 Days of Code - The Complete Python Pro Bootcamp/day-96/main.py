import requests, json
import folium
from folium.plugins import MarkerCluster
import webbrowser
from datetime import datetime as dt
from datetime import timezone, timedelta
import time

URL = "https://earthquake.usgs.gov/fdsnws/event/1/"

def auto_save_then_open(map_to_save, map_path):
    map_to_save.save(map_path)
    # open in browser.
    new = 2
    webbrowser.open(map_path, new=new)

def assign_magnitude_classes(input_magnitude):
    if input_magnitude <= 3.9:
        return "Minor"
    elif 3.9 < input_magnitude <= 4.9:
        return "Light"
    elif 4.9 < input_magnitude <= 5.9:
        return "Moderate"
    elif 5.9 < input_magnitude <= 6.9:
        return "Strong"
    elif 6.9 < input_magnitude <= 7.9:
        return "Major"
    elif 7.9 < input_magnitude:
        return "Great"
    else:
        return "Unknown"


if __name__ == "__main__":
    # epoch
    epoch_now_utc = dt.now(timezone.utc).timestamp()
    epoch_yesterday_utc = (dt.now(timezone.utc) - timedelta(days=1)).timestamp()

    # date
    date_now_utc = dt.fromtimestamp(epoch_now_utc).strftime('%Y-%m-%d')
    date_yesterday_utc = dt.fromtimestamp(epoch_yesterday_utc).strftime('%Y-%m-%d')

    params = {
        "method": "query",
        "format": "geojson",
        "starttime": date_yesterday_utc,
        "endtime": date_now_utc,
    }

    response = requests.get(url=URL, params=params)
    data = response.json()
    features = data["features"]

    m = folium.Map([0, 0], zoom_start=2, tiles="cartodb positron")
    marker_cluster = MarkerCluster().add_to(m)

    for feature in features:
        # timestamp processing
        epoch_timestamp = feature["properties"]["time"] # in UTC epoch
        dt_timestamp = dt.fromtimestamp(epoch_timestamp / 1000) # convert milliseconds to seconds

        # coordinates
        coordinates = feature["geometry"]["coordinates"]

        # for popup
        title = feature["properties"]["title"]
        magnitude = feature["properties"]["mag"]
        timestamp_date = dt_timestamp.strftime('%Y-%m-%d')
        timestamp_time = dt_timestamp.strftime('%H:%M:%S')

        iframe = folium.IFrame(title + "<br>"
                                + "date: " + str(timestamp_date) + "<br>"
                                + "time: " + str(timestamp_time)
                )

        popup = folium.Popup(iframe, min_width=150, max_width=250)

        folium.Marker(
            location=(coordinates[1], coordinates[0]),
            popup=popup
        ).add_to(marker_cluster)

        # m.add_child(
        #     folium.Marker(
        #         location=(coordinates[1], coordinates[0]),
        #         popup=popup
        #     ).add_to(marker_cluster)
        # )

        print(title)

    auto_save_then_open(map_to_save=m, map_path="map.html")
    print("done")
    print(time.process_time())


    # with open('earthquakes.json', 'w') as file:
    #     json.dump(features, file, indent=4)

