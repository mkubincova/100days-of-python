import art
import random
from clear import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def main():
    if input("Do you want to play a game of Blackjack? Y/n ").lower() == 'y':
        clear()
        print(art.logo)

        play = True

        user_cards = [random.choice(cards),random.choice(cards)]
        comp_cards = [random.choice(cards),random.choice(cards)]

        # round 0
        if user_cards == [11,11]: user_cards = [1,11]
        if comp_cards == [11,11]: comp_cards = [1,11]

        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computers first card: {comp_cards[0]}")

        if sum(user_cards) == 21 or sum(comp_cards) == 21:
            play = False
        
        if play:
            # user's moves
            while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user_cards.append(random.choice(cards))

                if sum(user_cards) == 21: break

                if sum(user_cards) > 21:
                    if 11 in user_cards:
                        user_cards[user_cards.index(11)] = 1
                        if sum(user_cards) > 21:
                            break
                    else:
                        break

                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computers first card: {comp_cards[0]}")
            
            # computer's moves
            while sum(comp_cards) < 17:
                comp_cards.append(random.choice(cards))

        # final results
        user_total = sum(user_cards)
        comp_total = sum(comp_cards)

        print(f"Your final hand:{user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {comp_cards}, final score: {comp_total}")

        if user_total == 21 and comp_total == 21:
            print("Two Blackjacks, it's a draw")
        elif user_total == 21:
            print("You got Blackjack, you win!")
        elif comp_total == 21:
            print("Dealer has Blackjack, you lose...")
        elif user_total > 21:
            print("You overshot and lost")
        elif comp_total > 21:
            print("Dealer overshot, you win")
        elif user_total == comp_total:
            print("It's a draw")
        elif user_total > comp_total:
            print("You win")
        else:
            print("You lose")

        main()
        
main()