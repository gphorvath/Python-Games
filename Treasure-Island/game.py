import random
import os
from art_pack import (
    boat,
    fire,
    island,
    light,
    monster,
    shark,
    three_doors,
    tiger,
    treasure_chest,
    treasure_map, 
)

print(island)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go?")
if input("Type 'left' or 'right'\n") != "left":
    os.system("clear")
    print(tiger)
    print("Before you can set off, you are attacked and killed by a tiger!")
else:
    os.system("clear")
    print(treasure_map)
    print("You have stumbled across a treasure map:")
    print("You follow the map until you find a lake.")
    print("There is an island in the middle of the lake.")
    if (input("Type 'swim' or 'wait'.\n") != "wait"):
        os.system("clear")
        print(shark)
        print("After a short time swimming, you are killed by a shark.")
    else:
        os.system("clear")
        print("You pause for a minute, looking around...")
        print("Tucked behind a nearby bush you find a small boat.")
        print(boat)
        print("You make use of the row boat to navigate safely to the island.")
        input("Row! (Type anything)\n")
        os.system("clear")
        colors = ["yellow", "red", "blue"]
        rand_color = random.choice(colors)
        colors.remove(rand_color)
        print("On the island you find a house with 3 doors. One red, one yellow and one blue.")
        print(three_doors)
        color_choice = input("Which colour do you choose to open? (Type 'red', 'yellow', or 'blue')\n")
        print(light)
        print("But wait... a feeling comes over you!")
        if (color_choice == rand_color):
            rand = random.randint(0, 1)
            print(f"The {colors[rand]} door is most certainly a trap!")
            if (input("Would you like to change doors? (Type 'yes' or 'no')\n") != "no"):
                color_choice=colors[1-rand]
        elif (color_choice == colors[0]):
            print(f"The {colors[1]} door is most definitely a trap!")
            if (input("Would you like to change doors? (Type 'yes' or 'no')\n") == "yes"):
                color_choice = rand_color
        elif (color_choice == colors[1]):
            print(f"The {colors[0]} door is most assuredly a trap!")
            if (input("Would you like to change doors? (Type 'yes' or 'no')\n") == "yes"):
                color_choice = rand_color
        else:
            color_choice = " "

        if (color_choice == colors[0]):
            os.system("clear")
            print(fire)
            print("As you reach for the door, you fall through a trap door!")
            print("You were slain in a pit of fire!")
        elif (color_choice == colors[1]):
            os.system("clear")
            print(monster)
            print("As you reach for the door, the door bursts open!")
            print("You are slain by a monster!")
        elif (color_choice == rand_color):
            os.system("clear")
            print(treasure_chest)
            print("You discovered the treasure!")
            
print("Game Over.")
