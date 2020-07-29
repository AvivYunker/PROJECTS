import random
def n_random_capital_letters (num):
    num = int(num)
    while (num > 0):
        rndm = random.randrange(65, 90)
        print(chr(rndm), end="")
        num = int(num - 1)


x = input("User, how many random (capital) letters?\n")
x = int(x)
n_random_capital_letters(x)
input("\n\nDONE!\n")
