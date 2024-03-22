import random
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
    print(tiger)
    print("Before you can set off, you are attacked and killed by a tiger!")
else:
    print(treasure_map)
    print("You have stumbled across a treasure map:")
    print("You follow the map until you find a lake.")
    print("There is an island in the middle of the lake.")
    if (input("Type 'swim' or 'wait'.\n") != "wait"):
        print(shark)
        print("After a short time swimming, your are killed by a shark.")
    else:
        print("You pause for a minute, looking around...")
        print("Tucked behind a nearby bush you find a small boat.")
        print(boat)
        print("You make use of the row boat to navigate safely to the island.")
        input("Row! (Type anything)\n")
        print("On the island you find a house with 3 doors. One red, one yellow and one blue.")
        print(three_doors)
        color = input("Which colour do you choose to open? (Type 'red', 'yellow', or 'blue')\n")
        print(light)
        print("But wait... a feeling comes over you!")
        if (color == "red"):
            print("The blue door is most certainly a trap!")
            if (input("Would you like to change doors? (Type 'yes' or 'no')\n") == "yes"):
                color = "yellow"
        elif (color == "blue"):
            print("You are certain that the red door is a trap!")
            if (input("Would you like to change doors? (Type 'yes' or 'no')\n") == "yes"):
                color = "yellow"
        elif (color == "yellow"):
            rand = random.randint(0, 1)
            if (rand == 0):
                print("The blue door is most certainly a trap!")
                if (input("Would you like to change doors? (Type 'yes' or 'no')\n") != "no"):
                    color = "red"
            else:
                print("You are certain that the red door is a trap!")
                if (input("Would you like to change doors? (Type 'yes' or 'no')\n") != "no"):
                    color = "blue"
        else:
            color = " "

        if (color == "red"):
            print(fire)
            print("As you reach for the door, you fall through a trap door!")
            print("You were slain in a pit of fire!")
        elif (color == "blue"):
            print(monster)
            print("As you reach for the door, the door bursts open!")
            print("You are slain by a monster!")
        elif (color == "yellow"):
            print(treasure_chest)
            print("You discovered the treasure!")
            
print("Game Over.")
