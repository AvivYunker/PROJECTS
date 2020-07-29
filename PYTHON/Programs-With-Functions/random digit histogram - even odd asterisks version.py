import random
def n_random_digits (num):
    num = int(num)
    arr = []
    while (num > 0):
        digit = random.randrange(0,10)
        arr.append(digit)
        if (num == 1):
            print(str(digit), end=".")
        else:
            print(str(digit), end=",")
        num = int(num - 1)
    even_odd_histogram(arr)

def even_odd_histogram(arr):
    cntE = int(0)
    cntO = int(0)
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (arr[cnt] % 2 == 0):
            cntE = int(cntE + 1)
        else:
            cntO = int(cntO + 1)
    print("\n")
    print("EVENS: ", end = "(")
    for cnt2 in range(0, cntE, 1):
        print("*", end="")
    print(")")
    print("ODDS: ", end = "(")
    for cnt3 in range(0, cntO, 1):
        print("*", end="")
    print(")")

x = input("User, how many random digits?\n")
x = int(x)
print("")
n_random_digits(x)
input("\nDONE!\n")
