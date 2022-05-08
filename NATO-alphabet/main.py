student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_ph_csv = pd.read_csv('NATO-alphabet\\nato_phonetic_alphabet.csv')
new_dict = {row.letter:row.code for (index,row) in nato_ph_csv.iterrows()}
# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# is_true = True
# while is_true:
def generate_pass():
    alphabet = input("Enter word: ").upper()
    try:
        word_list = [new_dict[word] for word in alphabet]
        # is_true = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_pass()
    else:
        print(word_list)
generate_pass()