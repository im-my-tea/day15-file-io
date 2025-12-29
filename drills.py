# Open the file using the relative path
with open("./Input/Names/invited_names.txt", "r") as names_file:
    # Read all lines into a list
    names_list = names_file.readlines()
    
# Print raw list to see the \n characters
print(names_list)

clean_names = []
for name in names_list:
    # .strip() removes whitespace (spaces, tabs, newlines) from start and end
    clean_names.append(name.strip())

print(clean_names)

# Create a dummy letter
with open("./Output/ReadyToSend/test_letter.txt", "w") as letter:
    letter.write("This is a test letter inside a deep folder.")