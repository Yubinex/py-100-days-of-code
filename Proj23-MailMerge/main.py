PLACEHOLDER = "[name]"

with open("./Proj23-MailMerge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
with open("./Proj23-MailMerge/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        formatted_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, formatted_name)
        with open(f"./Proj23-MailMerge/Output/ReadyToSend/letter_for_{formatted_name}", mode="w") as new_letter_file:
            new_letter_file.write(new_letter)
