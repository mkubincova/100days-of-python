from clear import clear
import art

def add_bid(bids):
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))

    bids[name] = bid

    more_bidders = input("Are there any other bidders? Y/n ").lower()
    if more_bidders == 'y':
        clear()
        add_bid(bids)

def get_winner(bids):
    top_bid = 0
    winner = ''

    for key in bids:
        if bids[key] > top_bid:
            top_bid = bids[key]
            winner = key
    
    return top_bid, winner


def main():
    print(art.logo)
    print("\nWelcome to the secret auction program.")

    bids = {}
    add_bid(bids)

    top_bid, winner = get_winner(bids)

    print(f"The winner is {winner} with a bid of ${top_bid}")

main()


