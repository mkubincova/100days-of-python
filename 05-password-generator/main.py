import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword generator!")

num_letters = input("How many letters would you like in your password?\n")
num_symbols = input("How many symbols would you like?\n")
num_numbers = input("How many numbers would you like?\n")

password = ""

for n in range(0, int(num_letters)):
    password += letters[random.randint(0, len(letters) - 1)]

for n in range(0, int(num_symbols)):
    password += symbols[random.randint(0, len(symbols) - 1)]

for n in range(0, int(num_numbers)):
    password += numbers[random.randint(0, len(numbers) - 1)]

print(f"Here is your password: {password}")