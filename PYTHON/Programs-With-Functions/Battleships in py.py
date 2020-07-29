# CREATED BY: Aviv Yunker
# NAME: "Small battleships game"
# TAGS: battle-ships, print, list, shot, append, return, small, for-in, if-elif, while
# EXPLANATION: this is a simple battle-ships game. There's a board of 16 cells - each of them
# either contains a piece of a ship or not. The game ends when the player had
# shot all 9 scattered pieces.

# this is a battleships game written in Python
# a matrix 4X4 is presented in this game
# '0' means open sea - where there aren't any ships
# '1' means that there is a piece of a ship
# '2' is a place where the ship had been shot
# '3' is a place where the open-sea (without ships) had been shot
# when the user had reached 9 shots - the game will end, and will print "You Win!"
import os
def insert_into_array (arr):
    arr.append(1)
    arr.append(1)
    arr.append(1)
    arr.append(0)
    arr.append(0)
    arr.append(1)
    arr.append(1)
    arr.append(1)
    arr.append(1)
    arr.append(1)
    arr.append(1)
    arr.append(0)
    arr.append(0)
    arr.append(0)
    arr.append(0)
    arr.append(0)

def print_array_contents (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (cnt % 4 == 0):
            print("")
        print(str(arr[cnt]), end="")
    print("")

def shoot_unit (arr):
    unt = input("User, enter a number from 1 to 16:\n")
    unt = int(unt)
    unt = int(unt - 1)
    if (arr[unt] == int(1)):
        arr[unt] = int(2)
        input("Good shot! (press any key to continue)\n")
    elif (arr[unt] == int(0)):
        arr[unt] = int(3)
        input("Wrong shot, (press any key to continue)\n")
    elif (arr[unt] == int(2)):
        input("Already had a good shot in this unit (press any key to continue)\n")
    elif (arr[unt] == int(3)):
        input("Already had a wrong shot in this unit (press any key to continue)\n")
    os.system('cls')


def nine_reds (arr):
    lim = len(arr)
    reds = int(0)
    for cnt in range(0, lim, 1):
        if (int(arr[cnt]) == int(2)):
            reds = int(reds + 1)
    if (reds == 9):
        return 1
    else:
        return 0

arr = []
insert_into_array(arr)
print_array_contents(arr)
d = nine_reds(arr)
while (d == 0):
    shoot_unit(arr)
    d = nine_reds(arr)
    print_array_contents(arr)
input("\nYou win!\n") # This holds the CLI.
