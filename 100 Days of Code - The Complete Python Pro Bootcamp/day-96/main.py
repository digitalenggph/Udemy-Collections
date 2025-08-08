import requests, json
import folium
import webbrowser

URL = "https://earthquake.usgs.gov/fdsnws/event/1/"

params = {
    "method": "query",
    "format": "geojson",
    "starttime": "2025-08-05",
    "endtime": "2025-08-06"
}


def auto_save_then_open(map_to_save, map_path):
    map_to_save.save(map_path)
    # open in browser.
    new = 2
    webbrowser.open(map_path, new=new)

if __name__ == "__main__":
    response = requests.get(url=URL, params=params)
    data = response.json()
    features = data["features"]

    m = folium.Map([52.5, 2], zoom_start=5)
    for feature in features:
        title = feature["properties"]["title"]
        timestamp = feature["properties"]["time"]
        coordinates = feature["geometry"]["coordinates"]


        m.add_child(
            folium.Marker(
                location=(coordinates[1], coordinates[0])
            )
        )

        print(title)

    auto_save_then_open(map_to_save=m, map_path="map.html")
    print("done")







    # with open('earthquakes.json', 'w') as file:
    #     json.dump(features, file, indent=4)

