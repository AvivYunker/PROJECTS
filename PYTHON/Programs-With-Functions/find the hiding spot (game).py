# CREATED BY: Aviv Yunker
# NAME: "find the hiding spot"
# TAGS: game, find, matrix, list, power, if-else, for-in, return, function, random, os
# EXPLANATION: this program will ask the user to enter the dimentions of the matrix.
# then - the program will hide a character - and request the user to find it
# (by placing guesses over the matrix). The game will end when the user
# had found the hiding spot.
# EXAMPLE:
# input 3:
# ___
# ___ - user needs to find hiding spot in 1 of 9 cells
# ___

import random
import os
def assign_size_array (arr, size):
    size = int(size)
    lim = int(pow(size, 2))
    for cnt in range(0, lim, 1):
        arr.append("_")

def print_array_contents (arr):
    lim = len(arr)
    rwcl = int(pow(lim, 0.5)) # combination of 'row' and 'col'
    for cnt in range(0, lim, 1):
        if (cnt % rwcl == 0):
            print("")
        print(str(arr[cnt]), end="")
    print("")

def randomly_assign_piece (arr, size):
    size = int(size)
    lim = int(pow(size, 2))
    rndm = random.randrange(0, lim)
    for cnt in range(0, lim, 1):
        if (cnt == rndm):
            arr.append(int(1))
        else:
            arr.append(int(0))

def game_over (arr, shot):
    lim = len(arr)
    if(int(arr[shot]) == int(1)):
        return 1
    else:
        return 0

def no_to_array (arr, shot):
    arr[shot] = 'X'

def yes_to_array (arr, shot):
    arr[shot] = '*'

x = input("User, enter size of the board:\n")
size = int(x)
arrFront = []
arrBack = []
assign_size_array(arrFront, size)
randomly_assign_piece(arrBack, size)
#print_array_contents(arrFront)
#print_array_contents(arrBack)
shot = int(-1)
d = game_over(arrBack, shot)
while (d == 0):
    shot = input("\nUser, enter a cell:\n")
    shot = int(shot)
    shot = int(shot - 1)
    d = game_over(arrBack, shot)
    if (d == 0):
        no_to_array(arrFront, shot)
        print_array_contents(arrFront)
        input("\nWRONG SHOT! (press any key to continue) \n")
        os.system('cls')
    else:
        yes_to_array(arrFront, shot)
        print_array_contents(arrFront)
        input("\nGOOD SHOT! (press any key to continue) \n")
        os.system('cls')
input("\nDONE!\n") # This holds the CLI.
