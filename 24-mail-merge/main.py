with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.read().split('\n')

for name in name_list:
    text = template.replace('[name]', name)

    with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as new_letter:
        new_letter.write(text)
