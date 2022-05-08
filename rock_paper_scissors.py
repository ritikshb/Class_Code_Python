import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
map = [rock,paper,scissors]
choose = int(input("1 for rock,2 for paper,3 for scissors choose only one of them"))
computer_random_choice = random.choice(map)
# print(map[choose-1])
# print(computer_random_choice)
if choose > 3:
    print("wrong number typed")
elif computer_random_choice == map[choose-1]:
    print(f"user choice: \n{map[choose-1]}\ncomputer choice: \n{computer_random_choice}\nyou won")
else:
    print(f"{map[choose-1]}\n{computer_random_choice}\nyou loss")
# if choose == 1 and computer_random_choice == 1:
#     print(f"{rock}\n{paper}\nyou loss")
# elif choose == 1 and computer_random_choice == 2:
#     print(f"{rock}\n{scissors}\nyou won")
# elif choose == 2 and computer_random_choice == 0:
#     print(f"{paper}\n{computer_random_choice}\nyou won")
# elif choose == 2 and computer_random_choice == 2:
#     print(f"{paper}\n{computer_random_choice}\nyou loss")
# elif choose == 3 and computer_random_choice == 0:
#    print(f"{scissors}\n{computer_random_choice}\nyou loss")
# elif choose == 3 and computer_random_choice == 1:
#     print(f"{scissors}\n{computer_random_choice}\nyou won")
# else:
#     print("Draw")
