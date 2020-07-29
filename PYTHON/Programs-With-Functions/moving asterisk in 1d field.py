import random
import os
def assign_array_size (num):
    num = int(num)
    for cnt in range(0, num, 1):
        arr.append('_')

def print_array_contents (arr, size, plr_pos):
    lim = len(arr)
    plr_pos = int(plr_pos)
    print("\n\n")
    print("(", end="")
    for cnt in range (0, size, 1):
        if (cnt == plr_pos):
            print(str("*"), end="")
        else:
            print(str(arr[cnt]), end="")
    print(")")

def plr_mover (arr, size, plr):
    size = int(size)
    plr = int(plr)
    while (plr >= 0 and plr < size):
        print_array_contents(arr, size, plr)
        mv = input("User:\nA-left\nD-right:\n")
        mv = str(mv)
        if (mv == 'a' or mv == 'A'):
            plr = int(plr - 1)
        elif (mv == 'd' or mv == 'D'):
            plr = int(plr + 1)
        else:
            input("Wrong input, try again")
        os.system('cls')

def assign_init_pos(size):
    size = int(size)
    init_pos = random.randrange(0, size)
    return init_pos


x = input("User, enter size of field:\n")
x = int(x)
plr = int(0)
arr = []
assign_array_size(x)
plr = assign_init_pos(x)
plr_mover(arr, x, plr)
input("\nDONE!\n")
