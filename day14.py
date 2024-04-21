import os
import random

from art import day14_logo
from day14_data import data

entry_a = random.choice(data)
entry_b = random.choice(data)

continue_game = True


def check_guess(letter, entry_a_followers, entry_b_followers):
    if entry_a_followers > entry_b_followers:
        return letter == 'a'
    if entry_b_followers > entry_a_followers:
        return letter == 'b'


def next_round_accounts(account_winner):
    global entry_a
    global entry_b
    entry_a = account_winner
    new_entry = random.choice(data)
    while new_entry == entry_a:
        new_entry = random.choice(data)
    entry_b = new_entry


def play_game(score):
    global continue_game
    while continue_game:
        print(day14_logo)

        if score > 0:
            print(f"Your score is {score} points")

        print(f"a: {entry_a['name']}, {entry_a['description']}, from {entry_a['country']}")
        print("==== VS ====")
        print(f"b: {entry_b['name']}, {entry_b['description']}, from {entry_b['country']}")

        a_followers = entry_a['follower_count']
        b_followers = entry_b['follower_count']

        player_guess = input("Who is more popular? Type 'a' or 'b': ").lower()

        result = check_guess(player_guess, a_followers, b_followers)
        if result:
            score += 1
            print(
                f"You're right! {entry_a['name']} has {entry_a['follower_count']} mln followers and {entry_b['name']} {entry_b['follower_count']} mln followers")
            if player_guess == 'a':
                next_round_accounts(entry_a)
            else:
                next_round_accounts(entry_b)

        else:
            print(
                f"You lost! {entry_a['name']} has {entry_a['follower_count']} mln followers and {entry_b['name']} {entry_b['follower_count']} mln followers")
            continue_game = False


play_game(0)
