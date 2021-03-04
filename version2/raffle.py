"""Randomly pick customer and print customer info"""

# Add code starting here

from random import choice

from customers import get_customers_from_file

def choose_winner():
    winner = choice(get_customers_from_file("customers.txt"))
    print(f"Tell {winner.name} at {winner.email} that they have won the raffle.")

choose_winner()
# Hint: remember to import any functions you need from
# other files or libraries
