import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
   def flight_apiWork(self):
        kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
        city_code = self.data_location.choose_data()[0]
        kiwi_para ={
            
            "fly_from": city_code,
            "date_from": "26/02/2022",
            "data_to": "28/02/2022",
            "limit":2
        }
        header ={
            "apikey": "rL7GHxPuPEBPev0Q2V4E9qzWADazg96r",
        }
        response = requests.get(url=kiwi_endpoint,params=kiwi_para,headers=header)
        response_json = response.json()
        city_from = response_json['data'][0]["cityFrom"]
        city_to = response_json['data'][0]["cityTo"]
        price = response_json['data'][0]["price"]
        print(city_from,city_to,price)