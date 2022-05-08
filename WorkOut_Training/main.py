import requests
from datetime import datetime

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = "388b0e61fb8186ab3bbcb97730fd5951"
API_ID = "ad7b929a"

sheety_endpoint = "https://api.sheety.co/c911bad4699b31b6cae3927ce528697a/myWorkouts/workouts"


exercise_query = input("Tell me which exercise you did: ")
exercise_params = {
    "query" : exercise_query,
    "gender": "male",
    "age": 21
}
header = {
    "x-app-id" :API_ID,
    "x-app-key": API_KEY,
}
today = datetime.now()
today_formate = today.strftime('%d/%m/%y')
today_time = today.time().strftime("%X")
# print(today_time)

response = requests.post(url=exercise_endpoint,json=exercise_params,headers=header)
response_data = response.json()
user_exercise = response_data["exercises"][0]["user_input"].title()
user_exercise_duration = response_data["exercises"][0]["duration_min"]
user_calories = response_data["exercises"][0]["nf_calories"]
# print(response_data)
# print(user_calories)
sheety_body = {
    "workout":{
        "date" : today_formate,
        "time" : today_time,
        "exercise" : user_exercise,
        "duration": user_exercise_duration,
        "calories": user_calories
    }
}
header = {
    "Authorization": "Bearer akshaueyrsnabsgrhusa"
}
sheets_response = requests.post(url=sheety_endpoint,json=sheety_body,headers=header)
print(sheets_response.text)