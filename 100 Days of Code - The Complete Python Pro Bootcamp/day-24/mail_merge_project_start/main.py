# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


invited_names = "./Input/Names/invited_names.txt"
starting_letter = "./Input/Letters/starting_letter.txt"
output_dir = "./Output/ReadyToSend/letter_for_"

with open(invited_names, mode='r') as names:
    contents = names.read()

    # creates name list
    names_list = contents.split('\n')

with open(starting_letter, mode='r') as letter:
    # reads letter and save it to a variable
    letter_content = letter.read()

# iterate through generated names list
for name in names_list:
    output_filename = output_dir + name + '.txt'
    output_letter = letter_content.replace("[name]", name)

    with open(output_filename, mode='w') as file:
        file.write(output_letter)
