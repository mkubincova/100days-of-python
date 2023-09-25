import art
from clear import clear

def calculate(num_1, operation, num_2):
    if operation == '+':
        return num_1 + num_2
    if operation == '-':
        return num_1 - num_2
    if operation == '*':
        return num_1 * num_2
    if operation == '/':
        return num_1 / num_2

def main():
    print(art.logo)

    keep_calculating = True

    num_1 = float(input("What is the first number?: "))
    print("+\n-\n*\n/")

    while keep_calculating:
        operation = input("Pick an operation: ")
        num_2 = float(input("What is the next number?: "))

        result = calculate(num_1, operation, num_2)
        print(f"{num_1} {operation} {num_2} = {result}")

        if input(f"Do you want to keep calculating with {result}? Y/n ").lower() == 'y':
            num_1 = result
        else:
            keep_calculating = False
            clear()
            main()

main()