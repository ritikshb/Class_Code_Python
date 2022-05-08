list1 = ['a','b','c']
list2 = ['d','e','f']
list3 = ['g','h','i']
aa = [list1,list2,list3]
partition = input("Which position do you want to change")
column = int(partition[0])
row = int(partition[1])
aa[row-1][column-1] = "X"
print(f"{list1}\n{list2}\n{list3}")