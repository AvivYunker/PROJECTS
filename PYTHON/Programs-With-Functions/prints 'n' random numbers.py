import random
def n_random_numbers (num):
    num = int(num)
    while (num > 0):
        rndm = random.randrange(0, 100001)
        print(str(rndm), end=",")
        num = int(num - 1)


x = input("User, enter a number:\n")
x = int(x)

n_random_numbers(x)
input("\nDONE!\n")
