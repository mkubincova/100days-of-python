import art
from clear import clear

def add(num_1, num_2):
    return num_1 + num_2

def substract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        print("You cannot divide by 0!")
        return 0
    return num_1 / num_2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def main():
    print(art.logo)

    keep_calculating = True

    num_1 = float(input("What is the first number?: "))
    for key in operations:
        print(key)

    while keep_calculating:
        operation = input("Pick an operation: ")
        num_2 = float(input("What is the next number?: "))

        result = operations[operation](num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {result}")

        if input(f"Do you want to keep calculating with {result}? Y/n ").lower() == 'y':
            num_1 = result
        else:
            keep_calculating = False
            clear()
            main()

main()