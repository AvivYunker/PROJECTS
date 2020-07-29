# CREATED BY: Aviv Yunker
# NAME: "inserts 'n' boggled numbers into array"
# TAGS: boggled, input, function, return, if-else, for-in, 
# EXPLANATION: This will first ask for a number. Then - ask for number of boggles.
# Then - it will insert 'n' (second input) boggled numbers (of the first input),
# and then it will print the results.
# EXAMPLE:
# input: 123, and 5:
# results: 123, 213, 321, 132, 312.
import random
def boggler_n_times (num, cnt, arr):
    num = int(num)
    cnt = int(cnt)
    while (cnt > 0):
       results = number_boggler(num)
       arr.append(results)
       cnt = int(cnt - 1)

def number_boggler (num):
    num = int(num)
    arr = []
    digits_to_array(num, arr)
    d = are_all_minus(arr)
    lim = len(arr)
    level = int(1)
    sums = int(0)
    while (d == 0):
        rnd = random.randrange(0, lim)
        if (arr[rnd] != -1):
            sums = int(sums + arr[rnd]*level)
            level = int(level * 10)
            arr[rnd] = int(-1)
            d = are_all_minus(arr)
    return sums

def are_all_minus (arr):
    sums = int(0)
    lim = len(arr)
    for cnt in range(0, lim, 1):
        sums = int(sums + arr[cnt])
    if (sums == int(-1*lim)):
        return 1
    else:
        return 0

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def print_array_contents(arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (cnt == (lim-1)):
            print(str(arr[cnt]), end=".")
        else:
            print(str(arr[cnt]), end=", ")



x = input("User, enter a number:\n")
y = input("User, how many times to be boggled?\n")
arr = []

x = int(x)
y = int(y)

boggler_n_times(x, y, arr)
print_array_contents(arr)
input("\nDONE!\n") # This holds the CLI.
