import random
import os
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def generate_number():
    return random.randint(1, 100)

def get_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Invalid difficulty.")
        return get_difficulty()
    
def get_guess():
    return int(input("Make a guess: "))

def check_guess(guess, number, attempts):
    if guess == number:
        print(f"Congratulations! The number was {number}.")
        return attempts
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print("Too high.")
        return attempts - 1

def game_loop():
    os.system('clear')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = generate_number()
    guess = 0
    attempts = get_difficulty()
        
    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = get_guess()
        attempts = check_guess(guess, number, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            break
            
    if input("Do you want to play again? Type 'yes' or 'no': ").lower() == 'yes':
        game_loop()
        
        
game_loop()
    