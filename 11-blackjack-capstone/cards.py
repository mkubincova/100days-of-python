cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
colors = ['♠','♦','♥','♣']

def create_card(color, name):
    space = ''
    if len(name) != 2:
        space = ' '

    card = f'''
╔═════════╗
║{space}{name}       ║
║         ║
║    {color}    ║
║         ║
║       {name}{space}║
╚═════════╝
    '''.split("\n")
    return card

def create_deck():
    deck = []

    for color in colors:
        for card in cards:
            # card value
            if card == "A":
                value = 11
            elif card == "J" or card == "Q" or card == "K":
                value = 10
            else:
                value = card

            deck.append({
                "color": color,
                "name": str(card),
                "value": value,
                "ascii": create_card(color, str(card))
            })
    
    return deck

def print_cards(cardlist):
    for card in zip(*cardlist):
            print('   '.join(card))


hidden_card = '''
╔═════════╗
║░░░░░░░░░║
║░░░░░░░░░║
║░░░░░░░░░║
║░░░░░░░░░║
║░░░░░░░░░║
╚═════════╝
'''.split("\n")