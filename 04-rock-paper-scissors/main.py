import random

### Winning combinations ###

# human         :   computer
# [0]rock       :   [2]scissors
# [1]paper      :   [0]rock
# [2]scissors   :   [1]paper

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
         ________)
        ________)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock, paper, scissors]

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

print(hand[human])
print("Computer chose:")
print(hand[computer])

if (human == computer):
    print("It's a draw.")
elif (
    (human == 0 and computer == 2) or 
    (human == 1 and computer == 0) or 
    (human == 2 and computer == 1)):
    print("You win!")
else:
    print("You lose...")