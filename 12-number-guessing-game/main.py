import random

art = '''
  ____                       _   _            _   _                 _               
  / ___|_   _  ___  ___ ___  | |_| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                     
'''

def get_attempts():
    lvl = input("Choose difficulty. Type 'e' for easy or 'h' for hard: ")
    if lvl == 'e':
        return 10
    return 5

def check_solution(guess, solution, attempts):
    '''Checks answer against guess, returns number of remaining guesses'''
    if guess == solution:
        print(f"You got it! The answer was {solution}")
    elif guess > solution:
        print("Too high")
        return attempts - 1
    elif guess < solution:
        print("Too low")
        return attempts - 1

def game():
    print(art)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = get_attempts()
    solution = random.randint(1, 100)
    guess = 0

    while guess != solution and attempts:
        print(f"You have {attempts} attempts left.")

        guess = int(input("Make a guess: "))
        attempts = check_solution(guess, solution,attempts)

        if attempts == 0:
            print(f"Game over, the correct answer was {solution}")
        elif guess != solution:
            print("Guess again")
       
game()