from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(position_text,number_shift,direction):
    if direction == 'decode':
            number_shift *= -1
    cipher_text = ''
    for char in position_text:
        if char not in alphabet:
            cipher_text += char
        else:
            position = alphabet.index(char)
            new_position = position + number_shift
            cipher_text += alphabet[new_position]
    print(cipher_text)
user_input = True
while user_input:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift %= 26
    caesar(position_text=text,number_shift=shift,direction=direction)
    user = input('Type \'yes\' if you want to go again. Otherwise type \'no\'.\n').lower()
    if user == 'no':
        user_input = False
        print("Game Over")
    else:
        print("you did no write 'yes' or 'no' thats why i'm shut down this game \nGame Over")
        user_input = False
