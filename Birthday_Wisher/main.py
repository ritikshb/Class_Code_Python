import smtplib
import datetime as dt
import random

# my_email = "ritiksharmapy@gmail.com"
# my_password = "Ritik*/12"
# # connection = smtplib.SMTP("smtp.gmail.com")
# # connection.starttls()
# # connection.login(user=my_email,password=my_password)
# # connection.sendmail(from_addr=my_email,to_addrs="ritiksharmapy@outlook.com",msg="Subject: My first Mail\n\n Hello")
# # connection.close()
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=my_password)
#     connection.sendmail(from_addr=my_email,to_addrs="ritiksharmapy@outlook.com",msg="Subject: My Second Mail\n\n Hello")

# now = dt.datetime.now()
# year = now.year
# month = now.month
# weekday1 = now.weekday()
# my_birth_day = dt.datetime(year=2001,month=6,day=9)
# print(weekday1)

# ### open text file--------------------------####
# with open("Birthday_Wisher\\quotes1.txt",'r',encoding='utf-8') as file:
#     read_data = file.readlines()
#     random_quotes = random.choice(read_data).strip('\n').encode('ascii','ignore')
#     random_quotes =random_quotes.decode("utf-8","ignore")
#     # print(random_quotes)
#     # string_name = ""
#     # string_name = ("".join(random_quotes)).encode('utf-8')


# ######----------current date
# current_date = dt.datetime.now()
# current_day = current_date.weekday()

# # send quotes to mail
# my_email = "ritiksharmapy@gmail.com"
# my_password = "Ritik*/12"
# # with smtplib.SMTP("smtp.gmail.com") as connection:
# #     connection.starttls()
# #     connection.login(password=my_password,user=my_email)
# #     connection.sendmail(from_addr=my_email,to_addrs='ritiksharmapy.outlook.com',msg=f"Subject: Today Quote \n\n{random_quotes}")
# if current_day == 0:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email,password=my_password)
#         connection.sendmail(from_addr=my_email,
#         to_addrs="ritiksharmapy@outlook.com",
#         msg=f"Subject: Today Quote \n\n{random_quotes}")