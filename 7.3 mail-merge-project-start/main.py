#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp

        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# file = open('mail_marge/input/letters/starting_letter.docx','a')
# file.write("\nHello World")
# file.close()


# with open('mail_marge/input/letters/starting_letter.docx','r') as file:
#     content = file.readlines()
#     with open('mail_marge/input/Names/invited_names.txt','r') as names:
#         name_file = names.readlines()
#         for namess in range(len(name_file)):
#             content[0] = f"Dear {name_file[namess]},\n"
#             with open(f'mail_marge/output/invited_na{namess}.docx','w') as file:
#                 file.write("".join(content))
            

    # for line in content:
    #     result = line.split(',')
    #     print(result)



# good solution
PLACEHOLDER = "[name]"
with open('mail_marge/input/Names/invited_names.txt','r') as names_file:
    names = names_file.readlines()
with open('mail_marge/input/letters/starting_letter.docx','r') as starting_file:
    st_file = starting_file.read()
    for name in names:
        new_file = st_file.replace(PLACEHOLDER,name.strip())
        with open(f'mail_marge/output/ReadyToSend/starting_letter{name.strip()}.docx','w') as files:
            files.write(new_file)