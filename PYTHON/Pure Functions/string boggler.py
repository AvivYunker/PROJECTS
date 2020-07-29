import random
def string_boggler (strr):
    strr = str(strr)
    arr = []
    res = ''
    chars_into_array(arr, strr)
    d = all_minus(arr)
    lim = len(arr)
    while (d == 0):
        rndm = random.randrange(0, lim)
        if (arr[rndm] != int(-1)):
            res += str(arr[rndm])
            arr[rndm] = int(-1)
            d = all_minus(arr)
    return res

def chars_into_array (arr, strr):
    strr = str(strr)
    lim = len(strr)
    for cnt in range(0, lim, 1):
        arr.append(str(strr[cnt]))


def all_minus (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != int(-1)):
            return 0
    return 1



x = input("User, enter a string:\n")
x = str(x)
results = string_boggler(x)
print("The results are: " + str(results))
input("\nDONE!\n")
