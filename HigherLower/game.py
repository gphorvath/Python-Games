import random
import os
from art import (
    logo,
    vs,
    lose,
)
from game_data import data

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game_loop(score):
    os.system('clear')


    print(logo)

    account_a = random.choice(data)
    account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")   
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if check_answer(guess, account_a['follower_count'], account_b['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}")
        input("Press Enter to continue")
        return game_loop(score)
    else:
        print(lose)
        print(f"Sorry, that's wrong. Final score: {score}")
        return
        
if __name__ == "__main__":
    game_loop(0)