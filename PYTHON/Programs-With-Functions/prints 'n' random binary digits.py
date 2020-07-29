import random
def n_random_binary_digits (num):
    num = int(num)
    while (num > 0):
        digit = random.randrange(0, 2)
        print(str(digit), end="")
        num = int(num - 1)

x = input("User, how many digits?\n")
x = int(x)

n_random_binary_digits(x)
input("\nDONE!\n")
