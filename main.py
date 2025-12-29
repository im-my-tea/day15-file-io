with open("./Input/Names/invited_names.txt", 'r') as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt", 'r') as template:
    letter_content = template.read()

for name in names:
    name = name.strip()
    new_letter = letter_content.replace("[name]", name)
    # New File
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'w') as new_file:
        new_file.write(new_letter)

