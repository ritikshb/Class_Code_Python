import random
from art import logo,vs
from game_date import data
from random import choice
a = choice(data)
b = choice(data)
# print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
# print(a)
score = 0
def higher_lower(a,b):
    global score
    print(logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    input_user= input("Who has more followers? Type 'A' or 'B'").upper()
    if (input_user == 'A' and a['follower_count'] > b['follower_count']) or (input_user == 'B' and b['follower_count'] > a['follower_count']):
        score +=1
        print(f"\nYou are right: Current Score: {score}")
        a = b
        b = choice(data)
        higher_lower(a,b)
    else:
        print(f"sorry that's wrong. Final score: {score}")   
higher_lower(a,b)
