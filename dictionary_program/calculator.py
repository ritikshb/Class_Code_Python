logo = """
 _____________________
|  _________________  |
| | calculator   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def addition(n1,n2):
  return n1+n2
def substraction(n1,n2):
  return n1-n2
def multiplication(n1,n2):
  return n1*n2
def division(n1,n2):
  if n2 == 0:
    return "second number can't be 0 in division "
  return n1/n2
cal_dict = {"+": addition,"-": substraction, "*": multiplication, "/": division}
def calculator():
  print(logo)
  num1 = float(input("Whats the first number: "))
  calculated_value =0
  for operater in cal_dict:
    print(operater)
  user_input = True
  while user_input:
    operation_symbol = input("pick an operation from the line above")
    num2 = float(input("Whats the next number: "))
    calculation_method = cal_dict[operation_symbol]
    calculated_value = calculation_method(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {calculated_value}")
    user = input(f"Type 'y' to continue claculating with {calculated_value}, or type 'n' to exit: ").lower()
    if user == 'y':
      num1 = calculated_value
    else:
      user_input = False
      calculator()
calculator()