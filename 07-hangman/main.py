import random
import art
import words
from clear import clear

end_of_game = False
lives = 6
guessed_letters = []

def print_game_progress():
    print(f"\n{' '.join(blanks)}")    
    print(f"{art.stages[lives]}\n")

# Intro
print(art.logo)
print("")

# 1. Generate the word
word = random.choice(words.word_list)
print(f"Chosen word: {word}")

# 2. Generate blanks for letters
blanks = []
for _ in range(len(word)):
    blanks.append("_")

### Game play ###
while not end_of_game:
    
    # 3. Ask user for guess
    user_guess = input("Guess a letter: ").lower()
    clear()

    if user_guess in guessed_letters:
        print(f"You have already guessed '{user_guess}'")
        print_game_progress()
        continue 

    guessed_letters.append(user_guess)

    
    # 4. Add letters to blanks
    for i in range(len(word)):
        if word[i] == user_guess:
            blanks[i] = word[i]

    # 5a. Incorrect guess
    if user_guess not in word:
        print(f"The letter '{user_guess}' is not in the chosen word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lost, the word was '{word}'.")
    
    # 5b. User guessed all letters
    if "_" not in blanks:
        end_of_game = True
        print("You won!")

    # print current status
    print_game_progress()

