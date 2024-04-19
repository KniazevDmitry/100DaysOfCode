import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

def deal_card(player, num):
    for n in num:
        player.append(random.choice(cards))

# initial draw of 2 cards:
deal_card(player_cards, 2)
print(f"player cards: {player_cards}")