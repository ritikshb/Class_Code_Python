# from amadeus import Client

    # amadeus = Client(client_id ="jub0zhltdUTqolgj1niszBNCfn9VbAVD",
    #                 client_secret ="tzuNluyYhpAwpt7Z")
    # response = amadeus.shopping.flight_offers_search.get(originLocationCode = 'MAD',
    #                                         destinationLocationCode="ATH",
    #                                         departureDate =today.date(),
    #                                         adults = 1)
    # print(response.data)







from datetime import datetime
import requests
from data_manager import DataManager

#This class is responsible for structuring the flight data.

class FlightData():
    def __init__(self):
        self.data_location = DataManager()
        self.today = datetime.now()
    