import random
def string_boggler (word):
    word = str(word)
    arr = []
    string_to_array(word, arr)
    results = actual_boggler(arr)
    return results

def string_to_array (word, arr):
    word = str(word)
    lim = len(word)
    for cnt in range(0, lim, 1):
        arr.append(word[cnt])

def actual_boggler (arr):
    lim = len(arr)
    res = str(0)
    d = are_all_zero(arr)
    while (d == 0):
        rndm = random.randrange(0, lim, 1)
        if (arr[rndm] != -1):
            res += str(arr[rndm])
            arr[rndm] = int(-1)
        d = are_all_zero(arr)
    return res

def are_all_zero(arr):
    lim = len(arr)
    sums = int(0)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != -1):
            return 0
    return 1

x = input("User, enter a word:  ")
x = str(x)
results = string_boggler(x)
print("The results are: " + str(results))
input("\nDONE!\n")
