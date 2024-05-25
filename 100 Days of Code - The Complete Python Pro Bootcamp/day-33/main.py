import requests

# get the endpoint
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=url)
response.raise_for_status()

data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (float(latitude), float(longitude))
print(iss_position)
