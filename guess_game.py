import random
print("""
      o__ __o                                                             o__ __o                                               
     /v     v\                                                           /v     v\                                              
    />       <\                                                         />       <\                                             
  o/                o       o     o__  __o       __o__    __o__       o/                 o__ __o/  \o__ __o__ __o     o__  __o  
 <|       _\__o__  <|>     <|>   /v      |>     />  \    />  \       <|       _\__o__   /v     |    |     |     |>   /v      |> 
  \\          |    < >     < >  />      //      \o       \o           \\          |    />     / \  / \   / \   / \  />      //  
    \         /     |       |   \o    o/         v\       v\            \         /    \      \o/  \o/   \o/   \o/  \o    o/    
     o       o      o       o    v\  /v __o       <\       <\            o       o      o      |    |     |     |    v\  /v __o 
     <\__ __/>      <\__ __/>     <\/> __/>  _\o__</  _\o__</            <\__ __/>      <\__  / \  / \   / \   / \    <\/> __/> 
""")
selected_number = random.randint(1,100)
# def calculate(first_number,last_number):
#     return first_number+last_number/2
def guess_number():
    # first_number = 1
    # second_number = 100
    print("Welcome to the Number Guessing Game")
    print("I'm Thinking of a number between 1 and 100")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == 'easy':
        attempt = 10
        print(f"You Have {attempt} attempts remaining to guess the number")
    elif difficulty_level == 'hard':
        attempt = 5
        print(f"You Have {attempt} attempts remaining to guess the number")
    else:
        print("you type wrong difficulty level")
        guess_number()
    for i in range(0,attempt):
        guessed_number = int(input("Make a Guess: "))
        # print(f"Make a guess: {guessed_number}")
        if guessed_number > selected_number:
            print("Too High \nGuess Again")
            attempt -= 1
            print(f"You Have {attempt} attempts remaining to guess the number")
            # second_number = guessed_number
        elif guessed_number < selected_number:
            print("Too low \nGuess Again")
            attempt -= 1
            print(f"You Have {attempt} attempts remaining to guess the number")
            # first_number = guessed_number
        elif guessed_number == selected_number:
            print(f"You got it! The answer was {guessed_number}")
            break
        else:
            print("You pressed Wrong key")
            attempt += 1
    if attempt == 0:
        print("Total attempt left 0 and you didn't guess the answer you loss")
guess_number()



 
        