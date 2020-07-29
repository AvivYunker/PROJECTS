import random
def n_random_digits (num):
    num = int(num)
    arr = []
    while (num > 0):
        digit = random.randrange(0, 10)
        arr.append(digit)
        if (num == 1):
            print(str(digit), end=".")
        else:
            print(str(digit), end=",")
        num = int(num - 1)
    print("")
    digit_histogram(arr)

def digit_histogram(arr):
    lim = len(arr)
    print("")
    for cnt in range(0, 10, 1):
        x = arr.count(cnt)
        if (x > 0):
            print(str(cnt), end=": (")
            for cnt2 in range (0, x, 1):
                print("*", end="")
            print(")")

x = input("User, how many random digits?\n")
x = int(x)
print("")

n_random_digits(x)
input("\nDONE!\n")
