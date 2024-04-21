import random

from art import day12_logo

DIFFICULTY_LEVEL = {
    "easy": 10,
    "hard": 5
}


def setup_random_number():
    num = random.randint(1, 100)
    return num


def check_input(number_to_guess, difficulty_level):
    attempts_left = difficulty_level
    print(f"You have {attempts_left} attempts to guess the number. Good luck!")

    while attempts_left > 0:
        num = int(input(f"Please enter the number: "))
        if num == number_to_guess:
            print(f"You win, the number is {number_to_guess}!")
        elif num > number_to_guess:
            attempts_left -= 1
            print(f"The number is too big. You have {attempts_left} attempts left")
        else:
            attempts_left -= 1
            print(f"The number is too small. You have {attempts_left} attempts left")
    else:
        print("You ran out of attempts, you lost.")


def play_game():
    print(day12_logo)
    print("Welcome to a guessing game. Pick a difficulty:")
    difficulty = input("Type 'easy' or 'hard': ")

    num_to_guess = setup_random_number()

    check_input(num_to_guess, DIFFICULTY_LEVEL[difficulty])

    return


play_game()
