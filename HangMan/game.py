import random
from art_pack import stages

lives = 6
word_list = [
    "taco", 
    "tuesday",
    "chinchilla",
    ]

answer = random.choice(word_list)
display = []

for _ in answer:
    display += "_"

print(stages[lives])
print(display)

game_over = False

while not game_over:
    letter = input("Choose a letter: ").lower()
    
    for position in range(len(answer)):
        if answer[position] == letter:
            display[position] = letter

    if letter in answer:
        print(display)
    else:
        lives -= 1
        print(stages[lives])
        print(display)
        
    if "_" not in display:
        print("You win!")
        game_over = True
    elif lives == 0:
        print("You lose!")
        game_over = True
