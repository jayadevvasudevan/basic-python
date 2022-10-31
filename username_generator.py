full_name = input("Please enter your name: ")
first_letter = full_name[0]
space_index = full_name.find(" ")
three_letters_surname = full_name[space_index + 1:space_index + 4]
number = random.randrange (1,999)
username = (first_letter, three_letters_surname, number)
print = (username)
