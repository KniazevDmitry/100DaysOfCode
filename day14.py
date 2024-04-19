import random

from art import day14_logo
from day14_data import data

entry_a = random.choice(data)
entry_b = random.choice(data)

print(day14_logo)

print(f"a: {entry_a['name']}, {entry_a['description']}, from {entry_a['country']}")
print("==== VS ====")
print(f"b: {entry_b['name']}, {entry_b['description']}, from {entry_b['country']}")
# ask to pick a or b
input = input("Who is more popular? Type 'a' or 'b': ")
# check if the answer is correct

# add a point for сorrect

# if correct - place b on the place of a and select another entry