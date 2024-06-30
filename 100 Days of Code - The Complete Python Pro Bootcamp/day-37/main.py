import requests
import datetime as dt

# ---------------------------CREATE ACCOUNT---------------------------#
URL = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = ""

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=URL, json=user_params)
# print(response.text)
# --------------------------------------------------------------------#


# ----------------------------CREATE GRAPH----------------------------#
URL_GRAPH = f"{URL}/{USERNAME}/graphs"
GRAPH_NAME = "graph1"

graph_params = {
    "id": GRAPH_NAME,
    "name": "Baby Muscles Graph",
    "unit": "mins",
    "type": "int",
    "color": "momiji"
}

# graph_response = requests.post(url=URL_GRAPH, json=graph_params, headers=headers)
# print(graph_response.text)
# --------------------------------------------------------------------#


# ----------------------------CREATE PIXEL----------------------------#
URL_ADD_PIXEL = f"{URL}/{USERNAME}/graphs/{GRAPH_NAME}"
today = dt.datetime.now().strftime("%Y%m%d")

add_pixel_params = {
    "date": today,
    "quantity": "10",
}

# add_pixel_response = requests.post(url=URL_ADD_PIXEL, json=add_pixel_params, headers=headers)
# print(add_pixel_response.text)
# --------------------------------------------------------------------#


# ----------------------------UPDATE PIXEL----------------------------#
date_to_update = "20240526"
URL_UPDATE_PIXEL = f"{URL}/{USERNAME}/graphs/{GRAPH_NAME}/{date_to_update}"

update_pixel_params = {
    "quantity": "20"
}

# update_pixel_response = requests.put(url=URL_UPDATE_PIXEL, json=update_pixel_params, headers=headers)
# print(update_pixel_response.text)
# --------------------------------------------------------------------#


# ----------------------------DELETE PIXEL----------------------------#
date_to_delete = "20240526"
URL_DELETE_PIXEL = f"{URL}/{USERNAME}/graphs/{GRAPH_NAME}/{date_to_delete}"

delete_pixel_response = requests.delete(url=URL_UPDATE_PIXEL, headers=headers)
print(delete_pixel_response.text)
# --------------------------------------------------------------------#
