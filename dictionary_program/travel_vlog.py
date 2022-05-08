travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country,visit,cities):
    travel_dict = {"country" : country,
                   "visits": visit,
                   "cities": cities
                   }
    travel_log.append(travel_dict)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



