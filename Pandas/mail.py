import pandas as pd
# with open('Pandas_CSV_FILES\weather_data.csv','r') as wather_data:
#     wather_list = wather_data.readlines()
#     print(wather_list)
# import csv
# with open('Pandas_CSV_FILES\weather_data.csv','r') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row_data in data:
#         if(row_data[1] != 'temp'):
#             temperature.append(int(row_data[1]))
#     print(temperature)

# data = pd.read_csv('Pandas_CSV_FILES\weather_data.csv')
# print(data['condition'])
# data_row = data['temp'].to_list()
# avg_temp = sum(data_row)/len(data_row)
# print(avg_temp)
# print(data['temp'].max())
# print(data['temp'].mean())
# print(data.condition)
# print(data[data.day == 'Wednesday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# temp_monday = (monday.temp * (9/5))+32
# print(temp_monday)
#Create dataframe from Scratch
# data_dict = {
#     "student" : ['Amy','James','Ritik'],
#     "scores" :  [50,32,80]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv('Pandas\\new_dict_file.csv')
data = pd.read_csv('Pandas\Squirrel_Data.csv')
gray_color_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_color_count = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_color_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# count_Gray = 0
# count_Black = 0
# count_Cinnamon = 0
# for i in colors:
#     if i == 'Gray':
#         count_Gray += 1
#     elif i == 'Black':
#         count_Black += 1
#     elif i == 'Cinnamon':
#         count_Cinnamon += 1
colors_data = {
    'Fur COlor' : ['grey','red','black'],
    'Count':[gray_color_count,cinnamon_color_count,black_color_count]
}
colors_dataframe = pd.DataFrame(colors_data)
colors_dataframe.to_csv('Pandas\squirrel_color_count.csv')
# print(data[data['Primary Fur Color'] == 'Gray'])
# print(colors.Gray == 'Gray')