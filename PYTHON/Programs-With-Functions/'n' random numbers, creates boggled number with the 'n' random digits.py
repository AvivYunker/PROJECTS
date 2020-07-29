import random
def n_random_digits (num):
    num = int(num)
    arr = []
    while (num > 0):
        digit = random.randrange(0, 10)
        arr.append(digit)
        print(str(digit), end=",")
        num = int(num - 1)
    results = number_boggler_array(arr)
    print("   The results are: " + str(results))

def number_boggler_array (arr):
    lim = len(arr)
    d = all_minus(arr)
    level = int(1)
    res = int(0)
    while (d == 0):
        rand = random.randrange(0, lim)
        if (arr[rand] != -1):
            res = int(res + int(arr[rand])*level)
            level = int(level * 10)
            arr[rand] = int(-1)
            d = all_minus(arr)
    return res

def all_minus(arr):
    sums = int(0)
    lim = len(arr)
    for cnt in range(0, lim, 1):
        sums = int(sums + arr[cnt])
    if (sums == int(-1*lim)):
        return 1
    else:
        return 0



x = input("User, how many random digits?\n")
x = int(x)

n_random_digits(x)
input("DONE!\n")
