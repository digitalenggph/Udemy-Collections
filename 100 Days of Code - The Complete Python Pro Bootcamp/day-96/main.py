import requests, json

URL = "https://earthquake.usgs.gov/fdsnws/event/1/"

params = {
    "method": "query",
    "format": "geojson",
    "starttime": "2025-08-01",
    "endtime": "2025-08-06"
}

if __name__ == "__main__":
    response = requests.get(url=URL, params=params)
    data = response.json()
    features = data["features"]

    with open('earthquakes.json', 'w') as file:
        json.dump(features, file, indent=4)

