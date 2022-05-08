from matplotlib.style import use
import requests
from datetime import datetime
import smtplib
LAN =51.507351
LON = -0.127758 
MY_PASSSWORD = "Ritik*/12"
MY_EMAIL = "ritiksharmapy@gmail.com"
# print(iss_position)
def position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    # iss_position = (longitude,latitude)
    if (LAN-5 <= latitude <= LAN+5)  or (LON-5 <= longitude <= LON+5) :
        return True


def check_night():
    parameters = {
        "lat": LAN,
        "lng": LON,
        "formatted" : 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(':')[0])
    # print(sunrise,sunset)
    today = datetime.now()
    today_hour = today.hour 
    if today_hour<= sunrise and today_hour>=sunset:
        return True
if check_night() and position():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="ritiksharmapy@outlook.com",
                            msg="Subject: LOOK UP \n\nThe ISS is above you in the sky")