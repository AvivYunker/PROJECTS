import random
def lowercase_printer(num):
    num = int(num)
    while (num > 0):
        rndm = random.randrange(0, 25)
        letter = int(97)
        while (rndm > 0):
            print(chr(letter), end=",")
            rndm = int(rndm - 1)
            letter = int(letter + 1)
        print("")
        num = int(num - 1)


x = input("User, enter a number:\n")
x = int(x)
lowercase_printer(x)
input("\nDONE!\n")