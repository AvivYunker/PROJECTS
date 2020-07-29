import random
def decimal_boggler (num):
    num = int(num)
    arr = []
    res = int(0)
    level = int(1)
    digits_to_array(arr, num)
    d = all_minus(arr)
    lim = len(arr)
    while (d == 0):
        rndm = random.randrange(0, lim)
        if (arr[rndm] != int(-1)):
            res = int(res + arr[rndm] * level)
            level = int(level * 10)
            arr[rndm] = int(-1)
            d = all_minus(arr)
    return res

def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def all_minus (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != int(-1)):
            return 0
    return 1

x = input("User, enter a number:\n")
x = int(x)
results = decimal_boggler(x)
print("The results are: " + str(results))
input("\nDONE!\n")
