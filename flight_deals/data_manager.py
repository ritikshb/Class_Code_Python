import requests
import random


class DataManager(object):
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/c911bad4699b31b6cae3927ce528697a/flightDeals/prices"
        self.response = requests.get(url=self.sheety_endpoint)
        # self.choose_data()
        # print(self.response.json())
    def choose_data(self):
        self.json_data = self.response.json()
        data_list = self.json_data["prices"]
        random_data = random.choice(data_list)
        self.city_code = random_data['iataCode']
        self.lowest_price = random_data["lowestPrice"]
        print(self.city_code,self.lowest_price)
        return (self.city_code,self.lowest_price)
