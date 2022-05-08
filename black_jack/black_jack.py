import random
card_deck = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
user = []
dealer = []
sum_user = 0
dealer_sum = 0
for i in range(2):
    user.append(random.choice(card_deck))
    sum_user += user[i]
    dealer.append(random.choice(card_deck))
    dealer_sum += dealer[i]
print(f'Dealer hand 1 card is {dealer[0]}')
print(f"Your both cards {user} and cards sum is: {sum_user}")
true_false = True
user_card_number = 2
dealer_card_number = 2
user_input = input("You want to hit or stand: type 'hit' for hit and 'stand' for stand: ").lower()
while true_false:
    if user_input == 'hit':
        user.append(random.choice(card_deck))
        sum_user += user[user_card_number]
        user_card_number +=1
        if sum_user > 21:
            print(f"Because you hit and your score is greater then 21 you loss your cards are {user} and sum {sum_user}")
            break
        user_input = input(f"your card are {user} and sum is {sum_user} You want to hit or stand: type 'hit' for hit and 'stand' for stand: ").lower()
        if user_input == 'hit':
            true_false = True
    if sum_user >21:
        print(f"You hit {user[user_card_number-1]} and because of this You Loss because your card_sum is greater then 21 : {sum_user}")
        true_false = False
        # exit()
    else:
        true_false = False
    print(f"your cards {user} and sum: {sum_user} ")
its_false = True
if sum_user <= 21:
    while its_false:
        if dealer_sum < 17:
            dealer.append(random.choice(card_deck))
            dealer_sum += dealer[dealer_card_number]
            print(f"dealer_hit {dealer} cards and sum is: ", end=' ')
            print(f"{dealer_sum}")
            dealer_card_number += 1
        else:
            its_false = False
        if dealer_sum > 21:
            its_false = False
            print(f"dealer loss {dealer_sum}")
    if dealer_sum <= 21 and dealer_sum > sum_user and sum_user < 21:
        print(f"dealer win {dealer_sum} > {sum_user}")
    elif sum_user <= 21 and sum_user>dealer_sum and dealer_sum <21:
        print(f'user_win {sum_user} > {dealer_sum}')
    elif sum_user <= 21 and dealer_sum <=21 and sum_user == dealer_sum:
        print(f"Draw {sum_user} = {dealer_sum}")