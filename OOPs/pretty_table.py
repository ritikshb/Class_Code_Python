from prettytable import PrettyTable
my_pretty = PrettyTable()
print(my_pretty)
my_pretty.add_column("Pokemon Name",["Pikachu","Squirtle","Charmandor"])
my_pretty.add_column("Type",["Electric","Water","Fire"])
my_pretty.align ='l'
print(my_pretty)