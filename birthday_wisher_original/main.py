import pandas as pd
from datetime import datetime
import smtplib
NAME = "[NAME]"

##################### my side code ######################

my_email = "ritiksharmapy@gmail.com"
my_password = "Ritik*/12"
# data = pd.read_csv("birthday_wisher_original\\birthdays.csv")
# my_name = data["name"][0]
# # print(my_name)
# today = dt.datetime.now()
# if today.month == 2 and today.day == 14:
#     with open("birthday_wisher_original\\letter_templates\\letter_1.txt",'r') as file:
#         file_data = file.read()
#         new_file = file_data.replace(NAME,my_name)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(password=my_password,user=my_email)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="ritiksharmapy@outlook.com",
#                             msg=f"Subject: Happy Birthday \n\n{new_file}")

today = datetime.now()
today_tuple = (today.month,today.day)
data = pd.read_csv("birthday_wisher_original\\birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = "birthday_wisher_original\\letter_templates\\letter_1.txt"
    with open(file=file_path) as file:
        content = file.read()
        wish_content = content.replace(NAME,birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(password=my_password,user=my_email)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ritiksharmapy@outlook.com",
                            msg=f"Subject: Happy Birthday \n\n{wish_content}")