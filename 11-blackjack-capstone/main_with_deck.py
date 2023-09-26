import art
import random
from clear import clear
from cards import create_deck, hidden_card, print_cards

cards = create_deck() 

def game_result(user_total, comp_total):
    """Takes player scores and returns message with game result."""
    if user_total == comp_total:
        return "Not great, not terrible. It's a draw. 🤝"
    elif user_total == 0:
        return "You got Blackjack, you win! 🥳"
    elif comp_total == 0:
        return "Dealer has Blackjack, you lose... 😭"
    elif user_total > 21:
        return "You overshot and lost. 😭"
    elif comp_total > 21:
        return "Dealer went over, you won. 🥳"
    elif user_total > comp_total:
        return "Hurray, you won. 🥳"
    else:
        return "Looks like you lost, better luck next time... 😭"

def calc_score(cards):
    """Takes a list of cards and returns its sum."""
    if sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def deal_card(index):
    """Takes card index and returns its value and image + index of the next card."""
    val = cards[index]["value"]
    img = cards[index]["ascii"]
    index += 1
    return val, img, index

def play_game():    
    print(art.logo)

    random.shuffle(cards)
    play = True
    next_card_index = 0

    user_cards = []
    comp_cards = []
    user_card_img = []
    comp_card_img = []

    for _ in range(2):
        val, img, next_card_index = deal_card(next_card_index)
        user_cards.append(val)
        user_card_img.append(img)

        val, img, next_card_index = deal_card(next_card_index)
        comp_cards.append(val)
        comp_card_img.append(img) 

    while play:
        user_total = calc_score(user_cards)
        comp_total = calc_score(comp_cards)

        print(f"Your current score: {user_total}")
        print_cards(user_card_img)
        print(f"Computer's score: {comp_cards[0]}")
        print_cards([comp_card_img[0], hidden_card])
        
        if user_total == 0 or comp_total == 0 or user_total > 21:
            play = False
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                val, img, next_card_index = deal_card(next_card_index)
                user_cards.append(val)
                user_card_img.append(img)
            else:
                while comp_total < 17:
                    val, img, next_card_index = deal_card(next_card_index)
                    comp_cards.append(val)
                    comp_card_img.append(img)
                    comp_total = calc_score(comp_cards)
                play = False
    
    print("---------------------------------------")
    print(f"Your final score: {user_total}")
    print_cards(user_card_img)
    print(f"Computer's final score: {comp_total}")
    print_cards(comp_card_img)
    print(game_result(user_total, comp_total))  

while input("Do you want to play a game of Blackjack? Y/n ").lower() == 'y':
    clear()
    play_game()
    print('')