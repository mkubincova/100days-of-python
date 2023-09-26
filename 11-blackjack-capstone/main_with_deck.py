import art
import random
from clear import clear
from cards import create_deck, hidden_card, print_cards

def print_game_result(user_total, comp_total):
    if user_total == 21 and comp_total == 21:
        print("Two Blackjacks, what are the odds? It's a draw. 🤝")
    elif user_total == 21:
        print("You got Blackjack, you win! 🥳")
    elif comp_total == 21:
        print("Dealer has Blackjack, you lose... 😭")
    elif user_total > 21:
        print("You overshot and unfortunatelly lost. 😭")
    elif comp_total > 21:
        print("Dealer overshot, you won. 🥳")
    elif user_total == comp_total:
        print("Not great, not terrible. It's a draw. 🤝")
    elif user_total > comp_total:
        print("Hurray, you won. 🥳")
    else:
        print("Looks like you lost, better luck next time... 😭")

def main():
    if input("Do you want to play a game of Blackjack? Y/n ").lower() == 'y':
        clear()
        print(art.logo)

        play = True
        cards = create_deck()
        random.shuffle(cards)   

        user_cards = [cards[0]["value"],cards[2]["value"]]
        comp_cards = [cards[1]["value"],cards[3]["value"]]

        user_card_img = [cards[0]["ascii"],cards[2]["ascii"]]
        comp_card_img = [cards[1]["ascii"],cards[3]["ascii"]]

        next_card_index = 4

        # round 0
        if user_cards == [11,11]: user_cards = [1,11]
        if comp_cards == [11,11]: comp_cards = [1,11]
        
        while play:
            # print current score
            print(f"Your current score: {sum(user_cards)}")
            print_cards(user_card_img)
            print(f"Computer's score: {comp_cards[0]}")
            print_cards([comp_card_img[0], hidden_card])

            # check Blackjack
            if sum(user_cards) == 21 or sum(comp_cards) == 21:
                play = False

            # check overshoot
            if sum(user_cards) > 21:
                if 11 in user_cards:
                    user_cards[user_cards.index(11)] = 1
                    if sum(user_cards) > 21:
                        play = False
                else:
                    play = False
                    
            # exit if game is finished (to skip computer moves)
            if play == False: break
            
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user_cards.append(cards[next_card_index]["value"])
                user_card_img.append(cards[next_card_index]["ascii"])
                next_card_index += 1
            else:
                while sum(comp_cards) < 17:
                    comp_cards.append(cards[next_card_index]["value"])
                    comp_card_img.append(cards[next_card_index]["ascii"])
                    next_card_index += 1
            
                play = False

        # final results
        user_total = sum(user_cards)
        comp_total = sum(comp_cards)

        print("---------------------------------------")
        print(f"Your final score: {user_total}")
        print_cards(user_card_img)
        print(f"Computer's final score: {comp_total}")
        print_cards(comp_card_img)

        print_game_result(user_total, comp_total)
        print('')
        
        main()
        
main()