from tokenize import Token
import requests
from datetime import datetime

pixela_endPoint = "https://pixe.la/v1/users"

TOKEN = "dascvfebhjsaw"
USERNAME = "shritik"
GRAPH_ID = "mygraph"

#####Create User Account
user_pram = {
    "token":Token,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endPoint,json=user_pram)
# print(response.text)
###----------------------------------###########

###Create Graph
graph_endpoint = f"{pixela_endPoint}/{USERNAME}/graphs"
graph_config = {
    "id" : GRAPH_ID,
    "name":"Track Daily Learning",
    "Unit": "Hr",
    "Type": "float",
    "color" : "momiji"
}
header = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(response.text)

###Create Pixel in graph_____#####

today = datetime.now()
print(today)

pixel_endpoint = f"{pixela_endPoint }/{USERNAME}/graphs/{GRAPH_ID}"
pixel_body = {
    "date":"20220221",
    "quantity": "6",
}
# response = requests.post(url=pixel_endpoint,json=pixel_body,headers=header)
# print(response.text)