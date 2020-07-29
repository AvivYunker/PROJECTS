import random
def n_dice_roles (num, arr):
    num = int(num)
    while (num > 0):
        roll = random.randrange(1,7)
        arr.append(roll)
        num = int(num - 1)

def print_array_contents (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (cnt == lim-1):
            print(str(arr[cnt]), end=" ")
        else:
            print(str(arr[cnt]), end=",")


x = input("User, how many dice-roles?\n")
x = int(x)
arr = []
n_dice_roles(x, arr)
print_array_contents(arr)
