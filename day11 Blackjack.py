import random

player_cards = []
dealer_cards = []

player_sum = 0
dealer_sum = 0

win = False
end_game = False


def deal_card(player, num):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for n in range(num):
        player.append(random.choice(cards))


def blackjack(cards_dealt):
    global win
    if set(cards_dealt) == {11, 10}:
        win = True
    return win


def game_over(reason):
    global end_game
    print(f"Game over! {reason}")
    end_game = True


def score(cards_dealt):
    score_sum = sum(cards_dealt)
    ace_dealt = cards_dealt.count(11)
    while score_sum > 21 and ace_dealt:
        score_sum -= 10
        ace_dealt -= 1

    return score_sum


def dealer_draws_cards():
    while sum(dealer_cards) <= 16:
        deal_card(dealer_cards, 1)
        print(f"dealer cards: {dealer_cards}")
        dealer_draws_cards()


def draw_another_card():
    if input(f"Do you want another card? Y or N: ") == "Y":
        deal_card(player_cards, 1)
        print(f"Your cards: {player_cards}")
        your_sum_score = score(player_cards)
        print(f"Your sum: {your_sum_score}")
        if not end_game:
            draw_another_card()
    else:
        dealer_draws_cards()
        dealer_sum_score = score(dealer_cards)
        print(f"dealer's sum: {dealer_sum_score}")


def check_score(user_score, computer_score):
    if user_score == 21 and not blackjack(computer_score):
        print("=========")
        print(f"your cards: {player_cards} ||| dealer cards: {dealer_cards}")
        print(f"your sum: {your_score} ||| dealer score: {dealer_score}")
        game_over("You got a 21!")

    if your_score <= 21 and dealer_score <= 21:
        if your_score > dealer_score:
            print("=========")
            print(f"your cards: {player_cards} ||| dealer cards: {dealer_cards}")
            print(f"your sum: {your_score} ||| dealer score: {dealer_score}")
            game_over("You win!")
        elif dealer_score > your_score:
            print("=========")
            print(f"your cards: {player_cards} ||| dealer cards: {dealer_cards}")
            print(f"your sum: {your_score} ||| dealer score: {dealer_score}")
            game_over("Dealer wins!")


# initial draw of 2 cards:
deal_card(player_cards, 2)
print("=========")
print(f"your cards: {player_cards}")
deal_card(dealer_cards, 2)

# check if anyone has a blackjack after initial draw
if blackjack(dealer_cards):
    game_over("Dealer got a blackjack!")
    print("=========")
    print(f"your cards: {player_cards} ||| dealer cards: {dealer_cards}")
elif blackjack(player_cards):
    game_over("You got a blackjack!")
    print("=========")
    print(f"your cards: {player_cards} ||| dealer cards: {dealer_cards}")
else:
    player_sum = score(player_cards)
    print(f"your sum = {player_sum}")
    print("=========")
    dealer_sum = score(dealer_cards)

# reveal computer's first card to a player:
if not blackjack(dealer_cards) and not blackjack(player_cards):
    print(f"The dealer's first card is a {dealer_cards[0]}")
    print("=========")

# ask if the player wants another card:
if not end_game:
    draw_another_card()

your_score = score(player_cards)
dealer_score = score(dealer_cards)

check_score(your_score, dealer_score)
