import random
import os
from art_pack import (
    stages,
    logo,
    win_stage,
    lose_stage,
)
from words import word_list

def game_loop():

    lives = len(stages) - 1
    answer = random.choice(word_list)
    display = []
    wrong_guesses = []

    for _ in answer:
        display += "_"

    game_over = False

    while not game_over:
        os.system("clear")
        print(logo)
        print(stages[lives])
        print(display)
        print("\n")
        print(f"Wrong gueses: {wrong_guesses}\n")
        letter = input("Choose a letter: ").lower()
        
        for position in range(len(answer)):
            if answer[position] == letter:
                display[position] = letter

        if not letter in answer and not letter in wrong_guesses:
            lives -= 1
            wrong_guesses.append(letter)
            
        if "_" not in display:
            os.system("clear")
            print("Thank you for playing Hangman!")
            print("The answer was: ", answer)
            print(win_stage)
            print("You escape to play another day!")
            game_over = True
        elif lives == 0:
            os.system("clear")
            print("Thank you for playing Hangman!")
            print("The answer was: ", answer)
            print(lose_stage)
            print("You are hanged!")
            game_over = True
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if "y" in play_again:
        return game_loop()
            
if __name__ == "__main__":
    game_loop()
