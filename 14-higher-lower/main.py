import art
from game_data import data
import random
from clear import clear

def generate_items(data, b):
    '''Take a list of data, return two items that have different follower counts'''
    a = b
    b = random.choice(data)
    while a == b or a['follower_count'] == b['follower_count']:
        b = random.choice(data)
    return a, b

def check_answer(a, b, guess):
    '''Takes two items and user's guess. Checks if user is correct'''
    if a['follower_count'] > b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

def play_game():
    print(art.logo)

    playing = True
    score = 0
    b = random.choice(data)
    
    while playing: 
        a, b = generate_items(data, b)
 
        print(f"Compate A: {a['name']}, {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        clear()

        if check_answer(a, b, guess):
            score += 1
            print(f"You're right! Current score: {score}\n")
        else:
            playing = False
            print(f"Incorrect! Final score: {score}")

play_game()