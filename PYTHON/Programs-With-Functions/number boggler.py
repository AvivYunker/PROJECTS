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

x = input("User, enter a number:\n")
x = int(x)

results = number_boggler(x)
print("The results are: " + str(results))
input("DONE!\n")
