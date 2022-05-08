from email import message
from inspect import Parameter
# import smtplib
import requests
from twilio.rest import Client


account_sid = "ACe3a61223f7f65919225612bf059e8107"
auth_token = "2a2fee8b1bfa9eaf63ea6edbf63c72c6"
api_key = "fcf47668d356f33abdac1728efcb13e1"
lat = 51.5073219
lon = -0.1276474
email = "ritiksharmapy@gmail.com"
password = "Ritik*/12"
parameter = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
api_data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameter)
api_data.raise_for_status()
weather_data = api_data.json()

# weather_id = []
# for i in range(12):
#     weather = weather_data['hourly'][i]['weather']
#     weather_id.append(weather[0]['id'])
# for id in weather_id:
#     if(id<700):
#         print("bring umbrella")
#         break

####OR
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
                              body="I's going rain today. Remember to bring umberala",
                              from_='+18596597910',
                              to='+91 91190 59393'
                          ) 
    print(message.status)
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=email,password=password)
    #     connection.sendmail(from_addr=email,
    #                         to_addrs="ritiksharmapy@outlook.com",
    #                         msg="Subject: Rain information \n\nbring Umbrella")

