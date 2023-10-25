import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = "magda8662"
TOKEN = os.getenv('TOKEN')
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATE NEW USER ACCOUNT
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# CREATE NEW GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.today()

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many kilometers did you walk today? "),
}

# CREATE NEW PIXEL IN GRAPH (FOR TODAY)
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity": input("How many kilometers did you walk today? ")
}

# EDIT VALUE OF TODAY'S PIXEL
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

# DELETE VALUE OF TODAY'S PIXEL
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
