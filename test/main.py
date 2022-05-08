import pandas as pd
data = pd.read_csv('test\weather_data.csv')
monday = data[data.day == "Monday"]
print(monday)
# temp_monday = (monday.temp * (9/5))+32
# print(temp_monday)