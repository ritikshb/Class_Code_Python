from re import T


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# coins = {
#     'quarters': 0.25,
#     'dimes': 0.10,
#     'nickles': 0.05,
#     'pennis': 0.01
# }
#print report
def resources_left():
    for key,value in resources.items():
        print(f"{key}: {value}")

#check resources
def menu_selection():
    global coffee_menu
    coffee_type = MENU[coffee_menu]
    ingredients = coffee_type['ingredients']
    water_need = ingredients["water"]
    coffee_need = ingredients["coffee"]
    milk_need = 0
    if coffee_menu == 'latte' or coffee_menu =='cappuccino':
        milk_need = ingredients["milk"]
    if water_need > resources["water"]:
        print("Sorry not enough water")
        return 0
    elif coffee_need > resources['coffee']:
        print("Sorry not enough coffee")
        return 0
    elif milk_need > resources['milk']:
        print("Sorry not enough milk")
        return 0
    resources['water'] -= water_need
    resources['milk'] -= milk_need
    resources['coffee'] -= coffee_need
    return coffee_type['cost']
def money_input():
    quarters = int(input("how many quarters: ")) *0.25
    dimes = int(input("how many dimes: ")) *0.10
    nickles = int(input("how many nickles: ")) *0.05
    pennis = int(input("how many pennis: ")) *0.01
    sum = quarters+dimes+nickles+pennis
    return sum
def transection_money(money_collected,money_coffee):
    global coffee_menu
    if money_collected < money_coffee:
        print("Sorry that's not enough money")
        return False
    elif money_coffee <= money_collected:
        remaining_cost = money_collected -money_coffee
        print(f"Here is ${remaining_cost} in change")
        print(f"Here is your {coffee_menu} ☕ Enjoy!")
        return True
its_true = True
while its_true:
    coffee_menu = input("What would you like? (espresso/latte/cappuccino) and also you can see 'report' left: ").lower()
    if coffee_menu == 'report':
        resources_left()
    else:
        need_money = menu_selection()
        if need_money == 0:
            break
        collected_money = money_input()
        its_true = transection_money(collected_money,need_money)
        
    
# its_true = True
# while its_true:
#     coffee_menu = input("What would you like? (espresso/latte/cappuccino) and also you can see 'resources' left: ").lower()
#     if coffee_menu == 'resources':
#         resources_left()
#     else:
#         coffee_type = MENU[coffee_menu]
#         ingredients = coffee_type['ingredients']
#         water_need = ingredients["water"]
#         coffee_need = ingredients["coffee"]
#         milk_need = 0
#         if coffee_menu == 'latte' or coffee_menu =='cappuccino':
#             milk_need = ingredients["milk"]
#         if water_need > resources["water"]:
#             print("Sorry not enough water")
#             its_true = False
#             break
#         elif coffee_need > resources['coffee']:
#             print("Sorry not enough coffee")
#             its_true = False
#             break
#         elif milk_need > resources['milk']:
#             print("Sorry not enough milk")
#             its_true = False
#             break
#         print("please insert coins.")
#         quarters = int(input("how many quarters: "))
#         dimes = int(input("how many dimes: "))
#         nickles = int(input("how many nickles: "))
#         pennis = int(input("how many pennis: "))
#         calculation = coins['quarters']*quarters + coins['dimes']*dimes + coins['nickles']*nickles + coins["pennis"]*pennis
#         if calculation < coffee_type['cost']:
#             print("Sorry that's not enough money")
#             its_true = False
#             break
#         elif coffee_type['cost'] <= calculation:
#             remaining_cost = calculation -coffee_type['cost']
#             print(f"Here is ${remaining_cost} in change")
#             print(f"Here is your {coffee_menu} ☕ Enjoy!")
#         resources['water'] -= water_need
#         resources['milk'] -= milk_need
#         resources['coffee'] -= coffee_need