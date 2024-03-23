import random
import os
from art_pack import (
    stages,
    win_stage,
    lose_stage,
)
from words import word_list

lives = len(stages) - 1
answer = random.choice(word_list)
display = []

for _ in answer:
    display += "_"

game_over = False

while not game_over:
    os.system("clear")
    print("Welcome to Hangman!")
    print(stages[lives])
    print(display)
    print("\n")
    letter = input("Choose a letter: ").lower()
    
    for position in range(len(answer)):
        if answer[position] == letter:
            display[position] = letter

    if not letter in answer:
        lives -= 1
        print(stages[lives])
        print(display)
        
    if "_" not in display:
        os.system("clear")
        print("Thank you for playing Hangman!")
        print("The answer was: ", answer)
        print(win_stage)
        print("You escape to play another day!")
        break
    elif lives == 0:
        os.system("clear")
        print("Thank you for playing Hangman!")
        print("The answer was: ", answer)
        print(lose_stage)
        print("You are hanged!")
        break
