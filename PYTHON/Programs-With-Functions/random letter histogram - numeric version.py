import random
def n_random_letters (num):
    num = int(num)
    arr = []
    while (num > 0):
        letter = random.randrange(97, 123)
        if (num == 1):
            print(chr(letter), end="")
        else:
            print(chr(letter), end=",")
        letter = int(letter - 97)
        arr.append(letter)
        num = int(num - 1)
    print("\n")
    letter_histogram(arr)

def letter_histogram (arr):
    lim = len(arr)
    for cnt in range (0, 26, 1):
        x = arr.count(cnt)
        if (x > 0):
            print(chr(cnt + 97), end=": (")
            print(str(x), end="/")
            print(str(lim), end="")
            print(")")

x = input("User, how many random letters?\n")
x = int(x)
print("")

n_random_letters(x)
input("\nDONE!\n")
