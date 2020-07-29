def between_ranges(lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> (")
        results = number_boggler(lower)
        print(str(results) + ")")
        lower = int(lower + 1)

import random
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


lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("DONE!\n")
