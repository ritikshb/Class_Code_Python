a = range(1,5)
new_list = [range_number*2 for range_number in a]
names = ['Alex','Beth','Caroline','Dave','Elanor','Freddie']
large_name = [name.upper() for name in names if len(name) >4]

print(large_name)