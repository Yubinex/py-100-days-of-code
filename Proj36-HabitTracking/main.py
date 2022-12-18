import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
# graph link:
# https://pixe.la/v1/users/yubinex/graphs/graph1.html

USERNAME = "yubinex"
with open(file="Proj36-HabitTracking/token.txt") as token_file:
    TOKEN = token_file.read()
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user account (one time thing)
""" response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text) """

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "h",
    "type": "int",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# create new graph
""" response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text) """

GRAPH_ID = "graph1"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

# add pixel to graph
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ").strip(),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4",
}

""" response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text) """

# delete pixel
delete_endpoint = update_endpoint

""" response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text) """
